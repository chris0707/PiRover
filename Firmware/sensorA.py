import RPi.GPIO as gpio
import time

def distance(measure='cm'):
    gpio.setmode(gpio.BOARD)
    gpio.setup(16,gpio.OUT)
    gpio.setup(18,gpio.IN)

#while True:
    gpio.output(16, True)
    time.sleep(0.00001)
    gpio.output(16, False)
    
    startTime = time.time()
    stopTime = time.time()

    while gpio.input(18) == 0:
        startTime = time.time()

    while gpio.input(18) == 1:
        stopTime = time.time()

    distance = (stopTime - startTime)*17000

    
    return distance

    print("distance: %.1f cm" % distance)
    #time.sleep(1)
