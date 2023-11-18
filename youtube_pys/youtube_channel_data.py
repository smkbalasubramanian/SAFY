from googleapiclient.discovery import build
import requests
import json
from youtube_harvesting.config.config import api_key
from youtube_video_data import get_video_details_json


def channel_info(channel_id):
    """
    Returns the YouTube Channel Info like Name,views count,tile,No of Videos
    :param channel_id:
    :return: Dict of channel data's
    """
    youtube = build('youtube', 'v3',
                    developerKey=api_key)
    ch_request = youtube.channels().list(
        part='statistics,snippet,id,contentDetails',
        id=channel_id)
    ch_response = ch_request.execute()
    sub_count = ch_response['items'][0]['statistics']['subscriberCount']
    channel_des = ch_response['items'][0]['snippet']['description']
    channel_name = ch_response['items'][0]['snippet']['title']
    total_videos = ch_response['items'][0]['statistics']['videoCount']
    channel_views = ch_response['items'][0]['statistics']['viewCount']
    return {"channel_name" : channel_name,
            "channel_id": channel_id,
            "subscription_Count" : sub_count,
            "channel_views": channel_views,
            "channel_description" : channel_des,
            "video_count" : total_videos,
           }

def video_id_list(channel_id):
    """
    Returns the list of first 50 video's in the channel ID
    :param channel_id:
    :return:
    """
    url = ("https://www.googleapis.com/youtube/v3/search?key={}"
           "&channelId={}&part=id,snippet&order=date&maxResults=150").format(api_key,channel_id)
    resp = requests.get(url).json()
    g = resp['items']
    chnl_video_lst = list()
    for video_id in resp['items']:
        try:
            chnl_video_lst.append(video_id['id']['videoId'])
        except:
            continue
    return (chnl_video_lst)

def channel_details_json(id):
    #print(video_id_list(id))
    channel_info_dict = channel_info(id)
    video_json_list = list()
    vds_lst = video_id_list(id)
    for id in vds_lst:
        try:
            video_json_list.append(json.dumps(get_video_details_json(id)))
        except:
            continue
    channel_info_json = json.dumps({channel_info_dict['channel_id']:{"Channel_info" : channel_info_dict,
                                        "video_list" : video_json_list
                                        }})
    return channel_info_json

def get_youtube_channel_id(channel_name):
    youtube = build('youtube', 'v3',
                        developerKey=api_key)

    request = youtube.search().list(q='Autodidact', type='channel', part='id', maxResults=10)
    response = request.execute()
    channel_id = response['items'][0]['id']['channelId']
    print(channel_id)
    return channel_id