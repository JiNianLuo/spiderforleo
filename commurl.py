import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver
def commurl(bs):
	#driver = webdriver.PhantomJS('C:\\phantomjs.exe')
	#url = 'https://list.suning.com/2-313005-0-0-0-0-0-0-0-0-123240.html'
	# driver.get(url)
	# bs = BeautifulSoup(driver.page_source,'html.parser')
	li = bs.find_all('li',ishwg="HWG",class_=re.compile("product"))
	a = BeautifulSoup(str(li),'html.parser').find_all('a',class_="sellPoint")
	#li = bs.find_all('li',ishwg="HWG",class_=re.compile("basic"))
	#a = bs.find_all('a',class_="sellPoint",target="_blank")
	# url = []
	# for item in a:
		# url += [('https:' + item['href'])]
	urll = []
	# id = []
	for item in a:
		urll += ['https:' + item['href']]
	urll = set(urll)
	# for iter in urll:
		# urll += [('https://product.suning.com/' + item['class'][-2][0:10] + '/' + item['class'][-2][11:] + '.html')]
		# id += [item['class'][-2][0:10] + item['class'][-2][11:]]
		# temp = re.findall(r"\d+",iter)
		# id += [str(temp[0]) + '_' + str(temp[1])]
	# print(id)
	#print(url)
	#print(urll)
	#driver.quit()
	return urll