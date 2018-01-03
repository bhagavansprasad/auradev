
import datetime

def convert_docker_date_time_to_datetime(str_datetime):
    (sdate, stime) = str_datetime.split("T")
    stime = stime.rstrip("Z")

    (h, mi, s) = stime.split(".")[0].split(":")
    (y, mn, d) = sdate.split("-")

    now = datetime.datetime(int(y), int(mn), int(d), int(h), int(mi), int(s))
    return now
