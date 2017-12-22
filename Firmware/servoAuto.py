import RPi.GPIO as gpio
import time
import sys
import Tkinter as tk
from sensorA import distance
import random

gpio.setmode(gpio.BOARD)
gpio.setup(7, gpio.OUT)
gpio.setup(11, gpio.OUT)
pwm=gpio.PWM(7,50)
pwm2=gpio.PWM(11,50)
pwm2.start(0)
pwm.start(0)


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
    pwm.ChangeDutyCycle(DC)
    DC2=1./18.*(180)+2
    pwm2.ChangeDutyCycle(DC2)
    time.sleep(tf)
    pwm.start(0)
    pwm2.start(0)

def turnLeft(tf):
    #for i in range(0,180):
        DC=1./18.*(1)+2
        pwm.ChangeDutyCycle(DC)
        pwm2.ChangeDutyCycle(DC)
        time.sleep(tf)
        pwm2.start(0)
        pwm.start(0)
        #gpio.cleanup()
        
def turnRight(tf):
        DC=1/18.*180+2
        pwm.ChangeDutyCycle(DC)
        pwm2.ChangeDutyCycle(DC)
        time.sleep(tf)
        pwm2.start(0)
        pwm.start(0)
        #gpio.cleanup()
        

'''def key_input(event):
    
    print 'Key: ', event.char
    key_press = event.char
    s = 0.030
    
    if key_press.lower()=='w':
        forward(s)
    elif key_press.lower()=='s':
        reverse(s)
    elif key_press.lower()=='a':
        turnLeft(s)
    elif key_press.lower()=='d':
        turnRight(s)


command = tk.Tk()
command.bind('<KeyPress>', key_input)
command.mainloop()
'''
def check_front():
    dist = distance()

    if dist < 15:
        print('Too close,', dist)
        
        reverse(0.4)
        turnLeft(1)
        dist = distance()
        
        if dist < 15:
            print('Too close. im done.', dist)
            sys.exit()

def autonomy():
    tf = 0.030
    x = random.randrange(0,4)

    if x==0:
        for y in range(30):
            check_front()
            forward(tf)
    elif x == 1:
        for y in range(30):
            check_front()
            forward(tf)
    elif x == 2:
        for y in range(30):
            check_front()
            forward(tf)

for z in range(10):
    autonomy()
    

