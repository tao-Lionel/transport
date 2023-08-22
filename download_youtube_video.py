from pytube import YouTube
import os


def download_complete_handler(stream, file_path):
    print("File: " + stream.title + "downloaded completed in " + file_path)


video = YouTube("https://www.youtube.com/watch?v=mRa0Gi_mRjs&t=6s",
                on_complete_callback=download_complete_handler)

print("Video_title = " + video.title)
print("Video_author = " + video.author)
print("Video_length = " + str(video.length))

current_res = 0
stream_highest_res = video.streams[0]
for everystream in video.streams.filter(type="video"):
    if int(everystream.resolution[:-1]) > 1080:
        continue
    if int(everystream.resolution[:-1]) > current_res:
        current_res = int(everystream.resolution[:-1])
        stream_highest_res = everystream
print("Highest stream: ", stream_highest_res)

stream_highest_res.download(filename='v1080p.webm')

# 下载音频
stream_audio = video.streams.filter(type="audio", abr="128kbps")[0]
print(stream_audio)
stream_audio.download(filename='audio.mp4')

# 合并视频+音频
os.system("ffmpeg -y -i v1080p.webm -i audio.mp4 -shortest v1080p+audio.mp4")
