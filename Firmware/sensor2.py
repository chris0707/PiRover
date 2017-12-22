import RPi.GPIO as gpio
import time
import signal
import sys

gpio.setmode(gpio.BOARD)

pinTrigger = 12
pinEcho = 18

def close(signal, frame):
    print("\nturning off sensor\n")
    gpio.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, close)

gpio.setup(pinTrigger, gpio.OUT)
gpio.setup(pinEcho, gpio.IN)

while True:
        gpio.output(pinTrigger, True)
        time.sleep(0.00001)
        gpio.output(pinTrigger, False)

        startTime = time.time()
        stopTime = time.time()

        while 0 == gpio.input(pinEcho):
                startTime = time.time()

        while 1 == gpio.input(pinEcho):
                stopTime = time.time()

        TimeElapsed = stopTime - startTime
        distance = (TimeElapsed * 34300) / 2
        #distance = (TimeElapsed * 17000) 
        print("Distance: %.1f cm" % distance)
        time.sleep(1)
