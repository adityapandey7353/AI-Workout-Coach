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

## Project Structure

```text
AI-Workout-Coach/
│
├── exercises/
│   ├── __init__.py
│   └── bicep_curl.py
│
├── static/
│   ├── script.js
│   └── style.css
│
├── templates/
│   └── index.html
│
├── utils/
│   ├── __init__.py
│   └── angle.py
│
├── main.py
├── pose_detector.py
├── requirements.txt
└── README.md
