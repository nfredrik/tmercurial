#!/usr/bin/python
import os,  sys
import struct

# TODO
# include generation of dtb files...
# check if the files exists...
# Check that the blob not bigger than 10k
# arguments to raise?
# take care of exception?
# find name string in blob and print it .... should be in an fix pos in blob like mpc5121ads cu70 c20 etc...
#

BIG_BINARY = 'totaly.bin'
BLOBSIZE = 10240
FILLPATTERN = 0xff

BLOB1  = 'c30can.dtb'
BLOB2  =  'c30diu.dtb'
BLOB3  = 'c30hmm.dtb'
BLOB4 = 'c30mmh.dtb'

def isprintable(s, codec='utf8'):
    try: s.decode(codec)
    except UnicodeDecodeError: return False
    else: return True
    
    

class Blob:
    def __init__(self, name):
   
   
        if(os.path.exists(name) != True):
           raise("file do not exist")
        
        self.size = os.path.getsize(name)
        if (self.size < BLOBSIZE):
            raise("to big blob")
            
        self.name = name
        self.fh = open(name,  'a+')
 
        self.fh.seek(0x4c) 
        self.str.append(self.fh.read(1))
        
        while self.str.isalnum() :
            self.sum.append(self.str)
            self.str.append(self.fh.read(1))
            
        for n in range(0,  BLOBSIZE-self.size):
            self.data = struct.pack('B', FILLPATTERN)
            self.fh.write(self.data)
        self.fh.close()
 
    def __str__(self):
        return self.name
            


blob_list =  []

# Make every blob 10k size so we can predict addresser in NOR

try:
    for blob in  ['nisse.bin','pelle.bin' ]:
        blob_list.append(Blob(blob))

except:
    print "help some one raised an exception!"
    sys.exit(2)


# Append all blobs to one big binary 
# TODO, remove stuff in big binary...
totalFily = open(BIG_BINARY, 'a+')

for item in blob_list:
    totalFily.write(open(str(item)).read())

totalFily.close()

print "\n The binary file contains following blobs:"
for item in blob_list:
    print " ",  item

