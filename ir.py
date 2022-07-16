from numpy import outer
import RPi.GPIO as GPIO
import time

pin0 = 0  # pin for input
pin1 = 0  # pin for output

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin0, GPIO.IN)
GPIO.setup(pin1, GPIO.OUT)
counter = 0


def counterplus(channel):
    global counter
    if GPIO.input(channel) > 5:
        counter += 1
    else:
        counter += 0


GPIO.add_event_delect(pin0, GPIO.RISING, callback=counterplus, bouncetime=3)
GPIO.output(pin1, True)
time.sleep(1)
for x in range(0, 500)
print("coint : ", counter)
time.sleep(10)

GPIO.cleamup()
print("bruh")
