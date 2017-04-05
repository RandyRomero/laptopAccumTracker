#! python3

#Small script that infinetely checks battery status of laptop until its become under 11%. It prints out and write to logFile percentage of charge and current time every 120 seconds or every N seconds you want it to. Initially it checks if there is 'psutil' module on PC. if not, it will be installed. 

import pip, time

#checks if module 'psutil' has already been installed. If not - it's gonna be installed
try:
	__import__('psutil')
except ImportError:
	pip.main(['install', 'psutil'])

import psutil 

#get time to add to name of log file
timestr = time.strftime('%Y-%m-%d__%Hh%Mm%Ss')

#get battery status
battery = psutil.sensors_battery()
percent = battery.percent

def prlog(message):
	print(message)
	logFile.write(message + '\n')

# check and write in file status of battery every 60 sec until there is only 10 percent left
while battery.percent > 10:
	battery = psutil.sensors_battery()
	percent = battery.percent
	timeNow = time.strftime('%Hh%Mm%Ss')
	#open log file in write mode with current time in its name
	logFile = open('BatteryStatus ' + timestr + '.txt', 'a')
	prlog(timeNow + ': battery percent is ' + str(percent) + '%.')
	logFile.close()
	#timer is here, in seconds
	time.sleep(120)

battery = psutil.sensors_battery()
percent = battery.percent
timeNow = time.strftime('%Hh%Mm%Ss')
prlog(timeNow + 'Battery status is low!! (' + str(percent) + '%). Script is switching off.')
logFile.close()