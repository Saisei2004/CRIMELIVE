import cv2
from .config import Config

class CameraManager:
    """OpenCVでUSBカメラからフレーム取得し、JPEGにエンコードして返すクラス"""
    def __init__(self):
        self.cap = cv2.VideoCapture(Config.CAMERA_INDEX, cv2.CAP_V4L2)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, Config.FRAME_WIDTH)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, Config.FRAME_HEIGHT)
        self.cap.set(cv2.CAP_PROP_FPS, Config.FRAME_FPS)
        if not self.cap.isOpened():
            raise RuntimeError("カメラをオープンできませんでした。/dev/video* と占有状況を確認してください。")

    def get_frame_jpeg(self) -> bytes | None:
        ok, frame = self.cap.read()
        if not ok:
            return None
        ok, buf = cv2.imencode(".jpg", frame, [int(cv2.IMWRITE_JPEG_QUALITY), Config.JPEG_QUALITY])
        return buf.tobytes() if ok else None

    def release(self):
        self.cap.release()
