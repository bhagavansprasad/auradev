import timeit
from csv import writer
 
# Hit the dynamic page 100 times, time the response time
 
t = timeit.Timer("h.request('http://127.0.0.1',headers={'cache-control':'no-cache'})","from httplib2 import Http; h=Http()")
times_p1 = t.repeat(100,1)
 
# Now hit a similar static page 100 times
t = timeit.Timer("h.request('http://127.0.0.1', headers={'cache-control':'no-cache'})","from httplib2 import Http; h=Http()")
times_p2 = t.repeat(100,1)
 
# the times to a CSV file
times = zip(times_p1, times_p2)
 
with open('times.csv','w') as f:
    w = writer(f)
    w.writerows(times)
