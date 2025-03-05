# GPQA Diamond Dataset Annotation Tool

A lightweight web application for annotating the GPQA (General-Purpose Question Answering) diamond dataset. This tool allows multiple annotators to convert multiple-choice questions into open-ended questions while tracking their progress and saving their work.

## Overview

This tool is designed to facilitate the annotation of the GPQA diamond dataset, which contains 198 multiple-choice questions. The annotation process involves:

1. Converting multiple-choice questions into open-ended questions
2. Rating the difficulty of the annotation process (1-5 scale)
3. Tracking progress and saving annotations

## Getting Started

### Prerequisites

- A modern web browser (Chrome, Firefox, Edge, Safari)
- The GPQA diamond dataset CSV file (`gpqa_diamond.csv`)
- No server or internet connection is required to run the app

### Installation

1. Download the `annotation-app.html` file to your computer
2. No installation is needed - the app runs entirely in your browser

## Usage

### 1. Loading the App

- Open the `annotation-app.html` file in your web browser
- You'll see the login screen with a file upload area and annotator selection dropdown

### 2. Uploading the Dataset

- Click on the file upload area and select the `gpqa_diamond.csv` file
- The file will be processed locally in your browser

### 3. Selecting Your Identity

- Choose your name from the dropdown menu (Ryan, Kartik, or Tom)
- Each annotator is assigned a specific subset of questions to avoid overlap:
  - Ryan: First third (questions 0-65)
  - Kartik: Middle third (questions 66-131)
  - Tom: Last third (questions 132-197)

### 4. Annotation Interface

After logging in, you'll see the main annotation interface with:

- **Progress bar**: Shows your completion percentage
- **Question editor**: A text area to rewrite the multiple-choice question as open-ended
- **Answer options**: Displays the correct answer (green) and incorrect answers (red)
- **Difficulty rating**: Rate how difficult the annotation was (1=easiest, 5=hardest)
- **Navigation controls**: Move between questions or jump to a specific question

### 5. Annotation Process

For each question:

1. Read the original multiple-choice question and the answer options
2. Edit the question to convert it to an open-ended format (e.g. remove the "Choose the correct answer" prompt and any multiple-choice framing)
3. Select a difficulty rating (1-5)
4. Click "Save" or simply navigate to the next/previous question (auto-save will trigger)

### 6. Data Persistence

- All annotations are automatically saved to your browser's localStorage
- Auto-saving occurs:
  - Every 30 seconds
  - When navigating between questions
  - When manually clicking the "Save" button
- Your progress is preserved even if you close the browser and return later

### 7. Exporting Annotations

- Click the "Download CSV" button to export your annotations
- The CSV includes:
  - Original question index
  - Your annotator name
  - Question subdomain
  - Original question
  - Your annotated (open-ended) question
  - Answer options
  - Difficulty rating
  - Timestamp of last save

## Features

- **User-specific assignments**: Each annotator sees only their assigned questions
- **Progress tracking**: Visual indication of completion percentage
- **Auto-save**: Prevents data loss
- **CSV export**: Easy data extraction for analysis
- **Offline operation**: Works without internet connection once loaded

## Troubleshooting

### Data Not Loading Properly
- Make sure you're using the correct CSV format
- Check that the file has the expected columns: "Question", "Correct Answer", "Incorrect Answer 1", "Incorrect Answer 2", "Incorrect Answer 3", and "Subdomain"

### Lost Progress
- Ensure you're using the same browser and device
- Browser localStorage can be cleared if you clear browsing data or use private/incognito mode
- Download CSV backups regularly

### Display Issues
- Try a different modern browser
- Ensure JavaScript is enabled

## Technical Notes

- The app uses browser localStorage which has a size limit (usually ~5MB)
- No data is sent to any servers; everything is processed locally
- The CSV parser uses the PapaParse library (included via CDN)

## Data Privacy

The application processes all data locally in your browser. No information is sent to any servers.

## Support

If you encounter issues or have questions about using this tool, please contact the project administrator.
