![Digiteq Logo](https://www.savs.cz/image-cache/db-public/images/3331/image/digiteq-logo-rgb.jpg_1000x259.jpg?ts=1720481469)
# Digiteq Automotive Python Hackathon

## Overview
This project is a Python-based solution for detecting and classifying emojis in images. It processes a dataset of images, identifies emojis, and classifies them into predefined categories such as "happy", "sad", "angry", "crying", and "surprised".

## The Hackathon Challenge
The challenge is to spot five types of emojis (happy, sad, crying, surprised, and angry) within a picture that's 800x600. These emojis can come in different sizes, colors, rotations, tilts, and may be a bit distorted. You might also find multiple emojis of each type in one picture. Before you start coding, take a look at the dataset to see what you're working with. You will be provided more then 1000 pictures for training and validation. Subsequently, at the end of the day your algorithm will be automatically tested on 280 pictures with the same data distribution. The output of the code will consist of the name of the picture, the name of each detected emoji, and the coordinates of the top-left corner of each detected emoji. This will allow for the identification of multiple emojis within a single picture. You will be awarded 1 point for each correctly classified emoji and 0.5 points for emojis that are properly classified but have coordinates off by 40 pixels or more. In case of missclassified emoji you lose 0.5 points.

## Features
- Detects emojis in images using contour detection.
- Classifies emojis based on edge detection and pixel intensity.
- Handles merging of emoji parts and filters overlapping detections.
- Outputs predictions in a standardized format for evaluation.

## File Structure
evaluate_main.py: Automatic evaluations program.
evaluation.py: Contains the evaluation logic for comparing predictions with ground truth labels.
your_implementation.py: Main implementation for emoji detection and classification.
requirements.txt: Lists the required Python libraries.
data: Folder with multiple datasets.
.venv: Virtual environment folder.

## Usage
Set up the project on your machine:
```bash
    git clone https://github.com/RomanAlexandroff/Digiteq_Python_Hackathon.git
    cd Digiteq_Python_Hackathon
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
```
Run the automatic evaluation:
```bash
    python evaluate_main.py data/train/labels.csv
```
Evaluate the results.

To try the solution on another dataset:
- change the path to datasets in your_implementation.py, row 40
- change the path to datasets when calling python evaluate_main.py data/SOME_OTHER_DATASET/labels.csv

## How It Works
Emoji Detection:
- The program reads images from the dataset folder.
- Converts images to grayscale and applies binary thresholding.
- Finds contours to detect emoji positions.

Emoji Classification:
- Crops detected emoji regions.
- Uses edge detection and pixel intensity to classify emojis into categories.

Output:
- Prints the detected emojis and their coordinates in the format:
```
Picture: <image_name>
Emoji: <emoji_type> Coordinates: (<x>, <y>)
```

## Error Handling
The program skips images that are missing or cannot be processed.
Outputs detailed error messages for debugging.

## Credits
Automatic Evaluation Program by Digiteq Automotive.
Solution by Roman Alexandrov
Email: r.aleksandroff@gmail.com