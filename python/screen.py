#!/usr/bin/python 
import pexpect
import sys
import time
import target


class Configuration:
    pass

config = Configuration()

config.ipaddr   = '192.168.1.205'
config.uboot    = 'mpc5121ads/u-boot.bin_dbg'
config.fdtfile  = 'mpc5121ads/thoreb_cu70.dtb'
config.bootfile = 'mpc5121ads/uImage.20110124'

ipaddr   = '192.168.1.205'
uboot    = 'mpc5121ads/u-boot.bin_dbg'
#fdtfile  = 'mpc5121ads/mpc5121ads.dtb'
fdtfile  = 'mpc5121ads/thoreb_cu70.dtb'
#bootfile = 'mpc5121ads/uImage.dbg'
bootfile = 'mpc5121ads/uImage.20110124'

child = pexpect.spawn ('screen /dev/tty.usbserial 115200\r\n')
#child.logfile = sys.stdout

print "started..."
print child.isalive()
print "started..."
try:
    child.expect ('MAC:')
    child.sendline ('stop')
    time.sleep(0.2)
    child.sendline ('stop')
    child.expect ('=> ')
#    child.expect ('Unknown ')     # We're in :-)
    print "got prompt."
    child.sendline('set ipaddr ' + ipaddr)
    child.expect ('=> ')
    child.sendline('set u-boot ' + uboot)
    child.expect ('=> ')
    child.sendline('set fdtfile ' + fdtfile)
    child.expect ('=> ')
    child.sendline('set bootfile ' + bootfile)
    child.expect ('=> ')
    child.sendline('run load')
    child.expect ('=> ')
    child.sendline('fli; save')
    child.expect ('=> ')
    child.sendline('run update')
    child.expect ('=> ')
    child.sendline('run load_blob')
    child.expect ('=> ')
    child.sendline('run update_blob')
    child.expect ('=> ')
    child.sendline('run load_kernel')
    child.expect ('=> ')
    child.sendline('run update_kernel')
    child.expect ('=> ')
    child.sendline('set olle glad')
    child.expect ('=> ')
    print "got prompt end."
    child.interact()
except:
    print "Exception was thrown"
    print "debug information:"
    print str(child)    
    child.kill(42);
