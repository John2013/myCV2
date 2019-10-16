# my Computer Vision 2

detects and shows objects like cars and peoples on video

## installation

1. Install Python>=3.6 and pip
2. install virtual environment
    ```bash
    $ python3 -m venv venv
    ```
3. activate venv
4. install pip packages
   ```bash
   $ pip install -r requirements.txt
   ```

## how to run

1. Download yolo.h5 to project directory from [here](https://github.com/OlafenwaMoses/ImageAI/releases/tag/1.0/)
1. Put video file in project directory
2. Edit `video_detection.py` and set input and output video files in:
    ```python
    video_path = detector.detectObjectsFromVideo(
        input_file_path=os.path.join(execution_path, "piter2.mp4"),
        output_file_path=os.path.join(execution_path, "piter2_detected_1"),
        frames_per_second=29.97,
        log_progress=True
    )
    ```
3. Run
    ```bash
    $ python video_detection.py
    ```
