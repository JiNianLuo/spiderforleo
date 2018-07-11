from SenderLoc import *
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re

def main():
	driver = webdriver.PhantomJS(executable_path = 'C:\phantomjs.exe')
	SL = senderloc(driver = driver)
	print(SL)
	driver.quit()
	return 0

if __name__ == "__main__":
	main()