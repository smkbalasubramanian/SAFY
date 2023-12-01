import pymysql
import datetime
from lib.convert_iso_duration import iso8601_duration_to_time
from lib.str_to_datetime import convert_to_datetime



from isodate import parse_duration


def migrate_data_to_sql(cursor,conn,channel_data):
    # Create the 'channels' table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS channels (
            channel_id VARCHAR(255) PRIMARY KEY,
            channel_name VARCHAR(255),
            subscribers INT,
            total_videos INT,
            channel_description TEXT,
            channel_views INT
        )
    ''')
    conn.commit()

    # Create the 'playlists' table if it doesn't exist
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS playlists (
                playlist_id VARCHAR(255) PRIMARY KEY,
                playlist_name VARCHAR(255),
                channel_id VARCHAR(255),
                FOREIGN KEY (channel_id) REFERENCES channels(channel_id)
            )
        ''')
    conn.commit()


    # Create the 'videos' table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS videos (
            video_id VARCHAR(255) PRIMARY KEY,
            playlist_id VARCHAR(255),
            video_title VARCHAR(255),
            published_at DATETIME,
            duration VARCHAR(255),
            favorite_count INT,
            likes INT,
            view_count INT,
            dislikes INT,
            comments INT,
            channel_id VARCHAR(255),
            FOREIGN KEY (channel_id) REFERENCES channels(channel_id),
            FOREIGN KEY (playlist_id) REFERENCES playlists(playlist_id)
        )
    ''')
    conn.commit()


    # Create the 'comments' table if it doesn't exist
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS comments (
                comment_id VARCHAR(255) PRIMARY KEY,
                 video_id VARCHAR(255),
                comment_text TEXT,
                comment_author TEXT,
                comment_published_date DATETIME,
                FOREIGN KEY (video_id) REFERENCES videos(video_id)
            )
        ''')
    conn.commit()

    # Insert channel and video data into their respective tables
    channel = channel_data
    try:
        # Insert channel data if the primary key (channel_id) doesn't exist

        query = '''
              INSERT INTO channels (channel_name,channel_id,  channel_description,subscribers,  channel_views, total_videos)
              VALUES (%(Channel_Name)s, %(Channel_ID)s, %(Channel_Description)s, %(Subscription_Count)s, %(Channel_Views)s, %(Channel_Video_Count)s)
          '''
        values = {
            'Channel_Name': channel['channel_name'],
            'Channel_ID': channel['channel_id'],
            'Channel_Description': channel['channel_description'],
            'Subscription_Count': int(channel['subscribers']),
            'Channel_Views': int(channel['channel_views']),
            'Channel_Video_Count': int(channel['video_count'])
        }
        cursor.execute(query, values)
        conn.commit()
    except Exception as e:
        print(e,"e in channels")

    try:
        # Insert video data using IGNORE to avoid duplicate entries
        for video in channel['videos']:
            query = '''
                            INSERT INTO videos 
                            (video_id,video_title, published_at, duration,favorite_count,likes,view_count,dislikes, comments, channel_id) 
                            VALUES (%(video_id)s, %(video_title)s, %(published_at)s, %(duration)s,
                             %(favorite_count)s, %(likes)s, %(view_count)s,%(dislikes)s, %(comments)s, %(channel_id)s) 
                             '''
            duration = iso8601_duration_to_time(video['duration'])
            published_at = convert_to_datetime(video['published_at'])
            values = {
                'video_id': video['video_id'],
                'video_title': video['video_title'],
                'duration': duration,
                'published_at': published_at,
                'favorite_count': int(video['favorite_count']),
                'likes': int(video['likes']),
                'view_count' : int(video['view_count']),
                'dislikes': int(video['dislikes']),
                'comments': video['comments'],
                'channel_id': channel['channel_id']
            }
            s = query
            cursor.execute('SET FOREIGN_KEY_CHECKS=0')
            cursor.execute(query, values)
            conn.commit()
    #duration_iso_to_seconds()
    except Exception as e:
        print(e," e  in videos")

    # Insert playlist data into the 'playlists' table
    try:

        query = """INSERT INTO playlists 
           (playlist_id, playlist_name, channel_id) 
           VALUES (%(play_list_id)s, %(playlist_name)s, %(channel_id)s)"""

        for playlist in channel.get('playlists', []):
            values = {
                'play_list_id' : playlist['playlist_id'],
                'playlist_name' : playlist['playlist_name'],
                'channel_id' : channel['channel_id']
            }
            cursor.execute(query,values)
            conn.commit()

        # Insert comment data into the 'comments' table
    except Exception as e:
            print(e,"playlists")
    videos_lst = channel_data['videos']
    try:
            query = '''
                                INSERT IGNORE INTO comments 
                                (comment_id, video_id,comment_text,comment_author,comment_published_date) 
                                VALUES (%(comment_id)s, %(video_id)s, %(comment_text)s,%(comment_author)s,%(comment_published_date)s)
             '''
            for video in channel_data['videos']:
                values = {
                    'comment_id' : video['comment_id'],
                    'video_id' : video['video_id'],
                    'comment_text' : video['comment_text'],
                    'comment_author' : video['comment_author'],
                    'comment_published_date' : convert_to_datetime(video['comment_published_date'])

                }
                #print(video)
                #cursor.execute('SET FOREIGN_KEY_CHECKS=0')
                cursor.execute(query,values)
                conn.commit()
    except Exception as e:
        print(e,"comments")





