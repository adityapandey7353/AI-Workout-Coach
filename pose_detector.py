import cv2
import mediapipe as mp


class PoseDetector:

    def __init__(self):

        self.mp_pose = mp.solutions.pose
        self.mp_draw = mp.solutions.drawing_utils

        self.pose = self.mp_pose.Pose(
            static_image_mode=False,
            model_complexity=1,
            smooth_landmarks=True,
            enable_segmentation=False,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )

    def find_pose(self, frame, draw=True):

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = self.pose.process(rgb)

        if results.pose_landmarks and draw:

            self.mp_draw.draw_landmarks(
                frame,
                results.pose_landmarks,
                self.mp_pose.POSE_CONNECTIONS
            )

        return results

    def get_landmarks(self, frame, results):

        landmarks = []

        if results.pose_landmarks:

            height, width, _ = frame.shape

            for landmark in results.pose_landmarks.landmark:

                x = int(landmark.x * width)
                y = int(landmark.y * height)

                landmarks.append(
                    (x, y, landmark.visibility)
                )

        return landmarks
    