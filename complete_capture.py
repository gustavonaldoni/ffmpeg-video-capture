from capture.audio_capture import AudioCapture
from merge.fix_video_duration import FixVideoDuration
from merge.merge_audio_video import MergeAudioVideo
from multiprocessing import Process, Event
from capture.video_capture import VideoCapture


class CompleteCapture:
    def __init__(self) -> None:
        self.temp_audio_path = "C:/temp/audio.wav"
        self.temp_video_path = "C:/temp/video.mp4"
        self.temp_fixed_video_path = "C:/temp/video_fixed.mp4"

        self.audio_capture = AudioCapture(self.temp_audio_path)
        self.video_capture = VideoCapture(self.temp_video_path)
        self.fix_video_duration = FixVideoDuration(
            self.temp_audio_path, self.temp_video_path, self.temp_fixed_video_path
        )

        self.stop_event = Event()

    def capture_video_and_audio(self) -> None:
        audio_capture_process = self._create_and_start_audio_capture_process()
        video_capture_process = self._create_and_start_video_capture_process()

        try:
            while True:
                pass
        except KeyboardInterrupt:
            self._stop_capture()

        audio_capture_process.join()
        video_capture_process.join()

        # self.fix_video_duration.fix_video_duration()

    def _create_and_start_audio_capture_process(self) -> Process:
        audio_capture_process = Process(
            target=self.audio_capture.capture_audio,
            args=(self.stop_event,),
        )
        audio_capture_process.start()

        return audio_capture_process

    def _create_and_start_video_capture_process(self) -> Process:
        video_capture_process = Process(
            target=self.video_capture.capture_video,
            args=(self.stop_event,),
        )
        video_capture_process.start()

        return video_capture_process

    def _stop_capture(self) -> None:
        self.stop_event.set()


if __name__ == "__main__":
    cp = CompleteCapture()
    cp.capture_video_and_audio()
