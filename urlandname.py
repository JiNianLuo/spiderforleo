from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
def urlandname(bs):
	#driver = webdriver.PhantomJS(executable_path = 'C:\phantomjs.exe')
	#url = 'https://g.suning.com'
	# driver.get(url)
	# bs = BeautifulSoup(driver.page_source)
	dirl = bs.find_all('div',class_="os-detail-left")
	dirr = bs.find_all('div',class_="os-detail-right")
	div = str(dirl) + str(dirr)
	bdd = BeautifulSoup(str(div))
	urlandname = bdd.find_all('dd')
	a = BeautifulSoup(str(urlandname)).find_all('a')
	rea = re.findall(r"href=(.*?)</a>",str(a))
	#driver.quit()
	# i = 0
	ans = {}
	for item in rea:
		tempa = re.findall(r"http.*?\"",item)
		tempb = item.split('>')
		ans[tempb[-1]] = tempa[0].strip('"')
		# i += 1
	# print(i)
	return ans

	#here we have got a dict in the form of name:url.
	#use the name as the category, also the 3rd level of dictionary to be archived.