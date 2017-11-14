import datetime
import aura_date_time

str_created_time =  "2016-12-29T10:30:07.119045211Z"
created_time = aura_date_time.get_docker_date_time_to_date(str_created_time)

print(created_time)
 

