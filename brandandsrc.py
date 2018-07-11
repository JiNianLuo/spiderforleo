from bs4 import BeautifulSoup
from selenium import webdriver
import re

def brandandsrc(bs): 
	#driver = webdriver.PhantomJS('C:\\phantomjs.exe')
	#url = 'https://product.suning.com/0070089086/128627627.html'
	# driver.get(url)
	# bs = BeautifulSoup(driver.page_source,'html.parser')
	# branda = bs.find_all('tr',parametercode="000897")
	# srca=bs.find_all('tr',parametercode="010857")

	try:
		tr = bs.find_all('tr',parametercode=re.compile("\d"))
		temp = re.findall(r"span>品牌.*?<tr",str(tr))
		brand = re.findall(r"blank.*?</a",str(temp))
		brand = re.findall(r">.*<",str(brand))
		canda = brand[0].lstrip('>').rstrip('<')
		
		# a = str(BeautifulSoup(str(branda)).find_all('a')[0])
		# canda = re.findall(r">.*<",str(a))[0].lstrip('>').rstrip('<')
	except:
		canda = ' '
	if (canda == ' '):
		try:
			branda = bs.find_all('tr',parametercode="000897")
			a = str(BeautifulSoup(str(branda)).find_all('a')[0])
			a = re.findall(r">.*<",str(a))[0].lstrip('>').rstrip('<')
		except:
			a = ' '
	else:
		a = canda
	
	
	try:
		tr = bs.find_all('tr',parametercode=re.compile("\d"))
		temp = re.findall(r"span>产地.*?<tr",str(tr))
		src = re.findall(r"val.*?</td",str(temp))
		src = re.findall(r">.*<",str(src))
		src = str(src[0]).lstrip('>').rstrip('<')
		candb = src
	except:
		candb = ' '
	if (candb == ' '):
		try:
			srca=bs.find_all('tr',parametercode="010857")
			b = BeautifulSoup(str(srca),'html.parser').find_all('td',class_="val")
			b = BeautifulSoup(str(b)).get_text()
			b = b.lstrip('[').rstrip(']')
		except:
			b = ' '
	else:
		b = candb
	
	try:
		price = bs.find_all('span',class_="mainprice")
		c = str(price)
		c =  re.findall(r"\d+\.?\d*",c)
		e = c[0]+c[1]
	except:
		e = ' '
	
	if(a == ' '):
		a = ''
	if(b == ' '):
		b = ''
	if(e == ' '):
		e = ''
	#driver.quit()
	#print(a,b)
	return a,b,e