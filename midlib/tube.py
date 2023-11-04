from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)
print("title : ",yt.title)
print("views : ", yt.views)