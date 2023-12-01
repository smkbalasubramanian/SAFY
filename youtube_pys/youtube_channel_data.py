from googleapiclient.discovery import build
import requests
import json
from config.config import api_key
from youtube_pys.youtube_video_data import *

def get_playlist_info(channel_id):
    youtube = build('youtube', 'v3', developerKey=api_key)
    playlists = youtube.playlists().list(part='snippet', channelId=channel_id).execute()
    ret_pllylst_info = list()
    if 'items' in playlists:
        for playlist in playlists['items']:
            playlist_id = playlist['id']
            playlist_name = playlist['snippet']['title']

            # Store playlist information in MongoDB
            playlist_data = {
                'playlist_id': playlist_id,
                'channel_id': channel_id,
                'playlist_name': playlist_name,
                'videos': []
            }
            ret_pllylst_info.append(playlist_data)
    return ret_pllylst_info

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
    channel_playlist_id = ch_response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
    channel_data = {
            "channel_name" : channel_name,
            "channel_id": channel_id,
            "subscribers" : sub_count,
            "channel_views": channel_views,
            "channel_description" : channel_des,
            "video_count" : total_videos,
            "playlist_id" : channel_playlist_id,
            "videos" : [],
            "playlists" : []
           }
    channel_data.update({"playlists" : get_playlist_info(channel_id)})
    return channel_data



#
# def channel_details_json(id):
#     #print(video_id_list(id))
#     channel_info_dict = channel_info(id)
#     video_json_list = list()
#     vds_lst = video_id_list(id)
#     for id in vds_lst:
#         try:
#             video_detail = get_video_details_json(id)
#             video_json_list.append(video_detail)
#         except:
#             continue
#     return {channel_info_dict['channel_id']:{"Channel_info" : channel_info_dict,
#                                         "video_list" : video_json_list
#                                         }}
#     return channel_info_json
#
# def get_youtube_channel_id(channel_name):
#     youtube = build('youtube', 'v3',
#                         developerKey=api_key)
#
#     request = youtube.search().list(q='Autodidact', type='channel', part='id', maxResults=10)
#     response = request.execute()
#     channel_id = response['items'][0]['id']['channelId']
#     print(channel_id)
#     return channel_id