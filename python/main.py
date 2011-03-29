#!/usr/bin/python 
import sys
from target import Target

class Configuration:
    pass

path = 'mpc5121ads/'
config = Configuration()
ipaddr   = '192.168.1.205'

if len(sys.argv) != 3:
    print "Usage: ./update_fw.py <hwtype> <fw>"
    print "hwtype = hw4, hw6, cu70"
    print "fw = all, uboot, blob, kernel"
    sys.exit(42)

if (sys.argv[1] == 'cu70'):
    config.uboot    = path + 'u-boot.frsv'
    config.fdtfile  = path + 'thoreb_cu70.dtb'
    config.bootfile = path + 'uImage-touch'
elif (sys.argv[1] == 'hw4'):
    config.uboot    = path + 'u-boot.bin_0322'
    config.fdtfile  = path + 'thoreb_cidx.dtb_hw4'
    config.bootfile = path + 'uImage.hw4-20110208'
elif (sys.argv[1] == 'hw6'):
    config.uboot    = path + 'u-boot.bin_0401'
    config.fdtfile  = path + 'nfs.dtb'
    config.bootfile = path + 'uImage.test'
else:
    print "Sorry," ,sys.argv[1], "is not an option"
    sys.exit(42)

config.hw = sys.argv[1]

if (sys.argv[2] == 'all' or sys.argv[2] == 'uboot' or
    sys.argv[2] == 'blob'or sys.argv[2] == 'kernel'):
    config.fw = sys.argv[2]
else:
    print "Sorry," ,sys.argv[2], "is not an option"
    sys.exit(42)

print "Trying to stop u-boot"

#try:
target = Target(ipaddr);
target.commit(config);
target.interact();
#except:
#    print "Oops! no contact with the board"
