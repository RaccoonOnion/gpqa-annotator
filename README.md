# GPQA Diamond Dataset Annotation Tool

A web-based tool designed for annotating questions in the GPQA (General-Purpose Question Answering) Diamond Dataset, converting multiple-choice questions into open-ended formats with difficulty and confidence ratings.

## Overview

This application allows annotators to:

1. Upload a CSV file containing multiple-choice questions
2. Edit questions to make them open-ended
3. Rate each question's difficulty (1-5)
4. Indicate confidence in the ratings (1-5)
5. Add notes about each question
6. Download annotated data as CSV

## Features

- **User Authentication**: Simple name-based login system that assigns different question sets to different annotators
- **Progress Tracking**: Visual progress bar showing completion status
- **Auto-save**: Automatically saves work as you type or make selections
- **CSV Import/Export**: Upload questions from CSV and download annotations as CSV
- **Local Storage**: Saves annotations in the browser's local storage
- **Navigation History**: Remembers recently visited questions for quick access

## Getting Started

### Prerequisites

- A modern web browser (Chrome, Firefox, Safari, Edge)
- A CSV file with questions in the required format

### CSV Format Requirements

The input CSV file should have the following columns:
- `Question`: The original multiple-choice question
- `Correct Answer`: The correct answer option
- `Incorrect Answer 1`: First incorrect option
- `Incorrect Answer 2`: Second incorrect option
- `Incorrect Answer 3`: Third incorrect option
- `Subdomain`: The subject area of the question
- `Explanation`: Explanation of why the correct answer is correct

### Using the Tool

1. **Upload Data**:
   - Click the file upload area on the login screen
   - Select a properly formatted CSV file
   - Wait for the file to process (you'll see a success message when complete)

2. **Login**:
   - Select your name from the dropdown
   - Click "Start Annotation"

3. **Annotate Questions**:
   - Edit the question text to make it open-ended (remove "Choose the correct answer" and similar directives)
   - Select difficulty rating (1-5, where 1 is easiest and 5 is hardest)
   - Select confidence rating (1-5, where 1 is least confident and 5 is most confident)
   - Add any notes in the notes field
   - Use "Next" and "Previous" buttons to navigate between questions

4. **Save Your Work**:
   - The tool auto-saves as you work
   - Click the "Save" button to manually save
   - All work is stored in your browser's local storage

5. **Download Annotations**:
   - Click the "Download CSV" button to export your annotations as a CSV file

## Annotation States

Questions can be in one of three states:
- **Not Annotated** (○): No changes have been made to the question
- **Incomplete** (!): Some changes have been made, but either difficulty or confidence ratings are missing
- **Annotated** (✓): Question has been edited and both ratings have been provided

## Tips for Effective Annotation

- **Making Questions Open-Ended**: Remove multiple-choice indicators and rephrase to ask for the answer directly
- **Difficulty Rating**: Consider the depth of knowledge required, complexity of reasoning, and ambiguity
- **Confidence Rating**: Reflect how confident you are in your difficulty assessment
- **Notes**: Use for documenting special considerations, challenges, or observations about the question

## Troubleshooting

- **Data Not Loading**: Ensure your CSV file follows the required format
- **Progress Not Saving**: Check that you haven't cleared your browser's local storage
- **Can't Proceed to Next Question**: If you've modified the question, you must provide both difficulty and confidence ratings

## Technical Information

This tool runs entirely in your browser and doesn't require a server. All data is processed locally, and annotations are stored in your browser's local storage. No data is sent to any external server.

---

For questions or issues, please contact the dataset administrators.
