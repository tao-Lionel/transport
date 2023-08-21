from pytube import YouTube

def download_complete_handler(stream, file_path):
    print ("File: " + stream.title + "downloaded completed in " + file_path)


video = YouTube("https://www.youtube.com/shorts/TaI5u9pwuKs",
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

stream_audio = video.streams.filter(type="audio", abr="128kbps")[0]
print(stream_audio)
stream_audio.download(filename='audio.mp4')
