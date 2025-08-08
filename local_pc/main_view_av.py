# ブラウザ不要のA/Vビューア
# - 映像: OpenCVでMJPEGを表示
# - 音声: ffplayで16bit PCMを再生
import subprocess
import sys
import time
import cv2

# 日本語コメント: 必要に応じてURLを変更（往復トンネルなら6000）
VIDEO_URL = "http://127.0.0.1:7000/video"
AUDIO_URL = "http://127.0.0.1:7000/audio"

def start_audio():
    # 日本語コメント: ffplayでPCM(16kHz/Mono/16bit)を再生
    # -nodisp: 画面を出さない, -autoexit: 終了時自動で閉じる, -loglevel error: ログ抑制
    cmd = [
        "ffplay", "-f", "s16le", "-ar", "16000", "-ac", "1",
        "-nodisp", "-autoexit", "-loglevel", "error",
        AUDIO_URL
    ]
    return subprocess.Popen(cmd)

def main():
    # 音声再生開始
    audio_proc = start_audio()
    # 映像再生開始
    cap = cv2.VideoCapture(VIDEO_URL)
    if not cap.isOpened():
        print("映像ストリームを開けません:", VIDEO_URL)
        audio_proc.terminate()
        sys.exit(1)

    win = "CRIMELIVE Viewer (q/ESCで終了)"
    cv2.namedWindow(win, cv2.WINDOW_NORMAL)

    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                print("フレーム取得に失敗:", VIDEO_URL)
                break
            cv2.imshow(win, frame)
            key = cv2.waitKey(1) & 0xFF
            if key in (27, ord('q')):  # ESC or q
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()
        # 日本語コメント: 音声プロセスを安全に終了
        if audio_proc.poll() is None:
            audio_proc.terminate()
            # 少し待って終了しなければkill
            for _ in range(10):
                if audio_proc.poll() is not None:
                    break
                time.sleep(0.05)
            if audio_proc.poll() is None:
                audio_proc.kill()

if __name__ == "__main__":
    main()
