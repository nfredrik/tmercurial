#!/usr/bin/python -tt

packet = [

0x83,
0xfa,
0x18,
#0x03,
0xc1,
0x6b,
0x8f
];

chksum = 0

for i in packet:
  chksum+= i;
  print 'added:', hex(i)


print hex(0xff and chksum);
