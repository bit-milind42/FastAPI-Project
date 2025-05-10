import cv2
import os
from pathlib import Path
import uuid

def extract_frames(video_path, output_dir, interval=1):
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = 0
    saved_frames = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if int(cap.get(cv2.CAP_PROP_POS_FRAMES)) % int(fps * interval) == 0:
            filename = f"{uuid.uuid4().hex}.jpg"
            filepath = os.path.join(output_dir, filename)
            cv2.imwrite(filepath, frame)
            saved_frames.append(filepath)
        frame_count += 1
    cap.release()
    return saved_frames
