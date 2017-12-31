#!python3

# Small script that infinitely checks battery status of a laptop until its become lower than 11%.
# It prints out and writes to logFile percentage of charge and current time every 120 seconds
# or every N seconds you want it to.
# Initially it checks if there is 'psutil' module on PC. if not, it will be installed.

import pip
import time
import os
import subprocess
import sys

# Checks if module 'psutil' has already been installed. If not - it's gonna be installed
try:
    __import__('psutil')
except ImportError:
    pip.main(['install', 'psutil'])

import psutil

if not os.path.exists('log'):
    os.mkdir('log')




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
logFile = os.path.join('log', 'BatteryStatus ' + timestr + '.txt')

startTime = time.time()

# check period
period = 120


def readable_time(second):
    h = int(second / (60 * 60))
    m = int((second % (60 * 60)) / 60)
    s = second % 60
    return "{} hour {:>02} min {:>02.0f} second".format(h, m, s)


while True:
    battery = psutil.sensors_battery()
    percent = battery.percent

    # create messages to print and log
    messageBox = []
    if battery.power_plugged:
        messageBox.append('The laptop is pluged.')
    timeNow = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    messageBox.append(timeNow + ': battery level : ' + str(percent) + '%.')
    elapsed = time.time() - startTime
    messageBox.append('Script has been running for {}'.format(readable_time(elapsed)))
    messageBox.append('Ctrl+C to quit.\n')
    message = '\n'.join(messageBox)

    print(message)
    with open(logFile,'a') as f:
        f.write(message)
    time.sleep(period)