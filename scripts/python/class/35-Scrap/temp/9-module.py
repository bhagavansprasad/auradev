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

''' 
print json_list 
print json_list[0]
print json_list[0]["State"]
''' 
start_time = json_list[0]["State"]["StartedAt"]
print "start_time :", start_time
print type(start_time)

#2017-07-11T15:07:59.869672233Z
# 15:07:59.869672233Z


(sdate, stime) = start_time.split("T")
print "sdate :", sdate
stime = stime.rstrip("Z")
print stime

#print stime.split(".")
#print stime.split(".")[0].split(":")
#t1 = datetime.time(stime.split["."][0].split[":"])
#print t1
(h, mi, s) = stime.split(".")[0].split(":")
print h, mi, s
(y, mn, d) = sdate.split("-")
print y, mn, d

now = datetime.datetime(int(y), int(mn), int(d), int(h), int(mi), int(s))
print now
