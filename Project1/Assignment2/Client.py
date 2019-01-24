# I have neither given or received unauthorized assistance on this work
# Signed: 1. Deepit Raj Sapru 1001522895
#         2. Ravi Chandra Kumar Venkatesh 1001581994
# Date:   10/06/2018

import os
import socket


def Main():
    global filename
    host = '127.0.0.1'
    port = 3000

    s = socket.socket()
    s.connect((host, port))
    file = raw_input("Enter the filename? -> ")
    choice = raw_input("File on Server or Client(S/C)?")
    dirname = os.path.dirname(__file__)
    if choice == 'S':
        serverfile = os.path.join(dirname, "Serverfiles\\")
        filename = os.path.join(serverfile, file)
        print filename
    if choice == 'C':
        clientfile = os.path.join(dirname, "Clientfiles\\")
        filename = os.path.join(clientfile, file)
        print filename
    if filename != 'q':
        s.send(filename)
        data = s.recv(1024)
        if data[:6] == 'EXISTS':
            filesize = long(data[6:])
            message = raw_input(
                "File exists, " + str(filesize) + "Bytes, 1. Download 2. Upload 3. Delete 4. Rename? -> ")
            if message == '1':
                s.send("Down")
                clientfile1 = os.path.join(dirname, "Clientfiles\\")
                os.chdir(clientfile1)
                f = open('new_' + file, 'wb')
                data = s.recv(1024)
                totalRecv = len(data)
                f.write(data)
                while totalRecv < filesize:
                    data = s.recv(1024)
                    totalRecv += len(data)
                    f.write(data)
                    print "{0:.2f}".format((totalRecv / float(filesize)) * 100) + "% Done"
                print "Download Complete!"
                f.close()
            if message == '2':
                s.send("Up")
                clientfile1 = os.path.join(dirname, "Clientfiles\\")
                os.chdir(clientfile1)
                with open(filename, 'rb') as f:
                    bytesToSend = f.read(1024)
                    s.send(bytesToSend)
                    while bytesToSend != "":
                        bytesToSend = f.read(1024)
                        s.send(bytesToSend)
                print "Upload Complete!"
                f.close()
            if message == '3':
                s.send("Del")
                print "File Deleted"
            if message == '4':
                s.send("Rename")
                newfile = raw_input("Enter the file to rename:")
                s.send(newfile)
                # data = s.recv(1024)
                # print data
                print "File Renamed"
    else:
        print "File Does Not Exist!"

    # s.close()


if __name__ == '__main__':
    Main()
