import threading
import time

 exitFlag=0
 
class mythread(threading.thread)
	def __init__(self,threadID,name,counter):
		threading.thread__init__(self)
		self.threadID=threadID
		self.name=name
		self.counter=counter
	def run(self):
	print "starting"+self.name
	print_time(self.name,5,self.counter)
	print "exiting"+self.name
	
def print_time(threadname,counter,delay):
	while counter:
		if exitflag:
			threadname.exit()
		time.sleep(delay)
		print "%s:%s"%(threadname,time.ctime(time.time()))
		counter -=1

