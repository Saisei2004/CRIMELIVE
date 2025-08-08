# 12から戻ってきた最終映像(MJPEG)を表示（音声は将来拡張）
# 例: url = "http://127.0.0.1:6000/stream" 等、トンネル経由URLを指定
from app.av_receiver import show_mjpeg

if __name__ == "__main__":
    url = "http://127.0.0.1:6000/stream"  # 必要に応じて変更
    show_mjpeg(url)
