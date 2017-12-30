#! python3

'''Script that infinitely launch some URL in crhome'''

import pip, time
import random

try:
	from selenium import webdriver
except:
	pip.main(['install', 'selenium'])

from selenium import webdriver

browser = webdriver.Chrome(executable_path=r".\\chromedriver.exe")

urlList = [
	'https://www.computeruniverse.ru/',
	'https://unsplash.com/',
	'https://3dnews.ru/',
	'http://www.ferra.ru/',
] 
toggleTimer = 25

while True:
	browser.get(random.choice(urlList))
	time.sleep(toggleTimer)
	