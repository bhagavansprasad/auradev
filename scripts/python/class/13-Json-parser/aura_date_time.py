import datetime

def get_docker_date_time_to_date(str_date_time):
    (yyyy, mm, dd) =  str_date_time[:9].split("-")
    print("xxxxx")
    return datetime.date(int(yyyy), int(mm), int(dd))
