import pyfirmata
import time
from app import board
from app import db
from app.models import User, Casa, Led, Sensor

it = pyfirmata.util.Iterator(board)
it.start()

board.digital[8].mode = pyfirmata.INPUT     # Sensor casa 1
# board.digital[4].mode = pyfirmata.INPUT     # Sensor casa 2
board.digital[3].mode = pyfirmata.INPUT     # Sensor casa 3
board.digital[7].mode = pyfirmata.INPUT     # Sensor casa 4
PIEZO_PIN = board.get_pin('d:6:p')          # Buzzer derecho
PIEZO_PIN2 = board.get_pin('d:5:p')         # Buzzer izquierdo

while True:
    sw1 = board.digital[8].read()
    # sw2 = board.digital[4].read()
    sw2 = False
    sw3 = board.digital[3].read()
    sw4 = board.digital[7].read()

    if sw1 is True:
        if sw2 is True:
            if sw3 is True:
                if sw4 is True:
                    board.digital[12].write(1)      # Led casa 1
                    # board.digital[11].write(1)      # Led casa 2
                    board.digital[11].write(0)      # Led casa 2
                    board.digital[10].write(1)      # Led casa 3
                    board.digital[9].write(1)       # Led casa 4
                    PIEZO_PIN.write(0.2)            # sensor derecho
                    PIEZO_PIN2.write(0.2)           # sensor izquierdo
                    time.sleep(3)
                else:
                    board.digital[12].write(1)      # Led casa 1
                    # board.digital[11].write(1)      # Led casa 2
                    board.digital[11].write(0)      # Led casa 2
                    board.digital[10].write(1)      # Led casa 3
                    board.digital[9].write(0)       # Led casa 4 OFF
                    PIEZO_PIN.write(0.2)            # sensor derecho
                    PIEZO_PIN2.write(0)             # sensor izquierdo
                    time.sleep(3)
            else:
                if sw4 is True:
                    board.digital[12].write(1)      # Led casa 1
                    # board.digital[11].write(1)      # Led casa 2
                    board.digital[11].write(0)      # Led casa 2
                    board.digital[10].write(0)      # Led casa 3 OFF
                    board.digital[9].write(1)       # Led casa 4
                    PIEZO_PIN.write(0.2)            # sensor derecho
                    PIEZO_PIN2.write(0.2)           # sensor izquierdo
                    time.sleep(3)
                else:
                    board.digital[12].write(1)      # Led casa 1
                    # board.digital[11].write(1)      # Led casa 2
                    board.digital[11].write(0)      # Led casa 2
                    board.digital[10].write(0)      # Led casa 3 OFF
                    board.digital[9].write(0)       # Led casa 4 OFF
                    PIEZO_PIN.write(0.2)            # sensor derecho
                    PIEZO_PIN2.write(0)             # sensor izquierdo
                    time.sleep(3)
        else:
            if sw3 is True:
                if sw4 is True:
                    board.digital[12].write(1)      # Led casa 1
                    board.digital[11].write(0)      # Led casa 2 OFF
                    board.digital[10].write(1)      # Led casa 3
                    board.digital[9].write(1)       # Led casa 4
                    PIEZO_PIN.write(0.2)            # sensor derecho
                    PIEZO_PIN2.write(0.2)           # sensor izquierdo
                    time.sleep(3)
                else:
                    board.digital[12].write(1)      # Led casa 1
                    board.digital[11].write(0)      # Led casa 2 OFF
                    board.digital[10].write(1)      # Led casa 3
                    board.digital[9].write(0)       # Led casa 4 OFF
                    PIEZO_PIN.write(0)              # sensor derecho
                    PIEZO_PIN2.write(0.2)           # sensor izquierdo
                    time.sleep(3)
            else:
                if sw4 is True:
                    board.digital[12].write(1)      # Led casa 1
                    board.digital[11].write(0)      # Led casa 2 OFF
                    board.digital[10].write(0)      # Led casa 3 OFF
                    board.digital[9].write(1)       # Led casa 4
                    PIEZO_PIN.write(0.2)            # sensor derecho
                    PIEZO_PIN2.write(0.2)           # sensor izquierdo
                    time.sleep(3)
                else:
                    board.digital[12].write(1)      # Led casa 1
                    board.digital[11].write(0)      # Led casa 2 OFF
                    board.digital[10].write(0)      # Led casa 3 OFF
                    board.digital[9].write(0)       # Led casa 4 OFF
                    PIEZO_PIN.write(0.2)            # sensor derecho
                    PIEZO_PIN2.write(0)             # sensor izquierdo
                    time.sleep(3)
    else:
        if sw2 is True:
            if sw3 is True:
                if sw4 is True:
                    board.digital[12].write(0)      # Led casa 1 OFF
                    # board.digital[11].write(1)      # Led casa 2
                    board.digital[11].write(0)      # Led casa 2
                    board.digital[10].write(1)      # Led casa 3
                    board.digital[9].write(1)       # Led casa 4
                    PIEZO_PIN.write(0.2)            # sensor derecho
                    PIEZO_PIN2.write(0.2)           # sensor izquierdo
                    time.sleep(3)
                else:
                    board.digital[12].write(0)      # Led casa 1 OFF
                    # board.digital[11].write(1)      # Led casa 2
                    board.digital[11].write(0)      # Led casa 2
                    board.digital[10].write(1)      # Led casa 3
                    board.digital[9].write(0)       # Led casa 4 OFF
                    PIEZO_PIN.write(0)              # sensor derecho
                    PIEZO_PIN2.write(0.2)           # sensor izquierdo
                    time.sleep(3)
            else:
                if sw4 is True:
                    board.digital[12].write(0)      # Led casa 1 OFF
                    # board.digital[11].write(1)      # Led casa 2
                    board.digital[11].write(0)      # Led casa 2
                    board.digital[10].write(0)      # Led casa 3 OFF
                    board.digital[9].write(1)       # Led casa 4
                    PIEZO_PIN.write(0.2)            # sensor derecho
                    PIEZO_PIN2.write(0.2)           # sensor izquierdo
                    time.sleep(3)
                else:
                    board.digital[12].write(0)      # Led casa 1 OFF
                    # board.digital[11].write(1)      # Led casa 2
                    board.digital[11].write(0)      # Led casa 2
                    board.digital[10].write(0)      # Led casa 3 OFF
                    board.digital[9].write(0)       # Led casa 4 OFF
                    PIEZO_PIN.write(0)            # sensor derecho
                    PIEZO_PIN2.write(0.2)           # sensor izquierdo
                    time.sleep(3)
        else:
            if sw3 is True:
                if sw4 is True:
                    board.digital[12].write(0)      # Led casa 1 OFF
                    board.digital[11].write(0)      # Led casa 2 OFF
                    board.digital[10].write(1)      # Led casa 3
                    board.digital[9].write(1)       # Led casa 4
                    PIEZO_PIN.write(0.2)            # sensor derecho
                    PIEZO_PIN2.write(0.2)           # sensor izquierdo
                    time.sleep(3)
                else:
                    board.digital[12].write(0)      # Led casa 1 OFF
                    board.digital[11].write(0)      # Led casa 2 OFF
                    board.digital[10].write(1)      # Led casa 3
                    board.digital[9].write(0)       # Led casa 4 OFF
                    PIEZO_PIN.write(0)            # sensor derecho
                    PIEZO_PIN2.write(0.2)           # sensor izquierdo
                    time.sleep(3)
            else:
                if sw4 is True:
                    board.digital[12].write(0)      # Led casa 1 OFF
                    board.digital[11].write(0)      # Led casa 2 OFF
                    board.digital[10].write(0)      # Led casa 3 OFF
                    board.digital[9].write(1)       # Led casa 4
                    PIEZO_PIN.write(0.2)            # sensor derecho
                    PIEZO_PIN2.write(0)           # sensor izquierdo
                    time.sleep(3)
                else:
                    board.digital[12].write(0)      # Led casa 1 OFF
                    board.digital[11].write(0)      # Led casa 2 OFF
                    board.digital[10].write(0)      # Led casa 3 OFF
                    board.digital[9].write(0)       # Led casa 4 OFF
                    PIEZO_PIN.write(0)            # sensor derecho
                    PIEZO_PIN2.write(0)           # sensor izquierdo
                    time.sleep(3)

