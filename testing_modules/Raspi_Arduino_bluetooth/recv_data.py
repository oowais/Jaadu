import bluetooth
from time import sleep

bd_addr = "98:D3:31:F5:B9:E7"
port = 1
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((bd_addr,port))

data = ''
while 1:
	try:
		data = str(sock.recv(1024))
		if data.find('f'):
			print('Forward!')
		elif data == 'b':
			print('Back!')
		sleep(0.1)
		#data += sock.recv(1024)
		#data_end = data.find('\n')
		#if data_end != -1:
			#rec = data[:data_end]
			#print(data)
			#data = data[data_end+1:]
	except KeyboardInterrupt:
		break
sock.close()
