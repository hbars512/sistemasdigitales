import pyfirmata
import time
from app import board
from app import db
from app.models import User, Casa, Led, Sensor

it = pyfirmata.util.Iterator(board)
it.start()

board.digital[7].mode = pyfirmata.INPUT
PIEZO_PIN = board.get_pin('d:6:p')

while True:
    sw = board.digital[7].read()

    if sw is True:
        PIEZO_PIN.write(0.2)
        time.sleep(2)
    else:
        PIEZO_PIN.write(0)
        time.sleep(2)
