import requests
import os
import re
from bs4 import BeautifulSoup
from selenium import webdriver
def downloadpics(bs):
	#driver = webdriver.PhantomJS('C:\\phantomjs.exe')
	# driver.get(url)
	# bs = BeautifulSoup(driver.page_source,'html.parser')
	imga = bs.find_all('a',id="bigImg",class_="view-img")
	tmp = re.findall(r"//.*?/>",str(imga))
	tmp1 = re.findall(r"src=.*",str(tmp[0]))
	tmp = re.findall(r"//.*\"",tmp1[0])
	img = tmp[0].rstrip('"')
	img = 'https:' + img
	#url = "https://image.suning.cn/uimg/b2c/newcatentries/0000000000-000000000651478028_1.jpg_800w_800h_4e"
	url = img
	return url
	# root = "C://"
	# path = root + url.split("/")[-1]
	# path = str(re.findall(r"C:.*jpg",path)[0])
	# try:
		# if not os.path.exists(root):
			# os.mkdir(root)
		# if not os.path.exists(path):
			# r = requests.get(url)
			# r.raise_for_status()
			# with open(path,"wb") as f:
				# f.write(r.content)
			# print("successfully downloaded")
		# else:
			# print("already exists")
	# except Exception as e:
		# print("fail to download:"+str(e))
		
	#driver.quit()
