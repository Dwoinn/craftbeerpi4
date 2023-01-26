import asyncio
import logging
from os import popen
from unittest.mock import MagicMock, patch

from cbpi.api import *


logger = logging.getLogger(__name__)

command='cat /proc/cpuinfo | grep "Radxa ROCK3"'
model=popen(command).read()
if len(model) != 0:
    from cbpi.extension.gpioactor.gpio_rock3 import *
else:
    from cbpi.extension.gpioactor.gpio_rpi import *

def setup(cbpi):

    '''
    This method is called by the server during startup 
    Here you need to register your plugins at the server
    
    :param cbpi: the cbpi core 
    :return: 
    '''

    cbpi.plugin.register("GPIOActor", GPIOActor)
    cbpi.plugin.register("GPIOPWMActor", GPIOPWMActor)
