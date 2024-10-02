import wave


class AudioDurationExtractor:
    def extract_wav_duration_in_seconds(self, wav_path: str) -> int:
        with wave.open(wav_path, "rb") as wav_file:
            frames = wav_file.getnframes()
            rate = wav_file.getframerate()

            duration = frames / float(rate)
            duration = int(duration)

            return duration