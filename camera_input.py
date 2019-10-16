import cv2 as cv
from imageai.Detection import VideoObjectDetection
import os

execution_path = os.getcwd()
camera = cv.VideoCapture(0)


detector = VideoObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(os.path.join(execution_path, "yolo.h5"))
detector.loadModel()

detector.detectObjectsFromVideo(
    camera_input=camera,
    output_file_path=os.path.join(execution_path, "camera_detected_video"),
    frames_per_second=1,
    log_progress=True,
    detection_timeout=3
)
print("done")
