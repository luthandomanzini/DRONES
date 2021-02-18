# Started from Tello Template
# This Python app is in the Public domain
# Some parts from Tello3.py

import threading, socket, sys, time, subprocess


# GLOBAL VARIABLES DECLARED HERE....
host = ''
port = 9000
locaddr = (host,port)
tello_address = ('192.168.10.1', 8889) # Get the Tello drone's address



# Creates a UDP socketd
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(locaddr)


def recv():
    count = 0
    while True:
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\n****Keep Eye on Drone****\n')
            break


def sendmsg(msg, sleep = 6):
    print("Sending: " + msg)
    msg = msg.encode(encoding="utf-8")
    sock.sendto(msg, tello_address)
    time.sleep(sleep)

# recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()


# CREATE FUNCTIONS HERE....

# Drones mission through the first hula hoop
def firstHoop():
    sendmsg('up 10')
    sendmsg('forward 220')


#Drones mission through the second hula hoop
def secondHoop():
    sendmsg('go 190 0 75 75')



#Drones mission through the third Hula Hoop with a Yaw
def thirdHoopYaw():
    sendmsg('ccw 90')
    sendmsg('forward 260')
    sendmsg('ccw 90')


#Drones mission through the fourth hula hoop
def fourthHoop():
    sendmsg('forward 100')
    sendmsg('down 50')
    sendmsg('forward 250')



print("\nFirst & Last Names: Luthando Manzini")
print("Program Name: Drone Competition")
print("Date: 11/13/2020 ")
print("\n****CHECK YOUR TELLO WIFI ADDRESS****")
print("\n****CHECK SURROUNDING AREA BEFORE FLIGHT****")
ready = input('\nAre you ready to take flight: ')


try:
    if ready.lower() == 'yes':
        print("\nStarting Drone!\n")

        sendmsg('command', 0)
        sendmsg('takeoff')

        firstHoop()

        secondHoop()

        thirdHoopYaw()

        fourthHoop()

        sendmsg('land')
        print('\nGreat Flight!!!')
    else:
        print('\nMake sure you check WIFI, surroundings, co-pilot is ready, re-run program\n')
except KeyboardInterrupt:
    sendmsg('emergency')

breakr = True
sock.close()
