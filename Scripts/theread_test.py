import visa
import time
import script
import os
import thread
from subprocess import Popen
from multiprocessing import Process


def script_info():
	return info

def testThread(ts):
	print "dd"
	#f=open("c:\ggg.txt","wt")

	for i in range(5):
		a=5
		ts.log_debug("thread 2")
		ts.sleep(1)
		#f.write("ddd")

	f.close()	
	return	

def run(test_script):
	global ts
	
	ts=test_script
	proc=script.Process(target=testThread,args=(ts,))
	proc.start()


	ts.log_debug('============ test ==============')
	ts.log_active_params()
	#thread.start_new_thread(listenThead,(conn,addr))
	#p=Popen(['python','c:\profile.py'])
	#testThread(ts)
	#thread.start_new_thread(testThead,(ts))
	#proc=Process(target=testThread,args=())
	#proc.start()
	
	for i in range(5):
		ts.log_debug("thread 1")
		ts.sleep(3)
	result="good"
	proc.join()
	ts.result(result)
	

def test_run():
	result = script.RESULT_FAIL
	try:
		rm=visa.ResourceManager()
		inst=rm.open_resource('ASRL5::INSTR')
		inst.baud_rate=19200
		inst.write("*IDN?")
		result=inst.read()
	except Exception, e:
		ts.log_error(e)
		
	inst.close()	
	return result



info = script.ScriptInfo(name=os.path.basename(__file__), run=run, version='1.0.0')
