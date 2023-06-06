import cv2
from typing import Collection, Any
from pathlib import Path
from threading import Thread


def extract_frames_from_video(source: str|Path, frame_ids: Collection, savedir: str):
    if isinstance(source, Path):
        source = Path(source)
    cap = cv2.VideoCapture(source)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    save_threads = []
    for frame_id in frame_ids:
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_id)
        ret, frame = cap.read()
        if ret and len(save_threads) < 32:
            filename = f"{}_frame_id_{frame_id}.jpg"
            save_threads.append(Thread(target=save_frame, args=(savedir, filename))).start()


def save_frame(directory: str, filename: str, image: Any):
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(str(directory / filename), image)
    cv2.imwrite(file_path, image)



if __name__ == '__main__':
    
    save_frame()