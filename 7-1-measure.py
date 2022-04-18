import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt
GPIO.setmode(GPIO.BCM)
dac=[26,19,13,6,5,11,9,10]
leds=[21,20,16,12,7,8,25,24]
comp=4
troyka=17
bit=8
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
voltage=0
arr_binary=[0]*bit
measurement=[]
t_0=time.time()
def read_voltage():
    voltage = GPIO.input()
    bitint = [0] * bit
    for i in range(bit):
        bitint[i] = 1
        GPIO.output(dac, bitint)
        time.sleep(0.01)
        compv = GPIO.input(comp)
        if compv == 0:
            bitint[i] = 0
        else:
            bitint[i] = 1
    sum = 0
    for m in range(bit):
        sum += bitint[m] * (2 ** (bit - m - 1))
    U = sum / (2 ** bit) * 3.3
    return U, bitint

def binary_out(arr_binary):
    GPIO.output(leds, arr_binary)

try:
    GPIO.output(troyka, 1)
    print("Starting flow in...")
    while voltage < 3.20:
        voltage, arr_binary=read_voltage()
        GPIO.output(leds, arr_binary)
        measurement.append(voltage)
    print("Starting flow out...")
    while voltage > 0.07:
        voltage, arr_binary=read_voltage()
        GPIO.output(leds, arr_binary)
        measurement.append(voltage)
    t_1 = time.time()
    print("Saving time...")
    print("Creating the plot...")
    plt.plot(measurement)
    print("Saving data...")
    T=(t_1 - t_0) / len(measurement)
    measurement_str=[str(item) for item in measurement]
    with open("data.txt", "w") as out_0:
        out_0.write("\n".join(measurement_str))
    with open("settings.txt", "w") as out:
        out.write("discretization frequency: ")
        out.write(str(1/T))
        out.write(" q_step: ")
        out.write(str(3.3/255))
    print("Experiment data:")
    print("Exp. time:", t_1-t_0, "secs")
    print("Period:", T)
    print("Frequency:", 1/T)
    print("q step:", 3.3/255)
finally:
    GPIO.output(leds, 0)
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()











