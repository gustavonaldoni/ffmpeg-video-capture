import pyaudio
import wave
from multiprocessing.synchronize import Event as EventClass


class AudioCapture:
    def __init__(self, audio_path: str) -> None:
        self.audio_path = audio_path

        self.block_size = 1024
        self.audio_format = pyaudio.paInt16
        self.channels = 2
        self.sample_rate = 44100

    def capture_audio(self, stop_event: EventClass) -> None:
        audio_capture_process = pyaudio.PyAudio()
        audio_stream = self.create_audio_stream(audio_capture_process)
        audio_frames = []

        try:
            while not stop_event.is_set():
                data = audio_stream.read(self.block_size)
                audio_frames.append(data)
        finally:
            audio_stream.stop_stream()
            audio_stream.close()
            audio_capture_process.terminate()

            self.save_audio_frames_to_wav(audio_frames, audio_capture_process)

    def create_audio_stream(
        self, audio_capture_process: pyaudio.PyAudio
    ) -> pyaudio.Stream:
        return audio_capture_process.open(
            format=self.audio_format,
            channels=self.channels,
            rate=self.sample_rate,
            frames_per_buffer=self.block_size,
            input=True,
        )

    def save_audio_frames_to_wav(
        self, audio_frames: list[bytes], audio_capture_process: pyaudio.PyAudio
    ) -> None:
        arquivoWAV = wave.open(self.audio_path, "wb")
        arquivoWAV.setnchannels(self.channels)
        arquivoWAV.setsampwidth(
            audio_capture_process.get_sample_size(self.audio_format)
        )
        arquivoWAV.setframerate(self.sample_rate)
        arquivoWAV.writeframes(b"".join(audio_frames))
        arquivoWAV.close()
