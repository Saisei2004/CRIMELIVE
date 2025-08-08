import queue
import sounddevice as sd
from .config import Config

class AudioManager:
    """sounddeviceでマイクから16bit PCMを取り出す簡易クラス"""
    def __init__(self):
        self.q = queue.Queue()
        self.stream = sd.InputStream(
            samplerate=Config.AUDIO_SAMPLE_RATE,
            channels=Config.AUDIO_CHANNELS,
            dtype="int16",
            blocksize=Config.AUDIO_BLOCK_SIZE,
            callback=self._callback
        )

    def _callback(self, indata, frames, time, status):  # 日本語コメント: マイク入力の都度呼ばれる
        if status:
            pass
        self.q.put(indata.tobytes())

    def start(self):
        self.stream.start()

    def stop(self):
        self.stream.stop()
        self.stream.close()

    def read_chunk(self) -> bytes:
        """ブロッキングで1チャンク取り出す"""
        return self.q.get()
