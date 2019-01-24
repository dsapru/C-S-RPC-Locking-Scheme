# I have neither given or received unauthorized assistance on this work
# Signed: 1. Deepit Raj Sapru 1001522895
#         2. Ravi Chandra Kumar Venkatesh 1001581994
# Date:   10/06/2018


import socket
import threading
import os


def RetrFile(name, sock):
    dirname = os.path.dirname(__file__)
    filename = sock.recv(1024)
    if os.path.isfile(filename):
        sock.send("EXISTS " + str(os.path.getsize(filename)))
        userResponse = sock.recv(1024)
        if userResponse[:4] == 'Down':
            with open(filename, 'rb') as f:
                bytesToSend = f.read(1024)
                sock.send(bytesToSend)
                while bytesToSend != "":
                    bytesToSend = f.read(1024)
                    sock.send(bytesToSend)
        if userResponse[:2] == 'Up':
            filesize = os.path.getsize(filename)
            print filesize
            file = os.path.basename(filename)
            serverfile = os.path.join(dirname, "Serverfiles\\")
            # serverfilename = os.path.join(serverfile, file)
            os.chdir(serverfile)
            # os.chdir("C:\\Users\\Deepit Sapru\\PycharmProjects\\Project1\\Serverfiles")
            # print file
            f = open('new_' + file, 'wb')
            data = sock.recv(1024)
            f.write(data)
            totalRecv = len(data)
            while totalRecv < filesize:
                data = sock.recv(1024)
                totalRecv += len(data)
                f.write(data)
                print "{0:.2f}".format((totalRecv / float(filesize)) * 100) + "% Done"
            print "Server Download Complete!"
            # f.close()

    else:
        sock.send("ERR ")

    sock.close()


def Main():
    host = '127.0.0.1'
    port = 5001

    s = socket.socket()
    s.bind((host, port))

    s.listen(5)

    print "Server Started."
    while True:
        c, addr = s.accept()
        print "client connected ip:<" + str(addr) + ">"
        t = threading.Thread(target=RetrFile, args=("RetrThread", c))
        t.start()
        s.close()


if __name__ == '__main__':
    Main()
