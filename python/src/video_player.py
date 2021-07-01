"""A video player class."""
import operator
import random
import re
from .video_library import VideoLibrary

global Playing
Playing = ""
global Pause
Pause = 1
class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print("Here's a list of all available videos:")
        l = self._video_library.get_all_videos()
        new_list = sorted(l, key=operator.attrgetter("title"))

        for x in range(len(new_list)):
            print(new_list[x].title, f"({new_list[x].video_id})", f"[{' '.join(new_list[x].tags)}]")

    def play_video(self, video_id):
        l = self._video_library.get_all_videos()
        val = 0
        global Playing
        global Pause
        for x in range(len(l)):
            if video_id == l[x].video_id:
                if Playing != "":
                    print("Stopping video:", Playing)
                    Playing = str(l[x].title)
                    print("Playing video:", Playing)
                    Pause = 1
                else:
                    Playing = str(l[x].title)
                    print("Playing video:", Playing)
                    Pause = 1
        for x in range(len(l)):
            if video_id != l[x].video_id:
                val = val + 1
                if val == len(self._video_library.get_all_videos()):
                    print("Cannot play video: Video does not exist")

    def stop_video(self):
        global Playing
        global Pause
        if Playing != "":
            print("Stopping video:", Playing)
            Playing = ""
            Pause = 1
        else:

            print("Cannot stop video: No video is currently playing")

    def play_random_video(self):
        global Playing
        global Pause
        l = self._video_library.get_all_videos()
        n = len(l)
        m = 0
        if Playing != "":
            print("Stopping video:", Playing)
            Playing = l[random.randint(m, n-1)].title
            print("Playing video:", Playing)
            Pause = 1
        else:
            Playing = l[random.randint(m, n-1)].title
            print("Playing video:", Playing)
            Pause = 1
    def pause_video(self):
        global Playing
        global Pause
        if Playing != "":
            if Pause == 1:
                print("Pausing video:", Playing)
                Pause = 0
            else:
                print("Video is already paused:", Playing)
        else:
            print("Cannot pause video: No video is currently playing")
            Pause = 1
    def continue_video(self):
        global Playing
        global Pause
        if Playing != "":
            if Pause == 1:
                print("Cannot continue video: Video is not paused")
            else:
                print("Continuing video:", Playing)
                Pause = 1
        else:
            print("Cannot continue video: No video is currently playing")


    def show_playing(self):
        global Playing
        global Pause
        status = ""
        id = ""
        tags = []
        l = self._video_library.get_all_videos()
        if Playing == "":
            print('No video is currently playing')
        else:
            for x in range(len(l)):

                if Playing == l[x].title:
                    id = (l[x].video_id)
                    tags = l[x].tags
            if Pause == 0:
                status = "- PAUSED"
            print("Currently playing:", Playing, f"({id})", f"[{' '.join(tags)}]", status)

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        l = self._video_library.get_all_videos()
        l1 = []

        for x in range(len(l)):
            tytul = l[x].title
            tytul = tytul.lower()

            search = re.search(search_term, tytul)
            if search != None:
                l1.append(l[x])
        if len(l1) == 0:
            print("No search results for", search_term)
        else:
            print("Here are the results for", f"{search_term}:")
            limit = []
            for i in range(len(l1)):
                limit.append(str(i+1))
                print(f"    {i+1})", l1[i].title, f"({l1[i].video_id})",  f"[{' '.join(l1[i].tags)}]")
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")

            val = input()
            try:
                int(val)
                it_is = True
            except ValueError:
                it_is = False
            if it_is:
                val = int(val) - 1
                if val in range(len(l1)):
                    VideoPlayer.play_video(self, l1[val].video_id)
                else:
                    pass
            else:
                pass

    def search_videos_tag(self, search_term):
        l = self._video_library.get_all_videos()
        l1 = []

        for x in range(len(l)):
            tytul = l[x].tags
            tytul = list(tytul)

            if any(search_term in s for s in tytul):
                l1.append(l[x])
        if len(l1) == 0:
            print("No search results for", search_term)
        else:
            print("Here are the results for", f"{search_term}:")
            limit = []
            for i in range(len(l1)):
                limit.append(str(i+1))
                print(f"    {i+1})", l1[i].title, f"({l1[i].video_id})",  f"[{' '.join(l1[i].tags)}]")
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")

            val = input()
            try:
                int(val)
                it_is = True
            except ValueError:
                it_is = False
            if it_is:
                val = int(val) - 1
                if val in range(len(l1)):
                    VideoPlayer.play_video(self, l1[val].video_id)
                else:
                    pass
            else:
                pass

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
