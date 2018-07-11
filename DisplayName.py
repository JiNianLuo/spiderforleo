#import requests
from bs4 import BeautifulSoup
import re

#this is a function used to get the display name of an commodity.
#input: url(string)
#ouput: name(string)
def finditemdisplayname(bs):
	#url = 'https://product.suning.com/0070169109/624924586.html'


	#req = requests.get(url)
	#html = req.text
	#div_bf = BeautifulSoup(html,'html.parser')
	#div = div_bf.find_all('h1',id="itemDisplayName")
	#d_bf = BeautifulSoup(str(div),'html.parser')
	#name = d_bf.get_text()

	'''
	get an string indicating the display name of this item.
	note that the variables should be renamed before being copied.
	'''
	#caller need to import the selenium.driver.
	# driver.get(url)
	# bs = BeautifulSoup(driver.page_source)
	div = bs.find_all('h1',id="itemDisplayName")
	d_bf = BeautifulSoup(str(div),'html.parser')
	name = d_bf.get_text()


	n = re.findall(r"[^\[\]]*",name)
	#name = n[1].lstrip()
	name = ''.join(n).lstrip()
	#name = ''.join(name.split())
	#delete all of the whitespaces
	
	name = re.sub(r"\s{2,}"," ",name)

	# another approach to delete the '[' and ']' and leading whitespace:
	# (not sure about which is a superior approach)
	#aa = ''
	#for ch in name:
	#     if(ch != '[' and ch != ']'):
	#         aa = aa + ch
	#name = aa.lstrip()
	
	return name

if __name__ == "__main__":
	finditemdisplayname()
	#don't run it as main()
