#!/usr/bin/python -tt
import os,  sys
import commands
import struct

# TODO
# include __main__ stuff
# include log-functions
# assert()?
#
# include generation of dtb files...
# arguments to raise?
# take care of exception?
#

BIG_BINARY = 'serveral.dtb'
BLOBSIZE = 1024 * 10
FILLPATTERN = 0x00
NAMESTART  = 0x4c

class DeviceTree:
    """
      Convert a device tree file to a binary file
    """
    def __init__(self, name):
       cmd ='./dtc'
       if (not os.path.exists(cmd)):
           print 'no dt compiler!'
           sys.exit(42)

       cmd+= '-b0 -p 1024 -O dtb ' + name + '.dts ' + ' -o ' + name +'.dtb'

       print 'I want to execute:' + cmd
       return
       sys.exit(42)

       (status, output) = commands.getstatusoutput(cmd)
       if status:
         print 'command failed: ' + output
         sys.exit(42)

class Blob:
    """
      Add some extra bytes till out to a 10k file
    """
    def __init__(self, name):

        name+= '.dtb'
        if (not os.path.exists(name)):
           print("file do not exist")
           sys.exit(42)

        self.size = os.path.getsize(name)
        if (self.size < BLOBSIZE):
            print("to big blob")
            sys.exit(42)

        self.name = name
        self.fh = open(name,  'a+')

        # TODO: get a better solution to read out ...
        self.fh.seek(NAMESTART)
        self.board = ''
        for n in range(10):
         self.board +=  self.fh.read(1)

        for n in range(0,  BLOBSIZE-self.size):
            self.data = struct.pack('B', FILLPATTERN)
            self.fh.write(self.data)
        self.fh.close()

    def __str__(self):
        return self.name

    def board (self):
        return self.board



# TODO: Generate blobs out of device tree files ....

# Make every blob 10k size so we can predict addresses in NOR
dt_list =  ['nisse','pelle' ]

blob_list = []
try:
    # Be careful, dtb are generated from dts
    for dt in  dt_list:
       DeviceTree(dt)

    for blob in  dt_list:
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

print '\n The ' + BIG_BINARY +  ' contains following blobs:'
i = 1
for item in blob_list:
    print  '   ' + str(i) +  '. '  + item.board
    i+=1

