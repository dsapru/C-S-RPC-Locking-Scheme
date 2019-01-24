# I have neither given or received unauthorized assistance on this work
# Signed: 1. Deepit Raj Sapru 1001522895
#         2. Ravi Chandra Kumar Venkatesh 1001581994
# Date:   10/06/2018

import socket
import threading
import os
from time import sleep

dict = {}
dirname = os.path.dirname(__file__)


def RetrFile(name, sock):
    filename = sock.recv(1024)
    # print filename
    if os.path.isfile(filename):
        sock.send("EXISTS " + str(os.path.getsize(filename)))
        userResponse = sock.recv(1024)
        if userResponse[:4] == 'Down':
            file = os.path.basename(filename)
            if file in dict:
                value = dict.get(file)
                if value == "unlocked":
                    with open(filename, 'rb') as f:
                        bytesToSend = f.read(1024)
                        sock.send(bytesToSend)
                        while bytesToSend != "":
                            bytesToSend = f.read(1024)
                            sock.send(bytesToSend)
                else:
                    print "file cannot be downloaded as it is locked"
            else:
                print "File does not exist"

        if userResponse[:2] == 'Up':
            upload(sock, filename)

        if userResponse[:3] == 'Del':
            os.remove(filename)
            print "File Deleted"

        if userResponse[:6] == 'Rename':
            rename(sock, filename)
            print "File Renamed"
    else:
        sock.send("ERR")


# @synchronized
def upload(sock, filename):
    filesize = os.path.getsize(filename)
    file = os.path.basename(filename)
    serverfile = os.path.join(dirname, "Serverfiles\\")
    os.chdir(serverfile)
    if file in dict:
        value = dict.get(file)
    else:
        dict[file] = "unlocked"
        value = "unlocked"
    if value == "unlocked":
            dict[file] = "locked"
            f = open('new_' + file, 'wb')
            data = sock.recv(1024)
            f.write(data)
            totalRecv = len(data)
            while totalRecv < filesize:
                data = sock.recv(1024)
                totalRecv += len(data)
                f.write(data)
                print "{0:.2f}".format((totalRecv / float(filesize)) * 100) + "% Done"
            f.close()
            print "Server Download Complete!"
            dict[file] = "unlocked"
    else:
            print "File cannot be uploaded"

def rename(sock, filename):
    file = os.path.basename(filename)
    print dict
    if file in dict:
        value = dict.get(file)

        if value == "unlocked":
            dict[file] = "locked"
            newfile = sock.recv(1024)
            base = os.path.dirname(filename)
            print base
            sleep(10)
            new = os.path.join(base, newfile)
            os.rename(filename, new)
            print "File renamed"
            dict[newfile] = "unlocked"
        else:
            print("Can not rename file because it is locked")
    else:
        print ("Can not rename file because it is not present")


def Main():
    serverfile = os.path.join(dirname, "Serverfiles\\")
    for filename in os.listdir(serverfile):
        dict[filename] = "unlocked"
    print dict
    host = '127.0.0.1'
    port = 3000

    s = socket.socket()
    s.bind((host, port))

    s.listen(5)

    print "Server Started."
    while True:
        c, addr = s.accept()
        print "client connected ip:<" + str(addr) + ">"

        t1 = threading.Thread(target=RetrFile, args=("RetrThread1", c))
        # t2 = threading.Thread(target=RetrFile, args=("RetrThread2", c))
        # t1.run()
        # t2.run()

        t1.start()
        # t2.start()
        # s.close()


if __name__ == '__main__':
    Main()
