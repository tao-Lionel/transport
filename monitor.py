from pytube import ChannelShorts
import sys
sys.path.append('./pytube')
# from pytube import Channel

channel = ChannelShorts(
    "https://www.youtube.com/channel/UCkQEYwVkQwA19O2D0n_clFg")

video_urls = []
video_urls = channel.video_urls
print(video_urls[0])

# videos = []
# videos = channel.videos
# print(videos[0].title)
# print(videos[0].length)
# new_videos = videos[0].streams.filter(res="720p")[0]
# filename = new_videos.default_filename
# new_videos.download(
#     output_path='./videos', filename=filename)
