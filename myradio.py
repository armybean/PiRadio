import os
import psutil
import subprocess
import time
from dot3k import backlight, lcd


class Radio():
    def __init__(self):
        self.channelLink = ["http://radiolausitz.mp3.green.ch:80",
                            "http://c22033-ls.i.core.cdn.streamfarm.net/T3R6XGogC9922033/22033mdr/live/app2128740352/w2128904194/live_de_128.mp3",
                            "http://c22033-ls.i.core.cdn.streamfarm.net/UjIe753Ui9922033/22033mdr/live/app2128740352/w2128904195/live_de_128.mp3",
                            "http://tuner.radiopaloma.de:80",
                            "http://stream.hoerradar.de/sunshinelive-mp3-192",
                            "http://rbb-mp3-fritz-m.akacast.akamaistream.net/7/799/292093/v1/gnl.akacast.akamaistream.net/rbb_mp3_fritz_m"]
        self.channelName = ["Radio Lausitz", "MDR Jump", "MDR Sputnik", "Radio Paloma", "Sunshine Live", "Fritz"]
        self.selected_station = 0
        self.start()

    def redraw(self):
        volume = subprocess.check_output("mpc status | grep volume", shell=True, stderr=subprocess.STDOUT)
        volume = volume[7:volume.find("%")]

        lcd.clear()
        lcd.set_cursor_position(0, 0)
        lcd.write(self.channelName[self.selected_station])

        lcd.set_cursor_position(0, 1)
        lcd.write(time.strftime("%d.%m. %H:%M:%S"))

        lcd.set_cursor_position(0, 2)
        lcd.write('Volume:' + volume + ' %')

        cpu = psutil.cpu_percent()
        backlight.set_graph(float(cpu) / 100.0)

    def create_playlist(self):
        os.system("sudo mpc clear")

        for channel in self.channelLink:
            os.system("mpc add " + channel)

    def start(self):
        self.create_playlist()
        os.system('mpc play 1')

    def up(self):
        os.system('mpc volume +5')

    def down(self):
        os.system('mpc volume -5')

    def right(self):
        self.selected_station += 1
        if self.selected_station >= len(self.channelLink):
            self.selected_station = 0
        self.play_selected_station()

    def left(self):
        self.selected_station -= 1
        if self.selected_station < 0:
            self.selected_station = len(self.channelLink) - 1
        self.play_selected_station()

    def play_selected_station(self):
        os.system('mpc play ' + str(self.selected_station + 1))

    def off(self):
        os.system('mpc stop')
        backlight.set_graph(0)
        backlight.rgb(0, 0, 0)
        lcd.clear()