import datetime

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

def convert_docker_date_time_to_datetime(str_datetime):
    (sdate, stime) = str_datetime.split("T")
    stime = stime.rstrip("Z")

    (h, mi, s) = stime.split(".")[0].split(":")
    (y, mn, d) = sdate.split("-")

    now = datetime.datetime(int(y), int(mn), int(d), int(h), int(mi), int(s))
    return now

start_time = json_list[0]["State"]["StartedAt"]
start_datetime = convert_docker_date_time_to_datetime(start_time)
print start_datetime

finish_time = json_list[0]["State"]["FinishedAt"]
finish_datetime = convert_docker_date_time_to_datetime(finish_time)
print finish_datetime
