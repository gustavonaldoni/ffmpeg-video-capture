import ffmpeg
import threading


class VideoCapture:
    def __init__(self, video_path: str, fps: int = 30) -> None:
        self.video_path = video_path
        self.fps = fps

    def capture_video(self, stop_event: threading.Event) -> bool:
        process = (
            ffmpeg.input("desktop", format="gdigrab", framerate=self.fps)
            .output(self.video_path, pix_fmt="yuv420p", vcodec="libx264")
            .run_async(pipe_stdin=True, overwrite_output=True)
        )

        try:
            while not stop_event.is_set():
                pass
        finally:
            process.stdin.write(b'q')
            process.stdin.close()
            process.wait()
