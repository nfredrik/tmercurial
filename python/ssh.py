#!/usr/bin/python 
import pexpect
#child = pexpect.spawn ('ssh root@10.42.102.148')
child = pexpect.spawn ('ssh root@192.168.1.149')
print "started..."
child.expect ('password: ')
print "got prompt1."
child.sendline ('ny123ny')
child.expect ('# ')
print "got prompt2."
child.sendline('ls')
child.expect ('# ')
print child.before
child.interact()
