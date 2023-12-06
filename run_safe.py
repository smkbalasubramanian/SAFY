from database.db_connections import *
from database.db_migrate_to_sql import *
from youtube_pys.youtube_channel_data import *
from database.db_queries import query_dict
from sqlalchemy import create_engine
import json
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from safy_app.streamlit_query_option import menu_options
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
print(ROOT_DIR)
st.set_page_config(layout="wide")
# Sidebar menu
# Main content area

st.markdown("<h1 style='color: #b56562;'>SAFY - Streamlit App For Youtube</h1>", unsafe_allow_html=True)
#logo_image = "path/to/your/logo.png"  # Replace with the path to your logo image
#st.image(logo_image, use_column_width=False, width=100)
# st.title("")
id = st.text_input("Enter YouTube Channel Name:")
submitted = st.button("Submit")
if not id == '':
    mb = st.button('Migrate to DB')
    if mb:
        channel_data_json = channel_info(id)
        channel_video_json = get_video_details_json(id,channel_data_json)
        mdc = mongo_db_connection()
        mdc.insert_one(channel_video_json)
        print("Database inserted into MongoDB")
        st.success("Database inserted into MongoDB!")
        for channel_video_json in mdc.find():
            del channel_video_json['_id']
            #print(json.dumps(channel_video_json, indent=4))
        cursor = sql_connecion()
        d = migrate_data_to_sql(cursor[0],cursor[1],channel_video_json)
        cursor[1].close()
        st.success("Data Migration Successful!")
    selected_option = st.sidebar.radio("Select an option", menu_options)
    cursor = sql_connecion()
    cur = cursor[0]
    con = cursor[1]

    if selected_option.startswith('I.'):
        st.header(selected_option)
        df = pd.read_sql_query(query_dict['I.'], con)
        st.dataframe(df)
        fig = px.bar(df, x="channel_name", y="video_title", title="Channel info")
        with st.expander("View Graph", expanded=False):
            # Display the chart in the expander
            st.plotly_chart(fig)

    elif selected_option.startswith('II.'):
        st.header(selected_option)
        df = pd.read_sql_query(query_dict['II.'], con)
        st.dataframe(df)
        fig = px.bar(df, x="channel_name", y="Number_of_Videos", title="Channel info")
        with st.expander("View Graph", expanded=False):
            # Display the chart in the expander
            st.plotly_chart(fig)

    elif selected_option.startswith('III.'):
        st.header(selected_option)
        df = pd.read_sql_query(query_dict['III.'], con)
        st.dataframe(df)
        fig = px.bar(df, x="channel_name", y="view_count", title="Most viewed videos")
        with st.expander("View Graph", expanded=False):
            # Display the chart in the expander
            st.plotly_chart(fig)


    elif selected_option.startswith('IV.'):
        st.header(selected_option)
        df = pd.read_sql_query(query_dict['IV.'], con)
        st.dataframe(df)
        fig = px.bar(df, x="video_title", y="Number_of_Comments", title="Most Commented videos")
        with st.expander("View Graph", expanded=False):
            # Display the chart in the expander
            st.plotly_chart(fig)

    elif selected_option.startswith('V.'):
        st.header(selected_option)
        df = pd.read_sql_query(query_dict['V.'], con)
        st.dataframe(df)
        fig = px.violin(df, x="channel_name", y="likes", title="Most Liked Channel")
        with st.expander("View Graph", expanded=False):
            # Display the chart in the expander
            st.plotly_chart(fig)

    elif selected_option.startswith('VI.'):
        st.header(selected_option)
        df = pd.read_sql_query(query_dict['VI.'], con)
        st.dataframe(df)
        fig = px.line(df, x="video_title", y="Total_Likes", title="Likes & Dislikes")
        st.plotly_chart(fig)



    elif selected_option.startswith('VII.'):
        st.header(selected_option)
        df = pd.read_sql_query(query_dict['VII.'], con)
        st.dataframe(df)
        fig = px.area(df, x="channel_name", y="Total_Views", title="Channel & Views")
        with st.expander("View Graph", expanded=False):
            # Display the chart in the expander
            st.plotly_chart(fig)

    elif selected_option.startswith('VIII.'):
        st.header(selected_option)
        df = pd.read_sql_query(query_dict['VIII.'], con)
        st.dataframe(df)

    elif selected_option.startswith('IX'):
        st.header(selected_option)
        df = pd.read_sql_query(query_dict['IX.'], con)
        st.dataframe(df)
        fig = px.bar(df, x="channel_name", y="Average_Duration", title="Average Duration ")
        with st.expander("View Graph", expanded=False):
            # Display the chart in the expander
            st.plotly_chart(fig)

    elif selected_option.startswith('X.'):
        st.header(selected_option)
        df = pd.read_sql_query(query_dict['X.'], con)
        st.dataframe(df)
        fig = px.bar(df, x="video_title", y="comments", title="Channel Name & Comments")
        with st.expander("View Graph", expanded=False):
            # Display the chart in the expander
            st.plotly_chart(fig)


    con.close()
