import RPi.GPIO as GPIO
import time
dac=[26,19,13,6,5,11,9,10]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
def decimal2binary(n):
    return [int(bit) for bit in format(n, 'b').zfill(8)]
try:
    per=float(input())
    a=0
    i=1
    while True:
        GPIO.output(dac, decimal2binary(a))
        time.sleep(per/512)
        a+=i
        if a==256:
            i=-1
            a+=i
        elif a==0:
            i=1
            a+=i

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
