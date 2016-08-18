# hashing the files
import hashlib

BLOCKSIZE = 65536
hasher    = hashlib.sha1()

part      = 1

print("Reading the parts")
while part < 11:
	print part
	file     = open(str(part), "rb")
	buff     = file.read()
	hasher.update(buff)
	print(hasher.hexdigest())
	part    += 1


#with open('t.txt', 'rb') as afile:
#    buf = afile.read(BLOCKSIZE)
#    while len(buf) > 0:
#        hasher.update(buf)
#        buf = afile.read(BLOCKSIZE)
#print(hasher.hexdigest())
