from urlandname import *
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re

def main():
	driver = webdriver.PhantomJS(executable_path = 'C:\phantomjs.exe')
	dict = urlandname(driver = driver)
	print(dict)
	driver.quit()
	print(dict['花王'])
	return 0

if __name__ == "__main__":
	main()