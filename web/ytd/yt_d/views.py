import os
from django.shortcuts import render
from pathlib import Path
from pytube import Playlist, YouTube
from django.contrib import messages
import requests

# Create your views here.
def index(request):
    path_to_save = str(os.path.join(Path.home(), "Downloads"))
    try:
        link = request.POST["link"]
        check_link = requests.get(link)
        if(check_link.status_code == 200):
            print("ok")
            if("https://www.youtube.com/playlist?" in link):
                yt_playlist = Playlist(link)
                print("\nStart downloading...\n")
                for index, yt_link in enumerate(yt_playlist.video_urls):
                    yt_obj = YouTube(yt_link)
                    print("%s - %s" % (index+1, yt_obj.title))
                    messages.success(request, "%s - %s" % (index+1, yt_obj.title))
                    yt_obj.streams.get_audio_only("mp4").download(path_to_save)
                    print('Song is READY\n')
                    messages.success(request, "Song is READY")
            else:
                yt = YouTube(link)
                print("\nStart downloading...\n")
                print(yt.title)
                messages.success(request, yt.title)
                yt.streams.get_audio_only("mp4").download(path_to_save)
                print("\nThe song is READY")
                messages.success(request, "Song is READY")
        else:
            print("no")
    except Exception as e:
        print(e)
    return render(request, "yt_d/index.html")

# if not work from first or second time just run while start to work

#______________YouTube-One-song__________________________________
# from pytube import Playlist, YouTube

# path_to_save = "/home/nikolai/Desktop/Python/YouTube-downloader/playlist"

# link = input("Enter YouTube song link: ")

# yt = YouTube(link)
# print("\nStart downloading...\n")
# print(yt.title)
# yt.streams.get_audio_only("mp4").download(path_to_save)

# print("\nThe song is READY")
#_____________________________________________________________

#______________YouTube-Playlist_________________________________
# from pytube import Playlist, YouTube

# path_to_save = "/home/nikolai/Desktop/Python/YouTube-downloader/playlist"

# link = input("Enter YouTube playlist link: ")

# yt_playlist = Playlist(link)
# print("\nStart downloading...\n")
# for index, yt_link in enumerate(yt_playlist.video_urls):
#     yt_obj = YouTube(yt_link)
#     print("%s - %s" % (index+1, yt_obj.title))
#     yt_obj.streams.get_audio_only("mp4").download(path_to_save)
#     print('Song is READY\n')

# print("\nAll songs are READY\n")
#_____________________________________________________________

# import pafy # not work
# link = input("Enter YouTube Playlist link: ")
# yt_playlist = pafy.get_playlist(link)
# print(yt_playlist["title"])
# # for yt_link in yt_playlist:
# #     pafy.new(yt_link).getbestaudio().download()
# print("\nAll songs are READY")