def timeConversion(s):
	# Complete this function
	if (s[-2:] == "AM"):
		if (int(s[:2]) == 12):
			return ("00" + s[2:-2])
		else:
			return (s[:-2])
	else:
		if (int(s[:2]) == 12):
			return (s[:-2])
		else:
			return str((int(s[:2])+12)) + s[2:-2]

print (timeConversion("07:05:45PM"))
print (timeConversion("07:05:45AM"))
print (timeConversion("00:59:45AM"))
print (timeConversion("04:59:59AM"))
print (timeConversion("12:40:22AM"))
print (timeConversion("12:40:22PM"))

