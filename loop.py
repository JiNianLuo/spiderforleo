from brandandsrc import *
from commurl import *
from DisplayName import *
from downloadpics import *
from SenderLoc import *
# from urlandname import *
from getid import *

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re

def loop(url):
	driver = webdriver.PhantomJS(executable_path = 'C:\phantomjs.exe')
	
	# urlori = 'https://g.suning.com'
	# driver.get(urlori)
	# bs = BeautifulSoup(driver.page_source)
	# dict = urlandname(bs)
	
	# url = dict[cate]
	# print(url)
	driver.get(url)
	bs = BeautifulSoup(driver.page_source,'html.parser')
	list = commurl(bs)
	# syn = 0
	for item in list:
		driver.get(item)
		bs = BeautifulSoup(driver.page_source,'html.parser')
		ans = []
		#print(item)
		brand,src,price = brandandsrc(bs)
		#print(brand,src,price)
		name = finditemdisplayname(bs)
		loc = senderloc(bs)
		id = getid(url = item)
		imgurl = downloadpics(bs)
		ans = [name,brand,src,price,loc,id,imgurl]
		# driver.close()
		# syn += 1
		#####this block is for test
		print(ans)
		# print('\n')
		# print(id)
		# print('\n')
		#####end
	
	driver.quit()
	return 0

if __name__ == "__main__":
	loop()