CSE5306-002, Distributed Systems Fall 2018
Project 2
I have neither given or received unauthorized assistance on this work
Signed: 1. Deepit Raj Sapru 1001522895
        2. Ravi Chandra Kumar Venkatesh 1001581994
Date:   11/18/2018

Assignment-3 (Implement a locking scheme to protect a share file in your distributed system):
===============================================================
Files:
1. Server.py
2. Client.py

IDE used: PyCharm
Packages used: socket, threading, os, time, portalocker

Instructions to run:
====================

    1. extract all the files from Assignment 3.
    2. then, compile them using the cmd: python <filename>.py
    3. then, first start the server using the command: python server.py
    4. and then the client, command: python client.py
    
    Note: You may run multiple clients, by opening separate CMDs & repeating step 4. Also, there is a batch file, i.e. main.bat for possible simultaneous execution. 
    Makes use of centralized locking scheme, where server issues tokens to the processes.  Assume that all processes keep requesting the lock until successfully acquiring the lock for a predefined number of 
    times, i.e. 4 times each assuming we have 2 concurrent processes.
