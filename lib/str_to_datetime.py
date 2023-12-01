from datetime import datetime

def convert_to_datetime(time_string):
    datetime_object = datetime.strptime(time_string, "%Y-%m-%dT%H:%M:%SZ")
    return datetime_object