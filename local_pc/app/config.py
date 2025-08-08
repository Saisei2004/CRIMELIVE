class Config:
    # --- 映像 ---
    CAMERA_INDEX = 0
    FRAME_WIDTH = 1280
    FRAME_HEIGHT = 720
    FRAME_FPS = 30
    JPEG_QUALITY = 80
    # --- 音声 ---
    AUDIO_SAMPLE_RATE = 48000
    AUDIO_CHANNELS = 2
    AUDIO_BLOCK_SIZE = 1024
    # --- HTTPサーバ ---
    HOST = "127.0.0.1"
    PORT = 5001
    VIDEO_ROUTE = "/video"
    AUDIO_ROUTE = "/audio"
