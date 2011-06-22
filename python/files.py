#!/usr/bin/python -tt
import os,  sys
import commands
import struct
import logging


# TODO
# include __main__ stuff
# Logger class  to use for classes ...

# TODO Coding style constants?
BIG_BINARY = 'serveral.dtb'
BLOBSIZE = 1024 * 10
FILLPATTERN = 0x00
BLOB_NAMESTART  = 0x4c
MAX_BLOB_NAME_SIZE = 20
class MyLogger:
   """
      My own logging class.
   """
   def __init__(self, name):
       self.logger = logging.getLogger('MyLogger')
       self.logger.setLevel(logging.DEBUG)
       # create file handler which logs even debug messages
       self.fh = logging.FileHandler('spam.log')
       self.fh.setLevel(logging.DEBUG)
       # create console handler with a higher log level
       self.ch = logging.StreamHandler()
       self.ch.setLevel(logging.ERROR)
       # create formatter and add it to the handlers
       self. formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
       self.ch.setFormatter(formatter)
       self.fh.setFormatter(formatter)
       # add the handlers to logger
       self.logger.addHandler(ch)
       self.logger.addHandler(fh)

   def log(self, log):
       print log

class MyExcept(Exception):
    def __init__(self, string):
       print string

class DeviceTree:
    """
      Convert a device tree file to a binary file
    """
    def __init__(self, name):
       self.cmd ='./dtc'
       self.name = name
       if (not os.path.exists(self.cmd)):
           raise MyExcept( 'no dt compiler!')

       self.cmd+= '-b0 -p 1024 -O dtb ' + self.name + '.dts ' + ' -o ' + self.name +'.dtb'

       print 'I want to execute:' + self.cmd
       return
       sys.exit(42)

       (status, output) = commands.getstatusoutput(self.cmd)
       if status:
         raise MyExcept( 'command failed: ' + output)

    def generate_blob(self):
       (status, output) = commands.getstatusoutput(self.cmd)
       if status:
         raise MyExcept( 'command failed: ' + output)
         
       return self.name 

    def __str__(self):
       return 'DeviceTree'

class Blob(MyLogger):
    """
      Add some extra bytes till out to a 10k file
    """
    def __init__(self, name):

        name+= '.dtb'
        if (not os.path.exists(name)):
           raise MyExcept( 'file do not exist:' + name)

        self.size = os.path.getsize(name)
        if (self.size < BLOBSIZE):
            raise MyExcept( 'too big blob:' + name)

        self.name = name
        self.fh = open(name,  'a+')

        self.fh.seek(BLOB_NAMESTART)
        self.board = ''
        for n in range(MAX_BLOB_NAME_SIZE):
           self.token  = self.fh.read(1)
           if self.token.isalnum() : 
              self.board +=  self.token
        
        for n in range(0,  BLOBSIZE-self.size):
            self.data = struct.pack('B', FILLPATTERN)
            self.fh.write(self.data)

        self.fh.close()

    def __str__(self):
        return self.name

    def board (self):
        return self.board



def main() :
   # Check dtc exsist and is executable ...
   assert  os.path.exists('./dtc') and os.access('./dtc', os.X_OK)

   logger = logging.getLogger('MyLogger')
   logger.setLevel(logging.DEBUG)
   # create file handler which logs even debug messages
   fh = logging.FileHandler('spam.log')
   fh.setLevel(logging.DEBUG)
  # create console handler with a higher log level
   ch = logging.StreamHandler()
   ch.setLevel(logging.ERROR)
   # create formatter and add it to the handlers
   formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
   ch.setFormatter(formatter)
   fh.setFormatter(formatter)
  # add the handlers to logger
   logger.addHandler(ch)
   logger.addHandler(fh)
#logger.info('info message')
#logger.warn('warn message')
#logger.error('error message')
#logger.critical('critical message')


dt_list =  ['nisse','pelle' ]
blob_list = []

try:
    # Be careful, dtb are generated from dts
    for dt in  dt_list:
       DeviceTree(dt)

    for blob in  dt_list:
        blob_list.append(Blob(blob))

except MyExcept as X:
    X.args
    sys.exit(2)
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



if __name__ == "__main__":
  main()
