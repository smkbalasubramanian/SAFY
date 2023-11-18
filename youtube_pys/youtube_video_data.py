from youtube_harvesting.config.config import api_key
from googleapiclient.discovery import build
import json


def get_video_details_json(video_id):
    youtube = build('youtube', 'v3', developerKey = api_key)
    request = youtube.videos().list(part='snippet,statistics,id,contentDetails', id=video_id)
    response = request.execute()
    video_title = response['items'][0]['snippet']['title']
    publishedat = response['items'][0]['snippet']['publishedAt']
    description = response['items'][0]['snippet']['description']
    view_count = response['items'][0]['statistics']['viewCount']
    like_count = response['items'][0]['statistics']['likeCount']
    comment_count = response['items'][0]['statistics']['commentCount']
    favorite_count = response['items'][0]['statistics']['favoriteCount']
    duration = response['items'][0]['contentDetails']['duration']
    return json.dumps(
        {response['items'][0]['id'] : {
        'video_title' : video_title,
        'video_description' : description,
        'published_at' : publishedat,
        'view_count' : view_count,
        'like_count' : like_count,
        'comment_count' : comment_count,
        'duration' : duration,
        'favourite_count' : favorite_count
    }
    }
    )



# video_id = 'dg_WG0cybyk'
# video_details_json = get_video_details_json(video_id)
# print(video_details_json)
