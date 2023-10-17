# youtube 视频下载
# transport

查看网页源代码搜索 externalId，拿到externalId 的值

url: <https://www.youtube.com/channel/${externalId}>

# 获取封面图

ffmpeg -i ./videos/v1080p+audio.mp4 -vf "select=eq(pict_type\,I)" -vframes 1  -vsync vfr -qscale:v 2 -f image2 v1080p_audio_output.jpeg -y

# 合并视频+音频

ffmpeg -y -i v1080p.webm -i audio.mp4 -shortest v1080p+audio.mp4
