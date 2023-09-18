
#!/usr/bin/env python3

from datetime import datetime, timedelta
from prometheus_client import start_http_server, Counter, Gauge
# import RPi.GPIO as gpio
import ASUS.GPIO as gpio
import time
import os
import threading

gpio.setwarnings(False)
os.system("clear")

total_count_metric=Counter("total_count","Total count of events")
value_per_hour_metric=Gauge("value_per_hour","Value per hour in Sv/h")
counter_metric=Gauge("counter","Count per minute")

def impulse(channel):
    global total_count
    global counter
    global timer
    timer.append(datetime.now())
    total_count += 1
    counter += 1

def init():
    global total_count
    global counter
    global timer
    global total_count_metric
    global value_per_hour_metric
    global counter_metric
    gpio_pin=7
    total_count=0
    counter=0
    timer=[]
    gpio.setmode(gpio.BOARD)
    gpio.setup(gpio_pin, gpio.IN)
    gpio.add_event_detect(gpio_pin,gpio.FALLING)
    gpio.add_event_callback(gpio_pin,impulse)
    start_http_server(8000)
    threading.Thread(target=update_prometheus_metrics).start()

def update_prometheus_metrics():
    while True:
        value_per_hour=round(counter/151,5)
        total_count_metric.inc(total_count)
        counter_metric.set(counter)
        value_per_hour_metric.set(value_per_hour)
        time.sleep(60)

def main():
    global counter
    global timer
    init()
    try:
        while True:
            for i in timer:
                if i + timedelta(seconds=60) < datetime.now():
                    timer.pop(0)
                    counter -= 1
            value_per_hour=round(counter/151,5)
            print(f"Current value:{value_per_hour}\u00b5Sv/h Counter:{counter} Total Count:{total_count}",end='\r')
            time.sleep(1)
    except KeyboardInterrupt:
        gpio.cleanup()

if __name__ == "__main__":
    main()
