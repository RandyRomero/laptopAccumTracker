#! python3

import time, psutil


battery = psutil.sensors_battery()
percent = battery.percent

while battery.percent > 15:
	battery = psutil.sensors_battery()
	percent = battery.percent
	print('Battery percent is ' + str(percent))
	time.sleep(5)
