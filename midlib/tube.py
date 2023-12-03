#!/usr/bin/python3
from pytube import YouTube
import os
from sys import argv 

def download_video(path, link):
    try:
        if not os.path.exists(path):
            os.makedirs(path)

        youtube_object = YouTube(link)
        video_stream = youtube_object.streams.get_highest_resolution()

        video_title = youtube_object.title
        file_name = f"{video_title}.mp4"
        file_path = os.path.join(path, file_name)

        video_stream.download(output_path=path, filename=file_name)

        print(f"Download completed successfully. Video saved at: {file_path}")
    except Exception as e:
        print(f"An error has occurred: {e}")

if __name__ == "__main__":
    if len(argv) < 3:
        print("usage : ./tube.py <PATH> <link> ")
    else:
        path = argv[1]
        video_url = argv[2]
        download_video(path, video_url)

