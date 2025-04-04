"""
python GPQAPro-inference.py --model meta-llama/Llama-3.1-8B-Instruct 2>&1 | tee output_llama.log
python GPQAPro-inference.py --model google/gemma-2-9b-it 2>&1 | tee output_gemma.log
python GPQAPro-inference.py --model Qwen/Qwen2.5-7B-Instruct 2>&1 | tee output_qwen.log
python GPQAPro-inference.py --model microsoft/phi-4 2>&1 | tee output_phi.log
python GPQAPro-inference.py --model Qwen/Qwen2.5-7B-Instruct --input_file sample_questions.jsonl
"""

import argparse
import json
import re
from vllm import LLM, SamplingParams

# ---- Parse CLI args ----
parser = argparse.ArgumentParser()
parser.add_argument("--model", type=str, required=True, help="Model name")
parser.add_argument("--input_file", type=str, default="questions.jsonl", help="Input JSONL with questions")
args = parser.parse_args()

model_name = args.model
input_file = args.input_file

# ---- Load model ----
llm = LLM(
    model=model_name,
    dtype="bfloat16",
    tensor_parallel_size=1,
    trust_remote_code=True
)

# ---- Sampling parameters ----
sampling_params = SamplingParams(
    temperature=0.7,
    top_p=0.9,
    max_tokens=2048
)

# ---- Load questions ----
with open(input_file, "r") as f:
    questions = [json.loads(line) for line in f]

# ---- Prompt builders for each model ----
def build_prompt(question, model_name):
    instruction = """You are a helpful assistant.

First, reason step by step to answer the user's question.

Then, output your final answer and confidence like this:
<GPQAPro-Answer>Your final answer here</GPQAPro-Answer>
<GPQAPro-Confidence>High / Medium / Low</GPQAPro-Confidence>"""

    if "phi-4" in model_name.lower():
        return f"<|im_start|>system\n{instruction}<|im_end|>\n<|im_start|>user\n{question}<|im_end|>\n<|im_start|>assistant\n"
    # Existing conditions for other models
    elif "gemma" in model_name.lower():
        return f"<start_of_turn>system\n{instruction}<end_of_turn>\n<start_of_turn>user {question}<end_of_turn>\n<start_of_turn>model "
    elif "llama" in model_name.lower():
        return (
            f"<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n"
            f"{instruction}<|eot_id|>\n"
            f"<|start_header_id|>user<|end_header_id|>\n"
            f"{question}<|eot_id|>\n"
            f"<|start_header_id|>assistant<|end_header_id|>\n"
        )
    elif "qwen" in model_name.lower():
        return (
            f"<|im_start|>system\n{instruction}<|im_end|>\n"
            f"<|im_start|>user\n{question}<|im_end|>\n"
            f"<|im_start|>assistant\n"
        )
    else:
        raise ValueError(f"Unsupported model: {model_name}")


prompts = [build_prompt(q["question"], model_name) for q in questions]

# ---- Run inference ----
outputs = llm.generate(prompts, sampling_params)

# ---- Tag-based parser ----
def extract_tagged_response(text):
    answer_match = re.search(r"<GPQAPro-Answer>(.*?)</GPQAPro-Answer>", text, re.DOTALL)
    confidence_match = re.search(r"<GPQAPro-Confidence>(.*?)</GPQAPro-Confidence>", text, re.DOTALL)

    errors = []
    answer = answer_match.group(1).strip() if answer_match else None
    confidence = confidence_match.group(1).strip().capitalize() if confidence_match else None

    if not answer:
        errors.append("missing_answer")
    if not confidence:
        errors.append("missing_confidence")

    reasoning = re.sub(r"<GPQAPro-(Answer|Confidence)>.*?</GPQAPro-\1>", "", text, flags=re.DOTALL).strip()

    result = {
        "reasoning": reasoning
    }
    if answer:
        result["answer"] = answer
    if confidence:
        result["confidence"] = confidence
    if errors:
        result["parse_error"] = errors

    return result

# ---- Save responses ----
output_file = f"responses_{model_name.split('/')[-1].replace('.', '_')}.jsonl"
with open(output_file, "w") as f:
    for q, out in zip(questions, outputs):
        raw_text = out.outputs[0].text.strip()
        parsed = extract_tagged_response(raw_text)
        result = {
            "id": q["id"],
            "question": q["question"],
            "raw_output": raw_text,
            "parsed": parsed
        }
        f.write(json.dumps(result) + "\n")

print(f"Saved {len(questions)} responses to {output_file}")