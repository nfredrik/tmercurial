#!/usr/bin/python
import os
import struct

print "hello"

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
