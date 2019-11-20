# Controls the LCD Widget in the Blynk App
class WidgetLCD():
	# contructor for the Blynk Widget
	# Parameters:
	#	blynk - Blynk object
	#	vPin  - The Virtual pin the LCD is connected to

	def __init__(self, blynk, vPin):
		self.__blynk = blynk
		self.__vPin = vPin

	# clear
	# clears the screen
	# Parameters: None
	def clear(self):
		self.__blynk.virtual_write(self.__vPin, 'clr')
		

	# printlcd(x,y,s)
	# prints a message to the LCD
	# Parameters:
	#	x - x-position of the lcd cursor| range(0,15)
	#	y - y-postion of the lcd cursor | range(0,1)
	#	s - messgae to print to LCD

	def printlcd(self, x, y, s):
		self.__blynk.virtual_write(self.__vPin, '\0'.join(map(str, ('p', x, y, s))))

