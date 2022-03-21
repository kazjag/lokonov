import RPi.GPIO as GPIO
dac=[26,19,13,6,5,11,9,10]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
def decimal2binary(n):
    return [int(bit) for bit in format(n, 'b').zfill(8)]
def check(n):
    try:
        float(n)
        return True
    except ValueError:
        return False


try:
    print('Enter the number')
    while True:
        a=input()
        if a=='q':
            break
        elif not check(a):
            print("not a number")
        else:
            if '.' in a:
                print("not an integer")
            else:
                a=int(a)
                if a<0:
                    print("not a positive")
                elif a>255:
                    print("out of range")
                else:
                    GPIO.output(dac, decimal2binary(a))
                    print("{:.4f}".format(3.3*a/256))






finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
