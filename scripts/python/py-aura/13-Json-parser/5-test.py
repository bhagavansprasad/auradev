import datetime
import aura_date_time

def get_docker_date_time_to_date(str_created_time):
	tlist = str_created_time.split("T")
	tldate = tlist[0].split("-")

	tltime = tlist[1].rstrip("Z").split(":")
	cdate = datetime.datetime(int(tldate[0]), int(tldate[1]), int(tldate[2]), int(tltime[0]), int(tltime[1]), int(tltime[2].split(".")[0]))
	return (cdate)

def get_delta_days_by_dates(past_date, cdate):
	return (cdate - past_date)

def aura_get_elapsed_days_by_past_date(strdate):
	created_time = get_docker_date_time_to_date(strdate)
	days = get_delta_days_by_dates(created_time, datetime.datetime.now())
	return (days)

def aura_get_elaspsed_time_in_str_format(str_created_time):
	days = aura_get_elapsed_days_by_past_date(str_created_time)
	#print ("result ", days)
	#print ("days   ", days.days)
	#print ("sec    ", days.seconds)
	return "8 weeks"

def main():
	'''
	str_created_time =  "2016-12-29T10:30:07.119045211Z"
	selapsedtime = aura_get_elaspsed_time_in_str_format(str_created_time)
	print (selapsedtime + "ago")
	'''
	print("file",     datetime.__file__)
	print("name ",    datetime.__name__)
	print("package ", datetime.__package__)
	#print("path ",    datetime.__path__)
	#print("version ", datetime.__version__)
	#print("build   ", datetime._build) 
	'''
	'''

if (__name__ == "__main__"):
	main()
