from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
def senderloc(bs):
	#driver = webdriver.PhantomJS(executable_path = 'C:\phantomjs.exe')
	# driver.get(url)
	# bs = BeautifulSoup(driver.page_source)
	span = bs.find_all('span',class_="w2")
	a = str(span[0])
	aa = BeautifulSoup(a)
	aa = aa.get_text()
	if(aa[-1] == '货'):
		aa = '保税仓发货'
	else:
		aa = '海外直邮'
	#driver.quit()
	return aa
