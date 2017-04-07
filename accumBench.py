#! python3

#Small script that infinetely checks battery status of laptop until its become lower than 11%. It prints out and writes to logFile percentage of charge and current time every 120 seconds or every N seconds you want it to. Initially it checks if there is 'psutil' module on PC. if not, it will be installed. 

import pip, time, logging

#checks if module 'psutil' has already been installed. If not - it's gonna be installed
try:
	__import__('psutil')
except ImportError:
	pip.main(['install', 'psutil'])

import psutil


logging.basicConfig(
	format = "%(levelname) -1s %(asctime)s line %(lineno)s: %(message)s",
	level = logging.DEBUG
	)

#get time to add to name of log file
timestr = time.strftime('%Y-%m-%d__%Hh%Mm%Ss')

#get battery status
battery = psutil.sensors_battery()
percent = battery.percent

def prlog(message):
	print(message)
	logFile.write(message + '\n')

def browserRefresh():
	try:
		from selenium import webdriver
	except:
		pip.main(['install', 'selenium'])

	from selenium import webdriver

	# browser = webdriver.Firefox()
	browser = webdriver.Chrome(executable_path=r".\\chromedriver.exe")
	time.sleep(5)
	browser.get('https://www.computeruniverse.ru/')
	time.sleep(5)
	browser.get('https://unsplash.com/')
	time.sleep(5)
	browser.get('https://3dnews.ru/')
	time.sleep(5)
	browser.get('http://www.ferra.ru/')

browserRefresh()

# check and write in file status of battery every N sec until there is only 10 percent left
totalTime = 0
timer = 120

while battery.percent > 10:
	battery = psutil.sensors_battery()
	percent = battery.percent
	timeNow = time.strftime('%Hh%Mm%Ss')
	#open log file in write mode with current time in its name
	logFile = open('BatteryStatus ' + timestr + '.txt', 'a')
	prlog(timeNow + ': battery level is ' + str(percent) + '%.')
	prlog('Script has already been working for ' + str('%0.0f' % (totalTime/60) + ' minute(s).\n'))
	logFile.close()
	#timer is here, in seconds
	time.sleep(timer)
	totalTime = totalTime + timer