# a raw client

import socket
import getopt
import sys
import os

#testing
import time

metadata               = ""
#server = ""
#port = 9999

def usage():
	print "./cli.py -s <server> -p <port> -f filename"
	print "-s --server target server"
	print "-p --port   target port"
	print "-f --file   file name"
	print "-h --help   help"

def parseInput(args):
	if len(args) < 6:
		usage()

	return args[2], args[4], args[6]

def progress(perc):
	sys.stdout.write('\r')
	sys.stdout.flush()
	sys.stdout.write("[*] Status "+str(perc)+"%")
#opts, args = getopt.getopt(sys.argv[1:], "s:p", ["server=", "port="])
#usage()

server, port, fileName = parseInput(sys.argv)


client                 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print "[*] Connecting to %s:%s" %(server, port)
try:
	client.connect((server, int(port)))
	print "[*] Connection Success"
	# Max filename size = 255 bytes
	# including 4 for . and extension
	# leaves filename to 6 chars
	print "[*] Sending File %s" %(fileName)

	fileNameLen           = 255-len(fileName)
	metadata              = fileName +":"
	#client.send('!' * filler)
	#client.send(fileName)
	file_buffer           = ""
	# Need an exception file handling
	st                    = os.stat(fileName)

	# file size in bytes
	fins                  = st.st_size
	fileSize              = str(fins)

	metadata             += fileSize

	metadata              = '!' * (512-len(metadata))+ metadata

	# Sending the file metadata
	client.send(metadata)

	# for every 10% add one dot
	ten_p                 = fins * 0.1
	next                  = ten_p
	comp                  = 0.0

	print "[*] Size: "+str(st.st_size/1000000) + "." + str(st.st_size % 1000000) + " MB"

	file                  = open(fileName, "rb")
	#sys.stdout.write("[*] Sending[")

	while True:

		file_buffer          = file.read(1024)
		comp                += 1024
		if file_buffer == "":
			print ""
			print "[*] Send complete"
			break
		else:
			#sys.stdout.write('.')
			if comp            >= next:
				next              += ten_p

			#print str(comp/float(fins) * 100)[:5]
			progress(str(comp/float(fins) * 100)[:5])
			client.send(file_buffer)

	file.close()

except Exception as e:
	print "[*] Connection Failed"
	print("[*] Exception is %s" % ( e))
finally:
	client.close()



#response = client.recv(1024)
#print response
#print "%s, %s" %(server, port)
#print sys.argv
#for o, a in opts:
#	print o+":"+a
#for o, a in opts:
#	if o in ("-s", "--server"):
#		server = a
#	elif o in ("-p", "--port"):
#		port = a
#	elif on in ("-h", "--help"):
#		usage()


#print "[*] Connecting to %s:%s" %(server, port)
#print type(port)
