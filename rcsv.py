import csv
def rcsv(path = 'C:\\Users\\leo\\Desktop\\input.csv'):
	ans = []
	with open(path,newline='') as f:
	# reader = csv.reader(f,delimiter=':',quoting=csv.QUOTE_NONE)
	# minconf = 1
	# maxconf = 42
	# i = 0
	# for row in reader:
		# print(row)
		# if(minconf <= i and i <= maxconf):
			# a = row[0].split(',')
			# print(a)
			# ans += [a[-2]]
			# for item in a:
				# print(item)
		# else: break
		# print(ans)

		# f = open('C:\\Users\\leo\\Desktop\\input.csv',newline='')
		reader = csv.reader(f,delimiter=':',quoting=csv.QUOTE_NONE)
		minconf = 2
		num = 41
		for row in reader:
			# print(row)
			# if(minconf <= i and i <= maxconf):
			a = row[0].split(',')
			#print(a)
			ans += [a[-1]]
			#print(a[-2])
			# i += 1
			#for item in a:
				#print(item)
			# elif (i < minconf):
				# continue
			# else:
				# break
		ans = ans[minconf-1:minconf-1+num]
	# print(ans)
	return ans
# f.close()
if __name__ == "__main__":
	rcsv()
