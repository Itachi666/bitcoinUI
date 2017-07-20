import os
import subprocess

#command1 = 'bitcoind.exe -testnet -datadir=D:\Bitcoin'
#subprocess.Popen(command1)



c= 'bitcoin-cli.exe -testnet -datadir=D:\Bitcoin listunspent'
r = os.popen(c)
info = r.readlines()
for line in info:
    line = line.strip('\r\n')
    print line

c= 'bitcoin-cli.exe -testnet -datadir=D:\Bitcoin getinfo'

r = os.popen(c)
info = r.readlines()
print info
for line in info:
    line = line.strip('\r\n')
    print line