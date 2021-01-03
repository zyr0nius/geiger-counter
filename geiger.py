#!/usr/bin/env python3

from datetime import datetime, timedelta
import RPi.GPIO as gpio
import time

def impulse(channel):
    """
    Is called when event is triggered. Increments the counters by 1
    and adds a timestamp to a list.
    """

    global total_count
    global counter
    global timer

    timer.append(datetime.now())
    total_count += 1
    counter += 1

def init():
    '''
    Initialises the counters, the list with timestamps and
    gpio for usage.
    '''

    global total_count
    global counter
    global timer

    gpio_pin = 0
    total_count = 0
    counter = 0
    timer = []

    # use pin layout of rasberry pi and set pin as input
    gpio.setmode(gpio.BOARD)
    gpio.setup(gpio_pin, gpio.IN)
    # trigger event when signal on pin is falling
    gpio.add_event_detect(gpio_pin, gpio.FALLING)
    gpio.add_event_callback(gpio_pin, impulse)

def main():
    """
    Checks continually if a timestamp is older than 60 s, removes
    those timestamps from the list and decrements the counter. This
    ensures that only impulses are counted which are within the last minute.
    Computes from the number of impulses the value in microsievert per hour.
    """

    global counter
    global timer

    init()

    try:
        while True:
            for i in timer:
                if i + timedelta(seconds=60) < datetime.now():
                    timer.pop(0)
                    counter -= 1
            
            # The value 151 is not just some random value. You can find
            # it in the documentation of 'RaditionD-v1.1(CAJOE)'
            value_per_hour = round(counter / 151, 3)

            # print("Total count: {}".format(total_count), end='\r')
            print("Current value: {} \u00b5Sv/h".format(value_per_hour), end='\r')
            time.sleep(1)

    # end the program properly when CTRL+C is pressed
    except KeyboardInterrupt:
        gpio.cleanup()


if __name__ == "__main__":
    main()
