import pyfirmata,winsound,time
board = pyfirmata.Arduino('com8')
it=pyfirmata.util.Iterator(board)
it.start()
touch1=board.get_pin('d:2:i')
touch2=board.get_pin('d:3:i')
touch3=board.get_pin('d:4:i')
touch4=board.get_pin('d:5:i')
while True:
    val1=touch1.read()
    if val1 ==True:
        winsound.PlaySound(r'Voice/1.wav',winsound.SND_FILENAME)
    val2=touch2.read()
    if val2 ==True:
        winsound.PlaySound(r'Voice/2.wav',winsound.SND_FILENAME)
    val3=touch3.read()
    if val3 ==True:
        winsound.PlaySound(r'Voice/3.wav',winsound.SND_FILENAME)
    val4=touch4.read()
    if val4 ==True:
        winsound.PlaySound(r'Voice/4.wav',winsound.SND_FILENAME)
    time.sleep(0.5)
