import time
import math

from utils.angle import calculate_angle


class BicepCurl:

    def __init__(self, arm="right"):

        self.arm = arm

        # -----------------------------
        # Rep tracking
        # -----------------------------

        self.reps = 0
        self.stage = "down"
        self.angle = 0

        # -----------------------------
        # Angle thresholds
        # -----------------------------

        self.UP_ANGLE = 65
        self.DOWN_ANGLE = 150

        # -----------------------------
        # Stability
        # -----------------------------

        self.up_frames = 0
        self.down_frames = 0
        self.required_frames = 3

        # -----------------------------
        # Rep timing
        # -----------------------------

        self.rep_start_time = None
        self.last_rep_time = 0
        self.rep_cooldown = 0.7

        # -----------------------------
        # Rep measurements
        # -----------------------------

        self.min_angle = 180
        self.max_angle = 0

        self.start_elbow = None
        self.max_elbow_movement = 0

        # -----------------------------
        # Form information
        # -----------------------------

        self.form_score = 100
        self.form_status = "Good"
        self.form_message = "Ready"

        self.range_score = 100
        self.stability_score = 100
        self.speed_score = 100

    # ==================================================
    # MAIN UPDATE
    # ==================================================

    def update(self, landmarks):

        if len(landmarks) < 25:
            return self.get_data()

        # ----------------------------------------------
        # Select arm
        # ----------------------------------------------

        if self.arm == "right":

            shoulder = landmarks[12]
            elbow = landmarks[14]
            wrist = landmarks[16]

        else:

            shoulder = landmarks[11]
            elbow = landmarks[13]
            wrist = landmarks[15]

        # ----------------------------------------------
        # Check visibility
        # ----------------------------------------------

        if (
            shoulder[2] < 0.5
            or elbow[2] < 0.5
            or wrist[2] < 0.5
        ):
            return self.get_data()

        # ----------------------------------------------
        # Calculate elbow angle
        # ----------------------------------------------

        self.angle = calculate_angle(
            shoulder[:2],
            elbow[:2],
            wrist[:2]
        )

        # Track angle range
        self.min_angle = min(
            self.min_angle,
            self.angle
        )

        self.max_angle = max(
            self.max_angle,
            self.angle
        )

        # ----------------------------------------------
        # Track elbow stability
        # ----------------------------------------------

        elbow_position = elbow[:2]

        if self.start_elbow is not None:

            movement = math.dist(
                self.start_elbow,
                elbow_position
            )

            self.max_elbow_movement = max(
                self.max_elbow_movement,
                movement
            )

        # ----------------------------------------------
        # Detect UP
        # ----------------------------------------------

        if self.angle < self.UP_ANGLE:

            self.up_frames += 1
            self.down_frames = 0

            if self.up_frames >= self.required_frames:

                if self.stage == "down":

                    self.stage = "up"

                    # Start measuring this rep
                    self.rep_start_time = time.time()

                    self.start_elbow = elbow_position

                    self.min_angle = self.angle
                    self.max_angle = self.angle

                    self.max_elbow_movement = 0

        # ----------------------------------------------
        # Detect DOWN
        # ----------------------------------------------

        elif self.angle > self.DOWN_ANGLE:

            self.down_frames += 1
            self.up_frames = 0

            if self.down_frames >= self.required_frames:

                if self.stage == "up":

                    current_time = time.time()

                    if (
                        current_time - self.last_rep_time
                        > self.rep_cooldown
                    ):

                        # Complete rep
                        self.reps += 1

                        self.last_rep_time = current_time

                        # Analyze the completed rep
                        self.analyze_form(
                            current_time
                        )

                self.stage = "down"

        # ----------------------------------------------
        # Middle position
        # ----------------------------------------------

        else:

            self.up_frames = 0
            self.down_frames = 0

        return self.get_data()

    # ==================================================
    # FORM ANALYSIS
    # ==================================================

    def analyze_form(self, current_time):

        # ----------------------------------------------
        # 1. Range of motion
        # ----------------------------------------------

        if (
            self.min_angle <= 55
            and self.max_angle >= 155
        ):

            self.range_score = 100

        elif (
            self.min_angle <= 70
            and self.max_angle >= 145
        ):

            self.range_score = 85

        elif (
            self.min_angle <= 85
            and self.max_angle >= 135
        ):

            self.range_score = 70

        else:

            self.range_score = 50

        # ----------------------------------------------
        # 2. Elbow stability
        # ----------------------------------------------

        # Smaller movement = better stability
        if self.max_elbow_movement <= 20:

            self.stability_score = 100

        elif self.max_elbow_movement <= 40:

            self.stability_score = 85

        elif self.max_elbow_movement <= 60:

            self.stability_score = 70

        else:

            self.stability_score = 50

        # ----------------------------------------------
        # 3. Movement speed
        # ----------------------------------------------

        speed_score = 100

        if self.rep_start_time is not None:

            duration = (
                current_time
                - self.rep_start_time
            )

            # Very fast rep
            if duration < 0.7:

                speed_score = 50

            elif duration < 1.0:

                speed_score = 70

            elif duration < 1.3:

                speed_score = 85

            else:

                speed_score = 100

        self.speed_score = speed_score

        # ----------------------------------------------
        # Final score
        # ----------------------------------------------

        self.form_score = round(
            (
                self.range_score
                + self.stability_score
                + self.speed_score
            ) / 3
        )

        # ----------------------------------------------
        # Feedback message
        # ----------------------------------------------

        if self.form_score >= 90:

            self.form_status = "Excellent"

            self.form_message = (
                "Great form. Keep it controlled."
            )

        elif self.form_score >= 75:

            self.form_status = "Good"

            if self.range_score < 75:

                self.form_message = (
                    "Try using a larger range of motion."
                )

            elif self.stability_score < 75:

                self.form_message = (
                    "Try keeping your elbow more stable."
                )

            elif self.speed_score < 75:

                self.form_message = (
                    "Slow down your movement."
                )

            else:

                self.form_message = (
                    "Good rep. Keep your form consistent."
                )

        else:

            self.form_status = "Needs Improvement"

            if self.range_score < 75:

                self.form_message = (
                    "Complete the curl through a fuller range."
                )

            elif self.stability_score < 75:

                self.form_message = (
                    "Keep your elbow closer to your body."
                )

            elif self.speed_score < 75:

                self.form_message = (
                    "Your movement is too fast."
                )

            else:

                self.form_message = (
                    "Focus on controlled movement."
                )
    def set_arm(self, arm):

        if arm not in ["left", "right"]:
            return

        self.arm = arm

        # Reset current movement state
        self.stage = "down"
        self.up_frames = 0
        self.down_frames = 0

        # Reset angle tracking
        self.angle = 0
        self.min_angle = 180
        self.max_angle = 0

        # Reset elbow tracking
        self.start_elbow = None
        self.max_elbow_movement = 0

        # Reset timing
        self.rep_start_time = None
        self.last_rep_time = 0
        # ==================================================
        # RETURN DATA
        # ==================================================

    def get_data(self):

        return {
            "reps": self.reps,
            "angle": round(self.angle),
            "stage": self.stage,
            "form_score": self.form_score,
            "form_status": self.form_status,
            "form_message": self.form_message
        }