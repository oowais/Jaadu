import time
from Adafruit_LED_Backpack import Matrix8x8


# Create display instance on default I2C address (0x70) and bus number.
dis = Matrix8x8.Matrix8x8()

# Alternatively, create a display with a specific I2C address and/or bus.
# display = Matrix8x8.Matrix8x8(address=0x74, busnum=1)

# Initialize the display. Must be called once before using the display.
dis.begin()

image = [(1,2),(1,3),(1,4),(1,5),(2,1),(2,2),(2,3),(2,4),(2,5),(2,6),(3,1),(3,2),(3,3),
		 (3,4),(3,5),(3,6),(4,1),(4,2),(4,3),(4,4),(4,5),(4,6),(5,1),(5,2),(5,3),(5,4),
		 (5,5),(5,6),(6,2),(6,3),(6,4),(6,5)]
# Run through each pixel individually and turn it on.
try:
	dis.clear()
	dis.write_display()
	print('Startup..')
	for x in range(8):
		for y in range(8):
			dis.set_pixel(x, y, 1)
			# time.sleep(0.1)
			dis.write_display()
	time.sleep(0.5)
	dis.clear()
	dis.write_display()
	time.sleep(0.2)

	print('Eye-ball')
	for a in image:
		dis.set_pixel(a[0],a[1],1)
	dis.write_display()

except KeyboardInterrupt:
	print('Exit...')


