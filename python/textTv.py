#!/usr/bin/python

import urllib
import re

# 'OMX STOCKHOLM           359.39  -1.45'

class textTv:

    def __init__(self):
        self.sock = urllib.urlopen("http://svt.se/svttext/web/pages/202.html")
        self.html = self.sock.read()
        self.sock.close()
        self.index = re.search('OMX STOCKHOLM[ \t]*([\d]*\.[\d]*)[ \t]*([+-][\d]*\.[\d]*)',  self.html)
    def getindex(self):
         print self.index.group(1)
    def getdeviation(self):
        print self.index.group(2)
        
        
        
        
# main

# Howto get the string from method???

teksttv = textTv()

teksttv.getindex()
teksttv.getdeviation()
 

# Save in SQLite or Excel??

       
