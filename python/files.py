#!/usr/bin/python
import os
import struct

BIG_BINARY = 'totaly.bin'
BLOBSIZE = 10240
FILLPATTERN = 0xff

class Blob:
    def __init__(self, name):
        self.name = name
        self.fh = open(name,  'a+')
        self.size = os.path.getsize(name)
        print self.size
        for n in range(0,  BLOBSIZE-self.size):
            self.data = struct.pack('B', FILLPATTERN)
            self.fh.write(self.data)
        self.fh.close()
    def __str__(self):
        return self.name
            


blob_list =  []

# Append all blobs to one big binary 
#blob_list.append(Blob('nisse.bin'))
#blob_list.append(Blob('pelle.bin'))

for blob in  ['nisse.bin','pelle.bin' ]:
    blob_list.append(Blob(blob))
   
   
totalFily = open(BIG_BINARY, 'a+')

for item in blob_list:
    totalFily.write(open(item.__str__()).read())

totalFily.close()


exit()

size = os.path.getsize('totaly.bin')

print str(size)


fh = open('test.bin',  'a+')
size = os.path.getsize('test.bin')

fh.seek(0, os.SEEK_END)

for n in range(0,  10240-size):
     data = struct.pack('B', 0x11)
     fh.write(data)

size = os.path.getsize('test.bin')

print str(size)


totalBinary = open('tot.bin','a+')

for f in ['test.bin', 'test.bin']:
    totalBinary.write(open(f).read())
    
totalBinary.close()
