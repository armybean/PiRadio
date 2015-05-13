#!/usr/bin/python
# coding=utf-8

import os
import RPi.GPIO as GPIO
import subprocess
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

lastValue = None
radio = None
status = None

while True:
    gpio = GPIO.input(21)

    if gpio and (lastValue is None or lastValue == 0):
        lastValue = 1
        if status is not None:
            status.terminate()
        radio = subprocess.Popen(['python', '/home/pi/PiRadio/newradio.py'])

    elif not gpio and (lastValue is None or lastValue == 1):
        lastValue = 0
        if radio is not None:
            radio.terminate()
            os.system('mpc stop')
        status = subprocess.Popen(['python', '/home/pi/PiRadio/status.py'])

    time.sleep(1)

GPIO.cleanup()