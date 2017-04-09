#! python3

'''Script that infinitely launch some URL in crhome'''

import pip, time

try:
	from selenium import webdriver
except:
	pip.main(['install', 'selenium'])

from selenium import webdriver

browser = webdriver.Chrome(executable_path=r".\\chromedriver.exe")

toggleTimer = 25

while True:
	browser.get('https://www.computeruniverse.ru/')
	time.sleep(toggleTimer)
	browser.get('https://unsplash.com/')
	time.sleep(toggleTimer)
	browser.get('https://3dnews.ru/')
	time.sleep(toggleTimer)
	browser.get('http://www.ferra.ru/')
	time.sleep(toggleTimer)
