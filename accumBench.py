#! python3

import time, psutil

#get time to add to name of log file
timestr = time.strftime('%Y-%m-%d__%Hh%Mm%Ss')

#open log file in write mode with current time in its name
logFile = open('BatteryStatus ' + timestr + '.txt', 'w')


battery = psutil.sensors_battery()
percent = battery.percent

while battery.percent > 15:
	battery = psutil.sensors_battery()
	percent = battery.percent
	print('Battery percent is ' + str(percent))
	time.sleep(5)
