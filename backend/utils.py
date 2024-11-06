import logging
import re
from pathlib import Path
from urllib.parse import urlparse


class Utils:
    """Utility class for common operations like file cleanup and sanitization."""

    @staticmethod
    def ensure_dir_exists(directory: str) -> None:
        if not Path(directory).exists():
            Path(directory).mkdir()

    @staticmethod
    def remove_files_by_base(base_filename: str, upload_folder:str) -> None:
        """Removes any existing files with the same base name."""
        base_path = str(Path(upload_folder)/ base_filename)
        file_paths = [base_path + ".webm", base_path + "_isolated_audio.wav", base_path + "_processed_video.mp4"]
        for path in file_paths:
            if Path(path).exists():
                logging.info(f"Removing old file: {path}")
                Path(path).unlink()

    @staticmethod
    def sanitize_filename(filename: str) -> str:
        """Replace non-alphanumerics (except periods and underscores) with underscores."""
        return re.sub(r"[^a-zA-Z0-9._-]", "_", filename)

    @staticmethod
    def validate_url(url: str) -> bool:
        """Basic URL validation"""
        parsed_url = urlparse(url)
        return all([parsed_url.scheme, parsed_url.netloc])