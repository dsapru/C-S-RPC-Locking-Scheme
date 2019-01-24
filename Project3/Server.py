# I have neither given or received unauthorized assistance on this work
# Signed: 1. Deepit Raj Sapru 1001522895
#         2. Ravi Chandra Kumar Venkatesh 1001581994
# Date:   11/18/2018

import socket
import threading
import os

dirname = os.path.dirname(__file__)
tokens = 'tokens.txt'


def Tokenizer(name, sock):
    f = open(tokens, 'r')
    data = f.read()
    f.close()
    has_token = int(data)
    has_token = has_token + 1
    sock.send(has_token.__str__())
    f = open(tokens, 'w')
    f.write(has_token.__str__())
    f.close()

def main():
    host = '127.0.0.1'
    port = 3000

    s = socket.socket()
    s.bind((host, port))

    s.listen(5)

    print "Server Started."
    while True:
        c, addr = s.accept()
        print "process connected ip:<" + str(addr) + ">"
        t1 = threading.Thread(target=Tokenizer, args=("RetrThread1", c))
        t1.start()
        # s.close()


if __name__ == '__main__':
    main()
