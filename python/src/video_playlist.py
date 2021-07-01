"""A video playlist class."""
from .video import Video
from pathlib import Path
import csv


def _csv_reader_with_strip(reader):
    yield from ((item.strip() for item in line) for line in reader)


class Playlist:
    """A class used to represent a Playlist"""
    def __init__(self, title):
        self.title = title
        self.list = []

    def load(self, video_id):
        self.list.append(video_id)

    def get_playlist(self, title):
        return

