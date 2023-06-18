from feat import Detector


class FaceProcessor:
    def __init__(self):
        self.face_model = "retinaface"
        self.landmark_model = "mobilenet"
        self.au_model = "svm"
        self.emotion_model = "resmasknet"
        self.detector = Detector(face_model = self.face_model, landmark_model = self.landmark_model, au_model = self.au_model, emotion_model = self.emotion_model)
    
    def detect_aus(self, image):
        """Takes a PIL (pillow) image as input and returns action units"""
        image_prediction = self.detector.detect_image(image)
        print(image_prediction)