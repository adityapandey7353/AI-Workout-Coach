# AI Workout Coach

> A real-time computer vision fitness assistant that tracks workout movements, counts repetitions, analyzes exercise form, and provides live feedback using your webcam.

---

## Overview

**AI Workout Coach** is a computer vision-based fitness application built with Python, OpenCV, MediaPipe, and Flask.

The application uses a webcam to detect body landmarks in real time and analyzes those landmarks to track exercise movements.

The current version focuses on **Bicep Curls**, including repetition counting, elbow-angle analysis, left/right arm selection, and form feedback.

The project started as a Python + OpenCV computer vision experiment and evolved into a web-based workout dashboard with a Flask backend and HTML, CSS, and JavaScript frontend.

---

## Features

### Computer Vision

- Real-time human pose detection
- MediaPipe Pose landmark detection
- Real-time elbow-angle calculation
- Movement stage detection
- Automatic repetition counting
- Left and right arm tracking

### Form Analysis

- Real-time form score
- Form quality classification
- Exercise-specific feedback
- Elbow-position analysis
- Live movement feedback

### Web Application

- Flask backend
- Live webcam streaming
- Real-time workout statistics
- Interactive workout dashboard
- Left/Right arm selection
- Responsive frontend
- Live rep, angle, stage, and form updates

---

## Demo

### Live Workout Detection

The application detects the user's pose through the webcam and overlays the detected landmarks and workout statistics.

![Workout Detection](screenshots/workout-detection.png)

### Web Dashboard

The Flask dashboard displays live workout information including repetitions, elbow angle, movement stage, and form status.

![Workout Dashboard](screenshots/dashboard.png)

> Add your own screenshots to the `screenshots/` folder and update the image names above.

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core application logic |
| OpenCV | Webcam capture and image processing |
| MediaPipe | Human pose detection |
| Flask | Backend and web server |
| HTML | Webpage structure |
| CSS | Dashboard styling |
| JavaScript | Real-time dashboard updates |

---

## Project Architecture

```text
                    Webcam
                       │
                       ▼
                    OpenCV
                       │
                       ▼
                 MediaPipe Pose
                       │
                       ▼
                Body Landmarks
                       │
                       ▼
              Exercise Detection
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
        Angle Analysis       Form Analysis
             │                   │
             ▼                   ▼
        Rep Counting        Form Feedback
             │                   │
             └─────────┬─────────┘
                       ▼
                  Flask Backend
                       │
                       ▼
                REST / Video Feed
                       │
                       ▼
              HTML + CSS + JavaScript
                       │
                       ▼
                Live Dashboard