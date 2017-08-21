import RPi.GPIO as GPIO
import time
import threading
import sys

TRIG = 23
ECHO = 24
LIGHT1 = 17


def definition():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ECHO, GPIO.IN)
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(LIGHT1, GPIO.OUT)


def fun1():
    while True:
        GPIO.output(TRIG, False)
        print("Waiting For Sensor To Settle")
        time.sleep(2)
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
        while GPIO.input(ECHO) == 0:
            pulse_start = time.time()
        while GPIO.input(ECHO) == 1:
            pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)
        if 2 < distance < 50:
            print
            "Distance:", distance - 0.5, "cm"
            GPIO.output(LIGHT1, 1)
            time.sleep(1)
            GPIO.output(LIGHT1, 0)
        else:
            print("Out Of Range")


def main():
    try:
        definition()
        threads = []
        t = threading.Thread(target=fun1)
        threads.append(t)
        t.start()
    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
