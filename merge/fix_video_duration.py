from duration_extractor.audio_duration_extractor import AudioDurationExtractor
from duration_extractor.video_duration_extractor import VideoDurationExtractor


import subprocess


class FixVideoDuration:
    def __init__(self, audio_path: str, video_path: str, output_path: str) -> None:
        self.audio_path = audio_path
        self.video_path = video_path
        self.output_path = output_path

        self.audio_duration_extractor = AudioDurationExtractor()
        self.video_duration_extractor = VideoDurationExtractor()

    def fix_video_duration(self) -> None:
        fix_video_duration_command = self._create_fix_video_duration_command()
        print(fix_video_duration_command)

        subprocess.run(fix_video_duration_command)

    def _create_fix_video_duration_command(self) -> list[str]:
        audio_duration = self.audio_duration_extractor.extract_wav_duration_in_seconds(self.audio_path)
        video_duration = self.video_duration_extractor.extract_mp4_duration_in_seconds(self.video_path)

        video_path_with_double_quotes = self._add_double_quotes_to_path(self.video_path)
        output_path_with_duble_quotes = self._add_double_quotes_to_path(self.output_path)

        command = [
            "ffmpeg",
            "-i",
            video_path_with_double_quotes,
            "-vf",
            f'"setpts=({audio_duration}/{video_duration})*PTS"',
            "-c:a", "copy",
            output_path_with_duble_quotes,
        ]

        return command
    
    def _add_double_quotes_to_path(self, path: str) -> str:
        if not path.startswith('"'):
            path = '"' + path

        if not path.endswith('"'):
            path = path + '"'

        return path
