#!/usr/bin/python

import urllib
import re
import csv

# 'OMX STOCKHOLM           359.39  -1.45'

class Storage:
    def save(self, date,  index,  deviation):
        self.date =date
        self.index=index
        self.deviation=deviation
        
        
class Calender:
    def store(self,  date):
        cmd = "google calendar add --cal \"dagar\" \"Susanne dag "
        cmd +=date
        cmd += "\""
        print cmd
            
            
class CSV(Storage):
    def display(self):
        print self.date,  self.index,  self.deviation

class textTv:

    def __init__(self):
        self.sock = urllib.urlopen("http://svt.se/svttext/web/pages/202.html")
        self.html = self.sock.read()
        self.sock.close()
        self.index = re.search('OMX STOCKHOLM[ \t]*([\d]*\.[\d]*)[ \t]*([-+][\d]*\.[\d]*)',  self.html)
        print self.index.groups()
    def getindex(self):
        print self.index.group(1)
    def getdeviation(self):
        print self.index.group(2)
        
        
        
        
# main

# Howto get the string from method???

calender = Calender()

turn = csv.reader(open('dagar.csv', 'rb'), delimiter=' ', quotechar='|')

for row in turn:
    test =  ',' .join(row)
    calender.store(test)
