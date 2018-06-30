# An Accessory for a LED attached to pin 11.
import logging
import os

from pyhap.accessory import Accessory
from pyhap.const import CATEGORY_LIGHTBULB


class LightBulb(Accessory):

    category = CATEGORY_LIGHTBULB

    @classmethod
    def _gpio_setup(_cls, pin):
        print('hi')
        #if GPIO.getmode() is None:
            #GPIO.setmode(GPIO.BOARD)
        #GPIO.setup(pin, GPIO.OUT)

    def __init__(self, *args, pin=11, **kwargs):
        super().__init__(*args, **kwargs)

        serv_light = self.add_preload_service('Lightbulb')
        self.char_on = serv_light.configure_char('On', setter_callback=self.set_bulb)

        #self.pin = pin
        #self._gpio_setup(pin)

    def __setstate__(self, state):
        self.__dict__.update(state)
        #self._gpio_setup(self.pin)

    def set_bulb(self, value):
        if value:
            os.system('chmod +x /home/pi/HAP-python/unicorn.sh')
            os.system('/home/pi/HAP-python/unicorn.sh &')
            #GPIO.output(self.pin, GPIO.HIGH)
        else:
            os.system('sudo killall unicorn.sh')
            #GPIO.output(self.pin, GPIO.LOW)

    def stop(self):
        super().stop()
        #GPIO.cleanup()
