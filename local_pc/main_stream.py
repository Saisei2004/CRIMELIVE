# ローカルPCで配信サーバを起動するスクリプト
# 映像: /video (MJPEG), 音声: /audio (16bit PCM)
from app.av_streamer import AVStreamer

if __name__ == "__main__":
    server = AVStreamer()
    try:
        server.run()
    except KeyboardInterrupt:
        server.stop()
