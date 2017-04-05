#! python3

import time, psutil

#get time to add to name of log file
timestr = time.strftime('%Y-%m-%d__%Hh%Mm%Ss')

#open log file in write mode with current time in its name

battery = psutil.sensors_battery()
percent = battery.percent

while battery.percent > 15:
	battery = psutil.sensors_battery()
	percent = battery.percent
	timeNow = time.strftime('%Hh%Mm%Ss')
	logFile = open('BatteryStatus ' + timestr + '.txt', 'a')
	logFile.write(timeNow + ': battery status is ' + str(percent) + '%.\n')
	print(timeNow + ': battery percent is ' + str(percent) + '%.')
	logFile.close()
	time.sleep(5)
