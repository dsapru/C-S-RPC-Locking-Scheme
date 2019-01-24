# I have neither given or received unauthorized assistance on this work
# Signed: 1. Deepit Raj Sapru 1001522895
#         2. Ravi Chandra Kumar Venkatesh 1001581994
# Date:   11/18/2018

import os
import socket
from time import sleep

from portalocker import lock, LOCK_EX


def main():
    filename = 'file.txt'
    host = '127.0.0.1'
    port = 3000
    s = socket.socket()
    s.connect((host, port))
    tok = s.recv(1024)
    token = int(tok)
    if token == 0:
        print "Token not assigned"
    else:
        print "Token", token, "has been assigned to,", str(os.getpid())
        while True:
            print "requesting lock...."
	    sleep(5)
	    fil = open(filename, 'r')
            lock(fil, LOCK_EX)
            dat = fil.read()
            coun = int(dat)
            fil.close()
            if coun < 8:
                if os.path.isfile(filename):
                    sleep(0.50)
                    f = open(filename, 'r')
                    lock(f, LOCK_EX)
                    print "file opened...."
                    sleep(0.50)
                    if f.mode == 'r':
                        data = f.read()
                        print "file read...."
                        sleep(0.50)
                        count = int(data)
                        f.close()
                        f = open(filename, 'w')
                        lock(f, LOCK_EX)
                        if f.mode == 'w':
                            print "counter incremented...."
                            sleep(0.50)
                            count = count + 1
                            print "file written...."
			    print "\n"
                            sleep(0.50)
                            f.write(count.__str__())
                            f.close()
			    sleep(2)
                else:
                    print "File Does Not Exist!"
            else:
                break
        print "\n"
	print "Process terminated"
	print "\n"
# s.close()


if __name__ == '__main__':
    main()
