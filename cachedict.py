from urlandname import *
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def cachedict():
	urlori = 'https://g.suning.com'
	driver = webdriver.PhantomJS(executable_path = 'C:\phantomjs.exe')
	driver.get(urlori)
	bs = BeautifulSoup(driver.page_source)
	dict = urlandname(bs)
	driver.quit()
	return dict