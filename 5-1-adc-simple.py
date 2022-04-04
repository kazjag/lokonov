import RPi.GPIO as GPIO
import time
dac=[26,19,13,6,5,11,9,10]
comp=4
troyka=17
bit=8
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
def decimal2binary(n):
    return [int(bit) for bit in format(n, 'b').zfill(8)]
def adc():
    for j in range(2**bit):
        sig = decimal2binary(j)
        GPIO.output(dac, sig)
        time.sleep(0.01)
        compv=GPIO.input(comp)
        if compv==0:
            print('digvol:', j, end=' ')
            return j
try:
    while True:
        U = adc()/(2**bit)*3.3
        print('voltage:', U)
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()

