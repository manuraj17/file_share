
import os
import sys

part = 1

meta = open("meta", "rb")
metadata = meta.read(1024)
print metadata
parts, fileName = metadata.split("::")[1], metadata.split("::")[2] 

total = int(parts)
final = open(os.path.join("downloads", fileName), "wb")

while part < total+1 :
	
	partFile = open(str(part), "rb")
	buff = partFile.read(1000000)			
	partFile.close()
	final.write(buff)

	part += 1

final.close()