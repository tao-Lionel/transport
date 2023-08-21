import sys
sys.path.append('./pytube')
# from pytube import Channel
from pytube import ChannelShorts

channel = ChannelShorts("https://www.youtube.com/channel/UCkQEYwVkQwA19O2D0n_clFg")

video_urls = []
video_urls = channel.video_urls
print(video_urls[0])

videos = []
videos = channel.videos
print(videos[0].title)
print(videos[0].length)
# print(videos[0].streams.filter(res="720p"))
default_filename  = videos[0].streams.filter(res="720p")[0].default_filename
print(default_filename)
# videos[0].streams.filter(res="720p")[0].download(output_path='./videos',filename="latest.mp4")

