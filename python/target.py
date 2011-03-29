#!/usr/bin/python 
import pexpect
import sys
import time

class Target:
    def __init__(self, ipaddr):
        try:
            self.child = pexpect.spawn ('screen /dev/tty.usbserial 115200')
            fout = file('mylog.txt','w')
            self.child.logfile = fout
            self.prompt ='=>'
            self.child.expect ('MAC:')
            self.sendline_w('stop')
            time.sleep(0.2)
            self.child.sendline ('stop')
            self.child.expect(self.prompt)
   #        self.child.expect ('Unknown ')     # We're in :-)
            print "got prompt."
            self.child.sendline('set ipaddr ' + ipaddr)
            self.child.expect(self.prompt)
           # some old hw need this command too ...
#            self.child.sendline('mw 80001108 1e3d4341')
#                    self.child.expect(self.prompt)
            print "ready to rock ...."
            time.sleep(1.0)
        except:
            self.child.kill(9)

    def __str__(self):
        return "Configures a board"

    def sendline_w(self, str):
        self.child.sendline(str)
        time.sleep(0.5)

    def updateUboot(self, config):
        print "u-boot:", config.uboot
        self.child.sendline('set u-boot ' + config.uboot)
        self.child.expect(self.prompt)
        self.child.sendline('set u-boot ' + config.uboot)
        self.child.expect(self.prompt)
        self.child.sendline('fli')
        self.child.expect(self.prompt)
#        self.child.sendline('pri u-boot ')
#        self.child.expect(config.uboot)
        self.child.sendline('run load')
        self.child.expect(self.prompt)
        self.child.sendline('run update')
        self.child.expect(self.prompt)
        print "u-boot updated."

    def updateBlob(self, config):
        print "fdtfile:", config.fdtfile
#        self.child.setecho(True)
        self.child.sendline('set fdtfile ' + config.fdtfile)
        self.child.expect(self.prompt)
        self.child.sendline('set fdtfile ' + config.fdtfile)
        self.child.expect(self.prompt)
        self.child.sendline('fli')
        self.child.expect(self.prompt)
#        self.child.sendline('pri fdtfile ')
#        self.child.expect (config.fdtfile)
        self.child.sendline('run load_blob')
        self.child.expect(self.prompt)
        self.child.sendline('run update_blob')
        self.child.expect('done')
        self.child.expect(self.prompt)
        print "blob updated."

    def OLDupdateKernel(self, config):
        print "bootfile:", config.bootfile
        self.sendline_w('set bootfile ' + config.bootfile)
        self.child.expect(self.prompt)
        time.sleep(1.0)
        # there's a bug here we need to do this twice ...
        self.sendline_w('set bootfile ' + config.bootfile)
        self.child.expect(self.prompt)
        time.sleep(1.0)
        self.sendline_w('pri bootfile ')
        self.child.expect (config.bootfile)
        self.sendline_w('pri bootfile ')
        self.child.expect (config.bootfile)
        self.sendline_w('run load_kernel')
        self.child.expect(self.prompt)
        self.sendline_w('run update_kernel')
        self.child.expect(self.prompt)
        self.sendline_w('set hw ' + config.hw)
        self.child.expect(self.prompt)
        print "kernel updated."

    def updateKernel(self, config):
        self.sendline_w('set bootfile ' + config.bootfile)
        self.child.expect(self.prompt)
        time.sleep(1.0)
        # there's a bug here we need to do this twice ...
        self.sendline_w('set bootfile ' + config.bootfile)
        self.child.expect(self.prompt)
        self.child.sendline('fli')
        self.child.expect(self.prompt)
        time.sleep(1.0)
        self.sendline_w('pri bootfile ')
        self.child.expect (config.bootfile)
        self.sendline_w('pri bootfile ')
        self.child.expect (config.bootfile)
        self.sendline_w('run load_kernel')
        self.child.expect(self.prompt)
        self.sendline_w('run update_kernel')
        self.child.expect(self.prompt)
        print "kernel updated."

    def interact(self):
        self.child.interact()

    def commit(self, config):

        if (config.fw == 'uboot'):
            self.updateUboot(config)

        if (config.fw == 'blob'):
            self.updateBlob(config)

        if (config.fw == 'kernel'):
            self.updateKernel(config)

        if (config.fw == 'all'):
            self.updateUboot(config)
            self.updateBlob(config)
            self.updateKernel(config)

        self.child.sendline('set hw ' + config.hw)
        self.child.expect(self.prompt)
        self.child.sendline('savee')
        self.child.expect(self.prompt)


