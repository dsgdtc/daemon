import sys,time
import os
from daemon import Daemon
from logobject import LogObject

class HelloDaemon(Daemon,LogObject):
#	def __init__(self):
#		LogObject.__init__(self)
	def run(self):
		LogObject.__init__(self)
		while True:
			file = open('/root/script/daemon/var/log/hello_daemon.log','a')
			file.write("hello daemon\n")
			file.close()
			time.sleep(2)


if __name__ == "__main__":
	daemon = HelloDaemon('/tmp/daemon-example.pid')
	if len(sys.argv) == 2:
		if 'start' == sys.argv[1]:
			daemon.start()
		elif 'stop' == sys.argv[1]:
			daemon.stop()
		elif 'restart' == sys.argv[1]:
			daemon.restart()
		elif 'status' == sys.argv[1]:
			daemon.is_running()
		else:
			print "Unknown command"
			sys.exit(2)
		sys.exit(0)
	else:
		print "usage: %s start|stop|restart" % sys.argv[0]
		sys.exit(2)
