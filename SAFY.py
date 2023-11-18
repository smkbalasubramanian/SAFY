from database.db_connections import mongo_db_connection
from SAFY.youtube_pys.youtube_channel_data import get_youtube_channel_id
import json
import streamlit as st
import pandas as pd
import numpy as np


st.header("Helo")
st.title('MY FIRST STREAMLIT APP')


#again added
"""
# id='UCKFIBM4IAxQfc71AZqrPX6g'
#id = 'UCGo5uT3qxwsSidWL_j-YDcw'
id = get_youtube_channel_id('CETech')
#id = 'UChtI4Ghi9nmZIvjlarhsmiA'
mongodb_json = channel_details_json(id)
data = json.loads(mongodb_json)
mdc = mongo_db_connection()
mdc.insert_one(data)
print("check db")
"""