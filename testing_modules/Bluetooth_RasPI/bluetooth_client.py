import bluetooth

bd_addr = "58:00:E3:F1:C1:20"

port = 1

sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))

sock.send("hello Saurav!!")

sock.close()
