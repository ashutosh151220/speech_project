from pytube import Playlist
import time
import random
# URL of the YouTube playlist
playlist_url = r"https://www.youtube.com/watch?v=k0CthZZQXpE&list=PLd9tDukllEeqfbq1dKXwXboq4yrr0LJhz"

# Create a Playlist object
sl=random.randint(40,60)
playlist = Playlist(playlist_url)

# Download the audio streams of the videos in the playlist
for video in playlist.videos:
    audio_stream = video.streams.filter(only_audio=True).first()
    if audio_stream:
        print(f"Downloading audio from: {video.title}...")
        audio_stream.download(output_path='sahil_khana/')
        time.sleep(sl)
    else:
        print(f"No audio stream available for: {video.title}")
        
    
