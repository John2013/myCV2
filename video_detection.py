import cv2 as cv
from imageai.Detection import VideoObjectDetection
import os

execution_path = os.getcwd()

fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi', fourcc, 29.97, (1280, 720))


def forFrame(frame_number, output_array, output_count, detected_frame):
    frame = detected_frame
    frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    out.write(frame)


detector = VideoObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(os.path.join(execution_path, "yolo.h5"))
detector.loadModel()

video_path = detector.detectObjectsFromVideo(
    input_file_path=os.path.join(execution_path, "piter2.mp4"),
    save_detected_video=False,
    # output_file_path=os.path.join(execution_path, "piter2_detected_1"),
    frames_per_second=29.97,
    log_progress=True,
    per_frame_function=forFrame,
    return_detected_frame=True
)
out.release()
print(video_path)
