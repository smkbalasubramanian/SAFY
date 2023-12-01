query_dict = {

"I." : '''SELECT v.video_title, c.channel_name FROM videos v JOIN channels c ON v.channel_id = c.Channel_id;''',
"II." : '''SELECT channels.channel_name, COUNT(videos.video_title) AS Number_of_Videos FROM channels JOIN videos ON
           channels.Channel_id = videos.Channel_id GROUP BY channels.channel_name ORDER BY Number_of_Videos DESC;''',
"III." : '''SELECT v.video_title, (SELECT c.channel_name FROM channels c WHERE c.channel_id = v.channel_id) AS 
            channel_name,v.view_count FROM videos v ORDER BY v.view_count DESC LIMIT 10;''',
"IV." : '''SELECT v.video_title, COUNT(c.comment_text) AS Number_of_Comments FROM videos v LEFT JOIN comments c ON
            v.video_id = c.video_id GROUP BY v.video_title;''',
"V." : '''SELECT v.video_title,c.channel_name,v.likes FROM videos v JOIN channels c ON
       v.channel_id = c.channel_id ORDER BY v.likes DESC LIMIT 10;''',
"VI." :'''SELECT video_title, SUM(likes) AS Total_Likes,SUM(dislikes) AS Total_Dislikes 
       FROM videos GROUP BY video_title;''' ,
"VII." : '''SELECT c.channel_name,SUM(v.view_count) AS Total_Views FROM videos v JOIN
        channels c ON v.channel_id = c.channel_id GROUP BY c.channel_name;''',
"VIII." : '''SELECT DISTINCT c.channel_name FROM videos v JOIN channels c 
         ON v.channel_id = c.channel_id WHERE YEAR(v.published_at) = 2022;''' ,
"IX.": '''SELECT c.channel_name,AVG(TIME_TO_SEC(v.duration)) AS Average_Duration FROM videos v JOIN channels c ON
       v.channel_id = c.channel_id GROUP BY c.channel_name;''',
"X." : '''SELECT v.video_title, c.channel_name,v.comments FROM videos v JOIN channels c ON v.channel_id = c.channel_id 
       ORDER BY v.comments DESC LIMIT 10;'''

}