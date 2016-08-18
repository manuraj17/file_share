# A file splitter and metadata created. 
import os
import sys

part = 1

filename	=	sys.argv[1]
file 		= 	open(filename, "rb")
print "[*] File to split %s" %(sys.argv[1])
print "[*] Split size : 1000 kB"

buff = ""

while True:
	buff = file.read(1000000)

	if buff == "":
		part -= 1
		break

	else:
		outfile = open(str(part), "wb")
		outfile.write(buff)
		outfile.close()
		part += 1

print "[*] Split complete"
print "[*] Number of parts: %d" %(part)

metadata = open("meta_"+filename, "wb")
metadata.write("1000::"+str(part)+":"+sys.argv[1])
metadata.close()

file.close()

