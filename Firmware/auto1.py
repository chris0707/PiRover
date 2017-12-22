import RPi.GPIO as gpio
import time
import sys
import Tkinter as tk
from bluetooth import*
import os
import random



gpio.setmode(gpio.BOARD)
gpio.setup(7, gpio.OUT)
gpio.setup(11, gpio.OUT)
pwm = gpio.PWM(7,50)
pwm2 = gpio.PWM(11,50)
pwm.start(0)
pwm2.start(0)

def forward(tf):
    DC=1./18.*(1)+2
    DC2=1./18.*(180)+2
    pwm.ChangeDutyCycle(DC2)
    pwm2.ChangeDutyCycle(DC)    
    time.sleep(tf) 
    pwm.start(0)
    pwm2.start(0)

def reverse(tf):
    DC=1./18.*(1)+2
    DC2=1./18.*(180)+2
    pwm.ChangeDutyCycle(DC)
    pwm2.ChangeDutyCycle(DC2)
    time.sleep(tf)
    pwm.start(0)
    pwm2.start(0)

def turnLeft(tf):
    
    DC=1./18.*(1)+2
    pwm.ChangeDutyCycle(DC)
    pwm2.ChangeDutyCycle(DC)
    time.sleep(tf)
    pwm.start(0)
    pwm2.start(0)

def turnRight(tf):
    
    DC=1./18.*(180)+2
    pwm.ChangeDutyCycle(DC)
    pwm2.ChangeDutyCycle(DC)
    time.sleep(tf)
    pwm.start(0)
    pwm2.start(0)

def stop():
    time.sleep(1)
    gpio.cleanup()

def check_front():
    dist = distance()

    if dist<15:
        print('Too close,', dist)

        reverse(1)
        turnLeft(1)
        
        if dist < 15:
            print("Alright... that's too close. Im done", dist)
            sys.exit()

def autonomy():
    tf = 0.030
    x = random.randrange(0,4)

    if x==0:
        for y in range(30):
            check_front()
            froward(tf)

    elif x==1:
        for y in range(30):
            check_front()
            forward(tf)
    elif x==2:
        for y in range(30):
            check_front()
            forward(tf)
        



server_sock = BluetoothSocket( RFCOMM )
server_sock.bind(("",PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

uuid = ("00001101-0000-1000-8000-00805f9b34fb");

advertise_service(server_sock, "SampleServer",
        service_id = uuid,
        service_classes = [ uuid, SERIAL_PORT_CLASS ],
        profiles = [ SERIAL_PORT_PROFILE ],
     #   protocols = [ OBEX_UUID ]
        )
print("Waiting for connection on RFCOMM channel %d" % port)

client_sock, client_info = server_sock.accept()
print("Accepted connection from ", client_info)

try:
    while True:
        data = client_sock.recv(1024)
        sleep = 0.030

        if data =='w':
            print("moving forward")
            forward(sleep)
        
        elif data == 's':
            print("moving backwards")
            reverse(sleep)

        elif data == 'a':
            print("turning left")
            turnLeft(sleep)

        elif data == 'd':
            print("turning right")
            turnRight(sleep)

        elif data == 'automap':
            print("auto mapping")
            for z in range(10):
                autonomy()

        
        elif data == 'stop':
            print("stopping")
            stop()
            

            
except IOError:
    pass

print("Disconnected")

client_sock.close()
server_sock.close()
print("Done")
