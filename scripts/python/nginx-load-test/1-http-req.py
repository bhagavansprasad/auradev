import timeit
 
# Request the page 100 times, time the response time
 
t = timeit.Timer("h.request('http://127.0.0.1/',headers={'cache-control':'no-cache'})", "from httplib2 import Http; h=Http()")
times_p1 = t.repeat(100,1)

