# from pytube import Channel
from pytube import YouTube
from pytube import Playlist
    
AUDIO_SAVE_DIRECTORY = "./download"
YOUTUBE_PLAYPLIST_URL = "https://youtube...."


def download_audio(video_url):
    video = YouTube(video_url)
    audio = video.streams.filter(only_audio = True).first()

    try:
        audio.download(YOUTUBE_PLAYPLIST_URL)
    except:
        print("Failed to download audio")

    print("audio was downloaded successfully")


p = Playlist()


for url in p.video_urls:
    print(url)
    download_audio(url)
