import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)

trig = 12
echo = 18

gpio.setup(trig, gpio.OUT)
gpio.output(trig, 0)

gpio.setup(echo, gpio.IN)
time.sleep(0.1)

print "Starting measurements..."

gpio.output(trig,1)
time.sleep(0.00001)
gpio.output(trig,0)

while gpio.input(echo) == 0:
    pass
start = time.time()

while gpio.input(echo) == 1:
    pass
stop = time.time()

print(stop - start) * 17000

gpio.cleanup()

