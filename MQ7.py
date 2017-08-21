import RPi.GPIO as GPIO
import time
import threading
import sys

DO = 15
LIGHT2 = 18


def definition():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(LIGHT2, GPIO.OUT)


def action(pin):
    print("Sensor detected action!")
    GPIO.output(LIGHT2, 1)
    time.sleep(1)
    GPIO.output(LIGHT2, 0)
    return


def fun2():
    while True:
        print("waiting for smoke")
        GPIO.add_event_detect(DO, GPIO.RISING)
        GPIO.add_event_callback(DO, action)
        GPIO.remove_event_detect(DO)


def main():
    try:
        definition()
        threads = []
        t2 = threading.Thread(target=fun2)
        threads.append(t2)
        t2.start()
    except KeyboardInterrupt:
        GPIO.cleanup()


if __name__ == "__main__":
    main()
