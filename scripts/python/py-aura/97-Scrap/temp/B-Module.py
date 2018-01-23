import datetime
import sys

sys.path.append('/home/bhagavan/training/scripts/python/class/scrap/temp/mods')

import my_date_time_mod

json_list = [
    {
        "Id": "dd3756c5eafcc219b531255a3e47c8054a610c24db57b25260d806848d05d9f4",
        "Created": "2017-07-11T15:07:58.990959648Z",
        "Path": "/bin/bash",
        "Args": [],
        "State": {
            "Status": "exited",
            "Running": "false",
            "Paused": "false",
            "Restarting": "false",
            "OOMKilled": "false",
            "Dead": "false",
            "Pid": 0,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2017-07-11T15:07:59.869672233Z",
            "FinishedAt": "2017-07-11T15:08:00.169576836Z"
        }
    }
]

start_time = json_list[0]["State"]["StartedAt"]
start_datetime = my_date_time_mod.convert_docker_date_time_to_datetime(start_time)
print start_datetime

finish_time = json_list[0]["State"]["FinishedAt"]
finish_datetime = my_date_time_mod.convert_docker_date_time_to_datetime(finish_time)
print finish_datetime
