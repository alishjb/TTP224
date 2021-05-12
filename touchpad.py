import pyfirmata
import time
board= pyfirmata.Arduino('COM5')
it = pyfirmata.util.Iterator(board)
it.start()
touch1=board.get_pin('d:4:i')
touch2=board.get_pin('d:5:i')
touch3=board.get_pin('d:6:i')
touch4=board.get_pin('d:7:i')
while True:
    valtouch1=touch1.read()
    if valtouch1==True:
        print('key 1 pressed')
    valtouch2=touch2.read()
    if valtouch2==True:
        print('key 2 pressed')
    valtouch3=touch3.read()
    if valtouch3==True:
        print('key 3 pressed')
    valtouch4=touch4.read()
    if valtouch4==True:
        print('key 4 pressed')
    time.sleep(1)