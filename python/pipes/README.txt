
First:

sudo socat PTY,link=/dev/inp PTY,link=/dev/outp

Check we're using the same baud rate, 38400....

Check to what file names they get:

/dev/pts/3 etc ....


Use it in the application

serial.open('/dev/pts/3') ...


and in the python-script

open('/dev/pts/3') ....


sen är det bara att köra .... :-)

sudo ./serialport  # applikationen

sudo ./gen_data.py  # testskriptet !!!
