#!/usr/bin/python
# coding=utf-8

import atexit
import time
from dot3k import backlight, joystick
from myradio import Radio

radio = Radio()


def clean_shutdown():
    radio.off()


atexit.register(clean_shutdown)

REPEAT_DELAY = 0.5


@joystick.on(joystick.UP)
def handle_up(pin):
    radio.up()


@joystick.on(joystick.DOWN)
def handle_down(pin):
    radio.down()


@joystick.on(joystick.LEFT)
def handle_left(pin):
    radio.left()


@joystick.on(joystick.RIGHT)
def handle_right(pin):
    radio.right()


# @joystick.on(joystick.BUTTON)
# def handle_button(pin):


backlight.left_rgb(255, 0, 0)
backlight.mid_rgb(255, 0, 255)
backlight.right_rgb(0, 0, 255)

while True:
    radio.redraw()
    time.sleep(0.2)
