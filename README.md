# laptopAccumTracker
Small script that infinetely checks battery status of laptop . 
It prints out and writes to logFile percentage of charge and current time every 120 seconds or every N seconds you want it to. 
Initially it checks if there is 'psutil' module on PC. if not, it will be installed. 
It can also show warning message if laptop is not unplugged. 
As a new feature it can opn Google Chrome and some page there - for battery benchmarking purpose. 
