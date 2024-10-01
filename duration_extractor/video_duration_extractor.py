import ffmpeg


class VideoDurationExtractor:
    def extract_mp4_duration_in_seconds(self, mp4_path: str) -> int:
        probe = ffmpeg.probe(mp4_path)

        duration = float(probe["format"]["duration"])
        duration = int(duration)

        return duration