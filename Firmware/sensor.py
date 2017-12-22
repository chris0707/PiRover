import RPi.GPIO as gpio
import time


gpio.setmode(gpio.BOARD)
gpio.setup(16,gpio.OUT)
gpio.setup(18,gpio.IN)

while True:
    gpio.output(16, True)
    time.sleep(0.00001)
    gpio.output(16, False)
    
    startTime = time.time()
    stopTime = time.time()

    while gpio.input(18) == 0:
        startTime = time.time()

    while gpio.input(18) == 1:
        stopTime = time.time()

    tl = (stopTime - startTime)*17000

    #if measure == 'cm':
    distance = tl
    #elif measure == 'in':
    #    distance = tl / 0.000148
    #else:
    #    print('imroper choice')
    #    distance = None

    #gpio.cleanup()
    #return distance

    print("distance: %.1f cm" % distance)
    time.sleep(1)
