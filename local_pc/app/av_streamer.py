from flask import Flask, Response
from .config import Config
from .camera_manager import CameraManager
from .audio_manager import AudioManager
from .utils_io import make_mjpeg_chunk

class AVStreamer:
    """Flaskで /video(MJPEG) と /audio(PCM) を提供するサーバ"""
    def __init__(self):
        self.app = Flask(__name__)
        self.cam = CameraManager()
        self.audio = AudioManager()
        self._register_routes()

    def _register_routes(self):
        @self.app.route(Config.VIDEO_ROUTE)
        def video():
            return Response(self._gen_video(),
                            mimetype="multipart/x-mixed-replace; boundary=frame")

        @self.app.route(Config.AUDIO_ROUTE)
        def audio():
            headers = {
                "Content-Type": "audio/L16",
                "X-Sample-Rate": str(Config.AUDIO_SAMPLE_RATE),
                "X-Channels": str(Config.AUDIO_CHANNELS),
            }
            return Response(self._gen_audio(), headers=headers)

    def _gen_video(self):
        while True:
            jpeg = self.cam.get_frame_jpeg()
            if jpeg is None:
                continue
            yield make_mjpeg_chunk(jpeg)

    def _gen_audio(self):
        self.audio.start()
        try:
            while True:
                chunk = self.audio.read_chunk()
                if not chunk:
                    continue
                yield chunk
        finally:
            self.audio.stop()

    def run(self):
        self.app.run(host=Config.HOST, port=Config.PORT, threaded=True)

    def stop(self):
        self.cam.release()
