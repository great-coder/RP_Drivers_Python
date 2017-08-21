import RPi.GPIO as GPIO
import time
import threading
import sys

HAM = 22
LIGHT3 = 27


def definition():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(HAM, GPIO.IN)
    GPIO.setup(LIGHT3, GPIO.OUT)


def action2(pin):
    print("sensor detect action2!")
    GPIO.output(LIGHT3, 1)
    time.sleep(1)
    GPIO.output(LIGHT3, 0)
    return


def fun3():
    # while(True):
    # print("waiting for moisture")
    # GPIO.add_event_detect(HAM, GPIO.RISING)
    # GPIO.add_event_callback(HAM, action2)
    # GPIO.remove_event_detect(HAM)
    while GPIO.input(HAM) == 0:
        print("0")

    while GPIO.input(HAM) == 1:
        print("Water detected!!!")
        GPIO.output(LIGHT3, 1)
        time.sleep(1)
        GPIO.output(LIGHT3, 0)


def main():
    try:
        definition()
        threads = []
        t3 = threading.Thread(target=fun3)
        threads.append(t3)
        t3.start()
    except KeyboardInterrupt:
        GPIO.cleanup()


if __name__ == "__main__":
    main()
