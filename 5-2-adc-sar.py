import RPi.GPIO as GPIO
import time
dac=[26,19,13,6,5,11,9,10]
comp=4
troyka=17
bit=8
bitint=[0]*bit
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
def decimal2binary(n):
    return [int(bit) for bit in format(n, 'b').zfill(8)]
def adc():
    bitint=[0]*bit
    for i in range(bit):
        bitint[i]=1
        GPIO.output(dac, bitint)
        time.sleep(0.01)
        compv=GPIO.input(comp)
        if compv==0:
            bitint[i]=0
        else:
            bitint[i]=1
    sum=0
    for m in range(bit):
        sum+=bitint[m]*(2**(bit-m-1))
    return sum

try:
    while True:
        l = adc()
        U = l/(2**bit)*3.3
        print('digvol', l, '; ','voltage:', U)
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()