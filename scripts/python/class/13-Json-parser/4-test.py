'''
import datetime
str_created_time =  "2016-12-29T10:30:07.119045211Z"

print str_created_time[:9].split("-")
(yyyy, mm, dd) =  str_created_time[:9].split("-")
print datetime.date(int(yyyy), int(mm), int(dd))
'''

'''
import datetime

def get_docker_date_time_to_date(str_date_time):
    (yyyy, mm, dd) =  str_date_time[:9].split("-")
    return datetime.date(int(yyyy), int(mm), int(dd))

str_created_time =  "2016-12-29T10:30:07.119045211Z"
created_time = get_docker_date_time_to_date(str_created_time)
print created_time
'''

'''
import datetime
import aura_date_time

str_created_time =  "2016-12-29T10:30:07.119045211Z"
created_time = aura_date_time.get_docker_date_time_to_date(str_created_time)
print created_time
'''

