import bluetooth

bd_addr = "98:D3:31:F5:B9:E6"
port = 1
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((bd_addr,port))

while 1:
        a = sock.recv(1)
        print(a)
sock.close()
