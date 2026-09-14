# AI Workout Coach

AI Workout Coach is a real-time computer vision fitness assistant built with Python, OpenCV, MediaPipe, and Flask.

It uses your webcam to detect body movements, count bicep curl repetitions, calculate elbow angles, and provide basic form feedback through a web dashboard.

## Features

- Real-time pose detection
- Bicep curl rep counting
- Left and right arm tracking
- Elbow angle calculation
- Up/Down movement detection
- Form score and feedback
- Live webcam feed
- Real-time workout dashboard

## Tech Stack

- Python
- OpenCV
- MediaPipe
- Flask
- HTML
- CSS
- JavaScript

## How It Works

The application captures video from the webcam and uses MediaPipe to detect body landmarks.

For bicep curls, it tracks:

**Shoulder → Elbow → Wrist**

The elbow angle is used to detect the movement stage and count repetitions.

The application also analyzes the movement and provides basic feedback about the user's form.

## Installation

Clone the repository:

```bash
git clone https://github.com/adityapandey7353/AI-Workout-Coach.git
cd AI-Workout-Coach
```
Install the required dependencies:
```
pip install -r requirements.txt

```
Run the Application

Start the Flask server:
```
python main.py
```
Then open this URL in your browser:
```
http://127.0.0.1:5000
```
Allow camera access when prompted.

Currently, the application supports:

Bicep Curls,
Right arm tracking, 
Left arm tracking, 
Repetition counting, 
Basic form analysis, 

Future Improvements:

Add more exercises, 
Improve form detection, 
Add workout history, 
Add calorie estimation, 
Add user profiles, 
Add voice feedback, 
Improve exercise recognition

Author

Aditya Pandey
```
GitHub: https://github.com/adityapandey7353
