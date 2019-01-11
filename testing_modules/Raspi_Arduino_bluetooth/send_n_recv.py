from time import sleep
import bluetooth

bd_addr = "98:D3:31:F5:B9:E7"
port = 1
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((bd_addr,port))
print('Ready!')
print('Press 1 to switch on LED, 0 to switch off')

while 1:
    data = ''
    tosend = input()
    if not len(tosend) > 0:
        continue
    elif tosend != 'q':
            sock.send(tosend)
    else:
            break
    sleep(0.1)
    data = str(sock.recv(1024))
    if data.find('on'):
        print('LED turned ON!')
        print(data)
    elif data.find('off'):
        print('LED turned OFF!')

sock.close()
