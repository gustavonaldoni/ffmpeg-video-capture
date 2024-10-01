from capture.audio_capture import AudioCapture
from merge.merge_audio_video import MergeAudioVideo
from capture.video_capture import VideoCapture


import threading


class CompleteCapture:
    def __init__(self) -> None:
        self.temp_audio_path = "C:/temp/audio.wav"
        self.temp_video_path = "C:/temp/video.mp4"
        
        self.audio_capture = AudioCapture(self.temp_audio_path)
        self.video_capture = VideoCapture(self.temp_video_path)
        
        self.stop_event = threading.Event()
        
    def capture_video_with_audio(self) -> None:
        audio_capture_thread = self._create_and_start_audio_capture_thread()
        video_capture_thread = self._create_and_start_video_capture_thread()

        try:
            while True:
                pass
        except KeyboardInterrupt:
            self._stop_capture()
            
        audio_capture_thread.join()
        video_capture_thread.join()

    def _create_and_start_audio_capture_thread(self) -> threading.Thread:
        audio_capture_thread = threading.Thread(
            target=self.audio_capture.capture_audio,
            args=(self.stop_event,),
        )
        audio_capture_thread.start()

        return audio_capture_thread

    def _create_and_start_video_capture_thread(self) -> threading.Thread:
        video_capture_thread = threading.Thread(
            target=self.video_capture.capture_video,
            args=(self.stop_event,),
        )
        video_capture_thread.start()

        return video_capture_thread
    
    def _stop_capture(self) -> None:
        self.stop_event.set()

if __name__ == "__main__":
    cp = CompleteCapture()
    cp.capture_video_with_audio()