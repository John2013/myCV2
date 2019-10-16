from imageai.Detection import VideoObjectDetection
import os

execution_path = os.getcwd()

detector = VideoObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(os.path.join(execution_path, "yolo.h5"))
detector.loadModel()

video_path = detector.detectObjectsFromVideo(
    input_file_path=os.path.join(execution_path, "piter2.mp4"),
    output_file_path=os.path.join(execution_path, "piter2_detected_1"),
    frames_per_second=29.97,
    log_progress=True
)
print(video_path)
