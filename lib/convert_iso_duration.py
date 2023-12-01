import datetime
import datetime
from isodate import parse_duration
import pymysql


def iso8601_duration_to_time(iso_duration):
    try:
        # Parse the ISO 8601 duration string
        duration = parse_duration(iso_duration)

        # Extract components (hours, minutes, seconds)
        hours, remainder = divmod(duration.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        # Format the time component as HH:MM:SS
        time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

        return time_string

    except Exception as e:
        print(f"An error occurred: {e}")
        return None



# def convert_iso_to_time(iso):
#     return iso8601_duration_to_time(iso)
