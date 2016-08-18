# thread based server

import socket
import threading
import sys
import os

metaSize = 512

ip = "0.0.0.0"
port = 9998

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, port))

server.listen(5)
print "[*] Server started"
print "[*] Listening on %s:%d" %(ip, port)

# the progress bar function
def progress(perc):
	sys.stdout.write('\r')
	sys.stdout.flush()
	sys.stdout.write("[=>] Status "+str(perc)+"%")

def handleClient(client):
	metadata = ""
	metadata = client.recv(metaSize)
	#print metadata
	metadata = metadata.strip('!')
	fileName = metadata.split(":")[0]
	fileSize = metadata.split(':')[1]
	#fileName = fileName + "_1"
	print "[=>] Recieving file: %s" %(fileName)
	#print "[=>] Size: %s" %(fileSize)
	print "[=>] Size: "+str(int(fileSize)/1000000) + "." + str(int(fileSize) % 1000000) + " MB"
	file = open(os.path.join("downloads",fileName), "wb")

	# file size completion calculation
	fileSize = int(fileSize)
	ten_p = fileSize * 0.1
	next = ten_p
	comp = 0.0

	comp = 0.0

	while True:
		request = client.recv(1024)
		comp += 1024
		if request:
			file.write(request)
			if comp >= next:
				next += ten_p

			progress(str(comp/float(fileSize) * 100)[:5])
		else:
			print ""
			break

	#client.send("=> Welcome to the server\n")
	print "[=>] Recieved %s" %(fileName)
	print "[*] Connection closed"
	client.close()

while True:
	try:
		client, addr = server.accept()
		print "[*] Accepted connection from %s:%d" %(addr[0], addr[1])
		clientHandler = threading.Thread(target=handleClient, args=(client, ))
		clientHandler.start()
	except KeyboardInterrupt:
		print "\n[*] Server shutting down"
		sys.exit()
