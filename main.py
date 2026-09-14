from flask import Flask, render_template, Response, jsonify, request
import cv2

from pose_detector import PoseDetector
from exercises.bicep_curl import BicepCurl


app = Flask(__name__)


# ==================================================
# CAMERA
# ==================================================

camera = cv2.VideoCapture(0)


# ==================================================
# COMPUTER VISION
# ==================================================

detector = PoseDetector()

exercise = BicepCurl(
    arm="right"
)


# ==================================================
# LIVE DATA
# ==================================================

current_data = {
    "reps": 0,
    "angle": 0,
    "stage": "down",
    "form_score": 100,
    "form_status": "Good",
    "form_message": "Ready"
}


# ==================================================
# CAMERA FRAME GENERATOR
# ==================================================

def generate_frames():

    while True:

        success, frame = camera.read()

        if not success:

            print("Could not access camera.")

            break

        # Mirror camera
        frame = cv2.flip(
            frame,
            1
        )

        # Pose detection
        results = detector.find_pose(
            frame,
            draw=True
        )

        # Get landmarks
        landmarks = detector.get_landmarks(
            frame,
            results
        )

        # ------------------------------------------
        # Exercise processing
        # ------------------------------------------

        if landmarks:

            data = exercise.update(
                landmarks
            )

            # Update live data
            current_data.update(
                data
            )

            # --------------------------------------
            # Draw CV information
            # --------------------------------------

            cv2.putText(
                frame,
                f"Reps: {data['reps']}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

            cv2.putText(
                frame,
                f"Angle: {data['angle']}",
                (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 255, 255),
                2
            )

            cv2.putText(
                frame,
                f"Stage: {data['stage']}",
                (20, 120),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 255, 255),
                2
            )

            cv2.putText(
                frame,
                f"Form: {data['form_score']}%",
                (20, 160),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2
            )

        # ------------------------------------------
        # Encode frame
        # ------------------------------------------

        success, buffer = cv2.imencode(
            ".jpg",
            frame
        )

        if not success:

            continue

        frame_bytes = buffer.tobytes()

        # ------------------------------------------
        # Send frame to browser
        # ------------------------------------------

        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n"
            + frame_bytes
            + b"\r\n"
        )


# ==================================================
# HOME PAGE
# ==================================================

@app.route("/")
def home():

    return render_template(
        "index.html"
    )


# ==================================================
# VIDEO STREAM
# ==================================================

@app.route("/video_feed")
def video_feed():

    return Response(
        generate_frames(),
        mimetype=(
            "multipart/x-mixed-replace; "
            "boundary=frame"
        )
    )


# ==================================================
# WORKOUT STATS API
# ==================================================

@app.route("/stats")
def stats():

    return jsonify(
        current_data
    )

@app.route("/select_arm", methods=["POST"])
def select_arm():

    data = request.get_json()

    arm = data.get("arm")

    if arm not in ["left", "right"]:

        return jsonify({
            "success": False,
            "message": "Invalid arm"
        }), 400

    exercise.set_arm(arm)

    return jsonify({
        "success": True,
        "arm": arm
    })
# ==================================================
# START SERVER
# ==================================================
if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False,
        threaded=True
    )

    camera.release()
    cv2.destroyAllWindows()