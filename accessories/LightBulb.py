# An Accessory for a LED attached to pin 11.
import logging
import os

from pyhap.accessory import Accessory
from pyhap.const import CATEGORY_LIGHTBULB

'''Import Unicorn HAT related libraries'''
import time
import unicornhat as unicorn

class LightBulb(Accessory):

    category = CATEGORY_LIGHTBULB

    '''@classmethod
    def _gpio_setup(_cls, pin):
        print('hi')
        #if GPIO.getmode() is None:
            #GPIO.setmode(GPIO.BOARD)
        #GPIO.setup(pin, GPIO.OUT)'''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        serv_light = self.add_preload_service('Lightbulb')
        self.char_on = serv_light.configure_char('On', setter_callback=self.set_bulb)

    def __setstate__(self, state):
        self.__dict__.update(state)

    def set_bulb(self, value):
        if value:
            print('INFO: Variable value has been set to', value)
            '''Initialize Unicorn HAT'''
            print('Initializing Unicorn HAT')
            unicorn.set_layout(unicorn.AUTO)
            unicorn.rotation(0)
            unicorn.brightness(0.5)
            width,height=unicorn.get_shape()
            for y in range(height):
                for x in range(width):
                    unicorn.set_pixel(x,y,255,255,255)
                    unicorn.show()
                    time.sleep(0.05)

        else:
            unicorn.clear()

    def stop(self):
        super().stop()
        print('Clearing Unicorn HAT...')
        unicorn.clear()
