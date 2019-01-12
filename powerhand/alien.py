from time import sleep
import bluetooth, sys


MAX_CONNECTION_ATTEMPT = 3
def connect():
    bd_addr = "98:D3:31:F5:B9:E7"
    port = 1
    print('Connecting to PowerHand...')
    attempt = 1
    
    while (attempt <= MAX_CONNECTION_ATTEMPT):
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        try:
            sock.connect((bd_addr, port))
        except IOError:
            print('Unable to connect to %s' % bd_addr)
        else:
            print('Ready!')
            return sock
            break;
        attempt += 1
        if attempt <= MAX_CONNECTION_ATTEMPT:
            print('Trying to connect again...')
        sys.stdout.flush()
    return None

sock = connect()

if not sock:
    sys.exit(1)

while 1:
    data = ''
    data = str(sock.recv(1))
    print(data)
    data = data[2:-1]
    if data =='f':
        print('Forward!')
        sock.send('h') # send happy emotion when moving forward
    elif data == 'l':
        print('Left!')
        sock.send('s') # send sad emotion when moving left
    elif data == 'r':
        print('Right!')
        sock.send('a') # send angry emotion when moving right
    elif data == 's':
        print('Stop!')
        sock.send('z') # send sleepy emotion when stop moving
    sleep(1)

sock.close()
