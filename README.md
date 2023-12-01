SAFY - Streamlit Application For Youtube 

cmd to Run the Application - 
              python -m streamlit run SAFY\run_safe.py

Youtybe channel ID will be the input for the streamlit Application
once its submitted the data of corresponding channel like videos,Playlists,
comments,likes dislikes,total number of comments  etc,will stored in MongoDB
and migrated to SQL and from there the main SAFY app file ( run_safy.py) 
will build the Streamlit app results along with graph.

# Project Folder Structure

Generated folder structure for the project.
**config/**
  - config.py  # Method contains contains configuration Variables
**database/**
  - db_connections.py   # Methods for SQL & MONGO db connections 
  - db_migrate_to_sql.py  # Operations for data migration to sql
  - db_queries.py # Contains  individual SQL Queries in dict 
  - __init__.py
**lib/**
  - convert_iso_duration.py # commom Operation for time casting
  - str_to_datetime.py      # common conversion for time casting 
**safy_app/**
  - streamlit_query_option.py # Option list for streamlit app
**youtube_pys/**
  - youtube_channel_data.py  # Method for channel information
  - youtube_video_data.py    # Methods for video information 
- __init__.py
