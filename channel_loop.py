import os
import translators as ts
import time
import json
from pytube import ChannelShorts
import sys
sys.path.append('./pytube')
# from pytube import Channel


uploadsJsonPath = "./json/uploads.json"
supported_target_platform = ['KS']


with open(uploadsJsonPath, "r") as json_file:
    uploads = json_file.read()
    json_file.close()

upload_log = json.loads(uploads)


# 获取 ChannelShorts
def getChannelShorts(url):
    return ChannelShorts(url)


# 获取视频信息
def getVideoInfo(url):
    c = getChannelShorts(url)
    new_video_url = c.video_urls[0]
    new_video_id = new_video_url[-11:]
    new_video_name = c.videos[0].title
    publish_date = c.videos[0].publish_date
    return {
        'url': new_video_url,
        'id': new_video_id,
        'name': new_video_name,
        'publishDate': publish_date,
        'videos': c.videos[0]
    }


# 写入文件
def writeUploadsJson():
    with open(uploadsJsonPath, "w") as json_file:
        uploads = json.dumps(upload_log)
        json_file.write(uploads)
        json_file.close()


# 下载视频
def downloadVideo(video):
    new_videos = video.streams.filter(res="720p")[0]
    filename = new_videos.default_filename
    # 翻译标题
    title_cn = ts.translate_text(
        query_text=filename, translator='alibaba', to_language='zh-CN')
    print(title_cn)
    new_videos.download(output_path='./videos', filename=filename)

    # 获取封面图
    os.system(
        "ffmpeg -i ./videos/{filename} -vf 'select=eq(pict_type\, I)' -vframes 1  -vsync vfr -qscale:v 2 -f image2 v1080p_audio_output.jpeg -y")


# while True:
for everyChannel in upload_log['uploads']:
    channel_url = everyChannel['channelUrl']
    latest_video_id = everyChannel['videos'][0]['id']
    video_info = getVideoInfo(channel_url)

    if video_info['id'] != latest_video_id:
        print('旧id:' + latest_video_id)
        print('新id:' + video_info['id'])
        video_log = dict(id=video_info['id'], url=video_info['url'], name=video_info['name'], publishDate=str(
            video_info['publishDate']), published=[])
        everyChannel['videos'].insert(0, video_log)
        writeUploadsJson()

        # 下载视频
        downloadVideo(video_info['videos'])

        # break

    for everyPlatform in supported_target_platform:
        if everyPlatform not in everyChannel['videos'][0]['published']:
            video_id = everyChannel['videos'][0]['id']
            print('上传' + video_id + '到' + everyPlatform)
            # 进行视频上传

            everyChannel['videos'][0]['published'].append(everyPlatform)
            writeUploadsJson()
    time.sleep(120)
