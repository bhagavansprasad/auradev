#!/usr/bin/python
import time
import calendar
import datetime

ticks = time.time()
print ("Number of ticks since 12:00am, January 1, 1970: %d" % (ticks))

print ("")

localtime = time.localtime(ticks)
print ("Local current time :", localtime)

#time.sleep(5)

localtime = time.localtime()
print ("Local current time :", localtime)

cal = calendar.month(2017, 9)
print ("Here is the calendar:")
print (cal)

print ("Time in seconds since the epoch: %s" % time.time())
print ("Current date and time          :", datetime.datetime.now())
print ("Or like this                   :", datetime.datetime.now().strftime("%y-%m-%d-%H-%M-%Y-%m-%m-%H"))
print ("Current year                   :", datetime.date.today().strftime("%Y"))
print ("Month of year                  :", datetime.date.today().strftime("%B"))
print ("Month of year                  :", datetime.date.today().strftime("%h"))
print ("Week number of the year        :", datetime.date.today().strftime("%W"))
print ("Weekday of the week            :", datetime.date.today().strftime("%w"))
print ("Day of year                    :", datetime.date.today().strftime("%j"))
print ("Day of the month               :", datetime.date.today().strftime("%d"))
print ("Day of week                    :", datetime.date.today().strftime("%A"))

now = datetime.datetime(2003, 8, 4, 12, 30, 45, 1234)
print (now)
print (repr(now))
print (type(now))
print (now.year, now.month, now.day)
print (now.hour, now.minute, now.second)
print (now.microsecond)

myt = datetime.time(1, 2, 3, 45)
print (myt)
print ('hour  :', myt.hour)
print ('minute:', myt.minute)
print ('second:', myt.second)
print ('microsecond:', myt.microsecond)
print ('tzinfo:', myt.tzinfo)

today = datetime.date.today()
print ('Today    :', today)

some_day = datetime.timedelta(days=45)
print ('One day  :', some_day)
print(type(some_day))

past_date = today - some_day
print ('past_date:', past_date)
print (type(past_date))

future_date = today + some_day
print ('Future_date :', future_date)

print ('future_date - past_date  :', future_date - past_date)
print ('past_date   - future_date:', past_date   - future_date)

print ('Times:')
t1 = datetime.time(12, 55, 0)
print ('t1:', t1)

t2 = datetime.time(13, 5, 0)
print ('t2:', t2)
print ('t1 < t2:', t1 < t2)
#print (help(datetime.timedelta))

print ('Dates:')
d1 = datetime.date.today()
print ('\td1:', d1)

d2 = datetime.date.today() + datetime.timedelta(days=-5)
print ('\td2:', d2)

print ('\td1 > d2:', d1 > d2)
exit(1)
