# from loop import *
# from rcsv import *
# from multiprocessing import Pool

# listofneeds = []
# listofneeds = rcsv()
# pool = Pool(4)
# pool.map(loop,listofneeds)
# pool.close()
# pool.join()
from queue import Queue
from threading import Thread
from loop import *
from rcsv import *
from cachedict import *
import warnings
warnings.filterwarnings("ignore")
import datetime

class solver(Thread):
	def __init__(self,queue):
		Thread.__init__(self)
		self.queue = queue
		# print(self.queue)
		# self.url = url
		# print(self.url)
		# self.dic = dic
	
	def run(self):
		while True:
			url = self.queue.get()
			# url = self.dic[cate]
			loop(url)
			self.queue.task_done()

def main():
	start = datetime.datetime.now()
	
	
	category = rcsv()
	queue = Queue()
	dic = cachedict()
	print(len(dic))
	
	
	for cat in category:
		#logger.info('Queueing {}'.fomat(link))
		queue.put(dic[cat])
	# print(queue)
	for x in range(5):
		# cate = queue.get()
		# url = dic[cate]
		worker = solver(queue)
		worker.daemon = True
		worker.start()
	
	queue.join()
	
	
	end = datetime.datetime.now()
	delta = end - start
	print(delta.total_seconds())
	
if __name__ == "__main__":
	main()
