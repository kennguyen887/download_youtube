from pytube import Channel
import os
from pytube import YouTube
from pytube import Playlist

from datetime import datetime


    
AUDIO_SAVE_DIRECTORY = "./download"
YOUTUBE_PLAYPLIST_URL = "https://www.youtube.com/watch?v=NsMWTiwG97A&list=PLv9w1I38lMN5TK3RA_fKrPH91q4yQ1wbc"


def download_audio(video_url):
    video = YouTube(video_url)
    audio = video.streams.filter(only_audio = True).first()

    try:
        audio.download(AUDIO_SAVE_DIRECTORY)
    except:
        print("Failed to download audio")

    print("audio was downloaded successfully")


p = Playlist(YOUTUBE_PLAYPLIST_URL)


def is_file_exists(folder_path, filename):
    file_path = os.path.join(folder_path, filename)
    return os.path.exists(file_path)



for url in p.video_urls:
    video = YouTube(url)
    if not is_file_exists(AUDIO_SAVE_DIRECTORY, f"{video.title.replace(".", "")}.mp4"):
        print(f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} | Downloading video: {video.title}")
        download_audio(url)
        
