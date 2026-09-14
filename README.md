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
How It Works

The application captures video from the webcam and uses MediaPipe to detect body landmarks.

For bicep curls, it tracks:

Shoulder → Elbow → Wrist

The elbow angle is used to detect the movement stage and count repetitions.

The application also analyzes the movement and provides basic feedback about the user's form.

Installation

Clone the repository:

git clone https://github.com/adityapandey7353/AI-Workout-Coach.git

Go to the project folder:

cd AI-Workout-Coach

Create a virtual environment:

python -m venv venv

Activate it on Windows:

venv\Scripts\activate

Install the dependencies:

pip install -r requirements.txt
Run the Application

Start the Flask server:

python main.py

Open the application in your browser:

http://127.0.0.1:5000

Allow webcam access and start performing bicep curls.

Current Exercise

Bicep Curl

Supported:

Right arm
Left arm
Automatic rep counting
Elbow angle tracking
Form analysis
Future Improvements
Add more exercises
Workout history
Exercise selection
Workout timer
Progress tracking
Voice feedback
Improved form analysis
Calorie estimation
Author

Aditya Pandey

GitHub: https://github.com/adityapandey7353

