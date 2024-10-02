import subprocess


FFMPEG_OPTIONS = {
    "input": "-i",
    "map": "-map",
    "shortest": "-shortest",
    "overwrite": "-y",
}


class MergeAudioVideo:
    def __init__(self, audio_path: str, video_path: str, output_path: str) -> None:
        self.audio_path = audio_path
        self.video_path = video_path
        self.output_path = output_path

    def merge_audio_video(self) -> bool:
        pass

    def _create_merge_command(self) -> list[str]:
        video_path_with_double_quotes = self._add_double_quotes_to_path(self.video_path)
        audio_path_with_double_quotes = self._add_double_quotes_to_path(self.audio_path)
        output_path_with_double_quotes = self._add_double_quotes_to_path(
            self.output_path
        )

        command = [
            "ffmpeg",
            FFMPEG_OPTIONS["input"],
            video_path_with_double_quotes,
            FFMPEG_OPTIONS["input"],
            audio_path_with_double_quotes,
            "-c:v",
            "copy",
            "-c:a",
            "aac",
            "-b:a",
            "192k",
            FFMPEG_OPTIONS["map"],
            "0:v:0",
            FFMPEG_OPTIONS["map"],
            "1:a:0",
            FFMPEG_OPTIONS["shortest"],
            FFMPEG_OPTIONS["overwrite"],
            output_path_with_double_quotes,
        ]

        return command

    def _add_double_quotes_to_path(self, path: str) -> str:
        if not path.startswith('"'):
            path = '"' + path

        if not path.endswith('"'):
            path = path + '"'

        return path
