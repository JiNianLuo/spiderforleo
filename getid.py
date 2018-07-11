# for iter in urll:
		# urll += [('https://product.suning.com/' + item['class'][-2][0:10] + '/' + item['class'][-2][11:] + '.html')]
		# id += [item['class'][-2][0:10] + item['class'][-2][11:]]
		# temp = re.findall(r"\d+",iter)
		# id += [str(a[0]) + '_' + str(a[1])]
import re
def getid(url):
	temp = re.findall(r"\d+",url)
	id = str(temp[0]) + '_' + str(temp[1])
	return id