import bluetooth

bd_addr = "98:D3:31:F5:B9:E7"
port = 1
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((bd_addr,port))
print('Ready!')
print('Press 1 to switch on LED, 0 to switch off')
while 1:
    tosend = input()
    if tosend != 'q':
            sock.send(tosend)
    else:
            break
sock.close()
