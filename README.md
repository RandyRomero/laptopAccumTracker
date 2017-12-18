# laptop_accum_tracker

Small script that checks battery status of a laptop infinitely. Tested on Windows 10.
It prints out and writes to logFile the percentage of charge and current time every 120 seconds or every N seconds you want it to. 
Initially it checks if there is 'psutil' module on your PC. If not, it will be installed. 
Script can also show warning message if laptop is not unplugged. 
As a new feature it can open Google Chrome and some page there - for battery benchmarking purpose. 
