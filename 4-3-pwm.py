import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup([23, 21], GPIO.OUT)
GPIO.setup(3, GPIO.IN)
p = GPIO.PWM(23, 1000)
p.start(0)
try:
    print("koef?")
    while True:
        k=float(input())
        p.ChangeDutyCycle(k)
        print('voltage:', "{:.4f}".format(3.3*k/100))
        
finally:
    p.stop()
    GPIO.cleanup()