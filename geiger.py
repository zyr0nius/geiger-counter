#!/usr/bin/env python3

import os
import threading
import time
from datetime import datetime, timedelta

# import RPi.GPIO as gpio
import ASUS.GPIO as gpio
from prometheus_client import Counter, Gauge, start_http_server

gpio.setwarnings(False)
os.system("clear")

# total_count_metric = Counter("total_count", "Total count of events")
# value_per_hour_metric = Gauge("value_per_hour", "Value per hour in Sv/h")
# counter_metric = Gauge("counter", "Count per minute")

# def impulse(channel):
# global total_count
# global counter
# global timer
# timer.append(datetime.now())
# total_count += 1
# counter += 1


# def init():
# global total_count
# global counter
# global timer
# global total_count_metric
# global value_per_hour_metric
# global counter_metric

# gpio_pin = 7
# total_count = 0
# counter = 0
# timer = []
# gpio.setmode(gpio.BOARD)
# gpio.setup(gpio_pin, gpio.IN)
# gpio.add_event_detect(gpio_pin, gpio.FALLING)
# gpio.add_event_callback(gpio_pin, impulse)
# start_http_server(8000)
# threading.Thread(target=update_prometheus_metrics).start()


# def update_prometheus_metrics():
#     while True:
#         value_per_hour = round(counter / 151, 5)
#         total_count_metric.inc(total_count)
#         counter_metric.set(counter)
#         value_per_hour_metric.set(value_per_hour)
#         time.sleep(60)


# def main():
#     # global counter
#     # global timer
#     init()

#     try:
#         while True:
#             for i in timer:
#                 if i + timedelta(seconds=60) < datetime.now():
#                     timer.pop(0)
#                     counter -= 1
#             value_per_hour = round(counter / 151, 5)
#             print(
#                 f"Current value:{value_per_hour}\u00b5Sv/h Counter:{counter} Total Count:{total_count}",
#                 end="\r",
#             )
#             time.sleep(1)
#     except KeyboardInterrupt:
#         gpio.cleanup()


class Geiger(object):
    def __init__(self, total_count=0, counter=0, timer=[]):
        self.total_count = total_count
        self.counter = counter
        self.timer = timer

        self.gpio_pin = 7
        self.total_count_metric = Counter("total_count", "Total count of events")
        self.value_per_hour_metric = Gauge("value_per_hour", "Value per hour in Sv/h")
        self.counter_metric = Gauge("counter", "Count per minute")

        gpio.set_mode(gpio.BOARD)
        gpio.setup(self.gpio_pin, gpio.IN)
        gpio.add_event_detect(self.gpio_pin, gpio.FALLING)
        gpio.add_event_callback(self.gpio_pin, self.__impulse)
        start_http_server(8000)
        threading.Thread(target=self.__update_prometheus_metrics).start()

    def __implulse(self, channel):
        self.timer.append(datetime.now())
        self.total_count += 1
        self.counter += 1

    def __update_prometheus_metrics(self):
        while True:
            self.total_count_metric.inc(self.total_count)
            self.counter_metric.set(self.counter)
            value_per_hour = round(self.counter / 151, 5)
            self.value_per_hour_metric.set(value_per_hour)
            time.sleep(60)

    def main_loop(self):
        try:
            while True:
                for i in self.timer:
                    if i + timedelta(seconds=60) < datetime.now():
                        self.timer.pop(0)
                        self.counter -= 1
                value_per_hour = round(self.counter / 151, 5)
                print(
                    f"Current value:{value_per_hour}\u00b5Sv/h Counter:{self.counter} Total Count:{self.total_count}",
                    end="\r",
                )
                time.sleep(1)
        except KeyboardInterrupt:
            gpio.cleanup()


def main():
    geiger = Geiger()
    geiger.main_loop()


if __name__ == "__main__":
    main()
