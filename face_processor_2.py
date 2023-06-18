from feat import Detector
import pandas as pd

detector = Detector(
    face_model="retinaface",
    landmark_model="mobilefacenet",
    au_model='xgb',
    emotion_model="resmasknet",
    facepose_model="img2pose",
)


def get_detection(image_path):
    detections =  detector.detect_image(image_path)
    return detections.to_json(orient='records')