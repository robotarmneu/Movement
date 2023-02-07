import pyfirmata
import time

mega = {
    'digital' : tuple(x for x in range(54)),
    'analog' : tuple(x for x in range(16)),
    'pwm' : tuple(x for x in range(2,14)),
    'use_ports' : True,
    'disabled' : (0, 1, 14, 15) # Rx, Tx, Crystal
}

board = pyfirmata.Board(port='COM3', layout=mega)

print("Board recognized")

step = board.get_pin('d:46:o')
direction = board.get_pin('d:48:o')
enable = board.get_pin('a:8:o')
enable.mode = pyfirmata.OUTPUT

while True:
    enable.write(0)
    direction.write(1)

    for i in range(200):
        step.write(1)
        time.sleep(1)
        step.write(0)
        time.sleep(1)

    time.sleep(1)

    


# dont put the wires in the same direction

# Z-STEP - D46 
# Z-DIR - D48
# Z-EN - A8