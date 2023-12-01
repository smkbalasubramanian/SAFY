from config.config import api_key
from googleapiclient.discovery import build
import json


def get_video_details_json(channel_id,channel_data):
    youtube = build('youtube', 'v3', developerKey=api_key)
    videos = youtube.search().list(part='snippet', channelId=channel_id, type='video').execute()
    for video in videos['items']:
        video_id = video['id']['videoId']
        video_comments = youtube.commentThreads().list(part='snippet', videoId=video_id).execute()
        video_title = video['snippet']['title']
        video_statistics = youtube.videos().list(part='snippet,contentDetails,statistics', id=video_id).execute()
        published_at = video_statistics['items'][0]['snippet']['publishedAt']
        duration = video_statistics['items'][0]['contentDetails']['duration']
        favorite_count = video_statistics['items'][0]['statistics'].get('favoriteCount', 0)
        likes = video_statistics['items'][0]['statistics'].get('likeCount', 0)
        view_count = video_statistics['items'][0]['statistics'].get('viewCount', 0)
        dislikes = video_statistics['items'][0]['statistics'].get('dislikeCount', 0)
        comments = video_statistics['items'][0]['statistics'].get('commentCount', 0)

        if 'items' in video_comments:
            for comment in video_comments['items']:
                comment_id = comment['id']
                comment_text = comment['snippet']['topLevelComment']['snippet']['textDisplay']
                comment_author = comment['snippet']['topLevelComment']['snippet']['authorDisplayName']
                comment_published_date = comment['snippet']['topLevelComment']['snippet']['publishedAt']

        # Store video details
        video_data = {
            'video_id': video_id,
            'video_title': video_title,
            'published_at': published_at,
            'duration': duration,
            'favorite_count': favorite_count,
            'likes': likes,
            'view_count' : view_count,
            'dislikes': dislikes,
            'comments': comments,
            'comment_id' : comment_id,
            'comment_text' : comment_text,
            'comment_author' : comment_author,
            'comment_published_date' : comment_published_date

        }
        channel_data['videos'].append(video_data)
    return channel_data
