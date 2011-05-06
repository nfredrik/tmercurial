#!/usr/bin/python
import os
import struct

class Blob:
    def __init__(self, name):
        self.name = name
        self.fh = open(name,  'a+')
        self.size = os.path.getsize(name)
        print self.size
        for n in range(0,  10240-self.size):
            self.data = struct.pack('B', 0x11)
            self.fh.write(self.data)
        self.fh.close()
    def __str__(self):
        return self.name
            


blob_list =  []

blob_list.append(Blob('nisse.bin'))
blob_list.append(Blob('pelle.bin'))

totalFily = open('totaly.bin', 'a+')

for item in blob_list:
    totalFily.write(open(item.__str__()).read())

totalFily.close()

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
