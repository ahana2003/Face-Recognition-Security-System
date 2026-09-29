# Smart Face Attendance System

A local OpenCV face-recognition attendance project inspired by the workflow shown in the referenced smart-attendance tutorial, implemented independently.

## Features
- Webcam face detection and recognition
- Deep-learning YuNet + SFace models from OpenCV Zoo
- Authorized/unknown display
- Automatic attendance
- One attendance entry per person per day
- SQLite database + CSV export
- Unknown-person snapshots
- Dataset registration helper
- Tkinter attendance dashboard

## Setup in VS Code

### 1. Install packages
```bash
python -m pip install -r requirements.txt
```

### 2. Download the two models
```bash
python download_models.py
```

The models must be:
```text
models/face_detection_yunet_2023mar.onnx
models/face_recognition_sface_2021dec.onnx
```

Official OpenCV Zoo:
- https://github.com/opencv/opencv_zoo/tree/main/models/face_detection_yunet
- https://github.com/opencv/opencv_zoo/tree/main/models/face_recognition_sface

### 3. Run the camera
```bash
python main.py
```
Press Q to stop.

### 4. Run the dashboard
```bash
python dashboard.py
```

### 5. Add another person
```bash
python register.py "NewPerson"
```
Press SPACE five times to capture reference photos.

## Initial dataset
Your five supplied images are included as Person_1 through Person_5. Rename those folders to the display names you want. For better accuracy, use 3–5 clear reference photos per person.

## Files created at runtime
- `data/attendance.db` — SQLite database
- `attendance/attendance.csv` — attendance export
- `unknown_faces/` — snapshots of unknown detections

## Important
This is a project/demo system. Face recognition can produce false matches or false rejections and should not be the sole mechanism for high-stakes access control.
