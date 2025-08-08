import cv2

# 日本語コメント: とりあえず最終映像(URLのMJPEG)をOpenCVで表示するだけ
def show_mjpeg(url: str, window_name: str = "CRIMELIVE Final"):
    cap = cv2.VideoCapture(url)
    if not cap.isOpened():
        print("ストリームを開けません:", url)
        return
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    while True:
        ok, frame = cap.read()
        if not ok:
            print("フレーム取得に失敗:", url)
            break
        cv2.imshow(window_name, frame)
        if (cv2.waitKey(1) & 0xFF) in (27, ord('q')):
            break
    cap.release()
    cv2.destroyAllWindows()
