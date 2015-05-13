#!/usr/bin/python
# coding=utf-8

import atexit
import fcntl
import socket
import struct
import time
from dot3k import backlight, lcd


def clean_shutdown():
    backlight.set_graph(0)
    backlight.rgb(0, 0, 0)
    lcd.clear()


# read current ip address for a given interface
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', ifname[:15]))[20:24])


atexit.register(clean_shutdown)

backlight.set_graph(0)
backlight.rgb(0, 0, 0)

while True:
    ip = 'Kein WLAN :('
    try:
        ip = get_ip_address('wlan0')
    except IOError:
        pass

    lcd.clear()
    lcd.set_cursor_position(0, 0)
    lcd.write('BathPi - PiRadio')

    lcd.set_cursor_position(0, 1)
    lcd.write('Standby...')

    lcd.set_cursor_position(0, 2)
    lcd.write(ip)

    time.sleep(1)
