#!python3

# Small script that infinitely checks battery status of a laptop until its become lower than 11%.
# It prints out and writes to logFile percentage of charge and current time every 120 seconds
# or every N seconds you want it to.
# Initially it checks if there is 'psutil' module on PC. if not, it will be installed.

import pip
import time
import logging
import subprocess
import sys

# Checks if module 'psutil' has already been installed. If not - it's gonna be installed
try:
    __import__('psutil')
except ImportError:
    pip.main(['install', 'psutil'])

import psutil

logging.basicConfig(
    format="%(levelname) -1s %(asctime)s line %(lineno)s: %(message)s",
    level=logging.DEBUG
    )


def prlog(message):
    print(message)
    logFile.write(message + '\n')


while True:
    startBrowser = (input('Hi. Do you want to start browser benchmark? (y/n): ')).lower()
    if startBrowser == 'y':
        # Run 'browserBench' simultaneously with 'accumTimer'
        subprocess.Popen([sys.executable, '.\\browserBench.py'])
        break
    elif startBrowser == 'n':
        print('Ok, only timer is gonna work.')
        break
    else:
        print('Input error. You should type in only "y" on "n".')

# Get time to add to name of log file
timestr = time.strftime('%Y-%m-%d__%Hh%Mm%Ss')

# Get battery status
battery = psutil.sensors_battery()
percent = battery.percent

totalTime = 0
# How often to check battery status
timer = 120

while True:
    battery = psutil.sensors_battery()
    percent = battery.percent
    timeNow = time.strftime('%Hh%Mm%Ss')
    # Open log file in write mode with current time in its name
    logFile = open('BatteryStatus ' + timestr + '.txt', 'a')
    if battery.power_plugged:
        prlog('\nWARNING! You forget to unplug te laptop.')
    prlog(timeNow + ': battery level is ' + str(percent) + '%.')
    prlog('Script has already been working for ' + str('%0.0f' % (totalTime/60) + ' minute(s).\n'))
    logFile.close()
    time.sleep(timer)
    totalTime = totalTime + timer
