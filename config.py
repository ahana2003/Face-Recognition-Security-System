from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
DATASET_DIR = BASE_DIR / 'dataset'
MODELS_DIR = BASE_DIR / 'models'
DATA_DIR = BASE_DIR / 'data'
ATTENDANCE_DIR = BASE_DIR / 'attendance'
UNKNOWN_DIR = BASE_DIR / 'unknown_faces'
DB_FILE = DATA_DIR / 'attendance.db'
CSV_FILE = ATTENDANCE_DIR / 'attendance.csv'
DETECTOR_MODEL = MODELS_DIR / 'face_detection_yunet_2023mar.onnx'
RECOGNIZER_MODEL = MODELS_DIR / 'face_recognition_sface_2021dec.onnx'
CAMERA_INDEX = 0
MATCH_THRESHOLD = 0.25
UNKNOWN_SAVE_COOLDOWN_SECONDS = 10
