from commurl import *
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re

def main():
	driver = webdriver.PhantomJS(executable_path = 'C:\phantomjs.exe')
	url = commurl(driver = driver)
	print(url)
	driver.quit()

if __name__ == "__main__":
	main()