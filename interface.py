# Makeathon Car interface software version 1
# Author: Thabo Malete, thabo.nono.th@gmail.com

import RPi.GPIO as GPIO
import time
from time import sleep
import blynklib
import WidgetLCD

#GPIO pins setup
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

speed=16
right_indicator=18
left_indicator=12
Brightness=19
driveMode=13

_value = 0
_lInd = 1
_rInd = 1
_drive_modes = ["P", "D", "N", "PRES"] 


BLYNK_AUTH = 'ea4b787f99ce4355911eeea0a645a593'

# initialize blynk

blynk = blynklib.Blynk(BLYNK_AUTH)
lcd = WidgetLCD.WidgetLCD(blynk, 0)

WRITE_EVENT_PRINT_MSG = "[WRITE_VIRTUAL_PIN_EVENT] Pin: V{} Value: '{}'"
READ_PRINT_MSG = "[READ_VIRTUAL_PIN_EVENT] Pin: V{}"

# reister handler for virtual pin v4 write event
#@blynk.handle_event('read V11')
#def read_virtual_pin_handler(pin):
#    print(READ_PRINT_MSG.format(pin))
#    blynk.virtual_write(pin, random.randint(0,255))

@blynk.handle_event('write V4')
def write_virtual_event_handler(pin, value):
	_value = value[int(len(value)/2)]
	print(WRITE_EVENT_PRINT_MSG.format(pin, value))
	
	@blynk.handle_event('read V11')
	def read_virtual_pin_handler(pin):
		print(READ_PRINT_MSG.format(pin))
		blynk.virtual_write(pin, value)
		lcd.clear()
		if _value == "0":
			lcd.printlcd(0, 0, "OFF")
		elif _value == "1":
			lcd.printlcd(0, 0, "Speed:")
			lcd.printlcd(0, 1, "range:")
			lcd.printlcd(15, 1, _drive_modes[0])
			if _lInd and _rInd:
				blynk.virtual_write(1, 255)
				blynk.virtual_write(2, 255)
				time.sleep(0.5)
				blynk.virtual_write(1, 0)
				blynk.virtual_write(2,0)


			elif _rInd and not _lInd:
				blynk.virtual_write(2, 255)
				blynk.virtual_write(1, 0)
				time.sleep(0.5)
				blynk.virtual_write(2, 0)
	
			elif not _rInd and _lInd:
				blynk.virtual_write(1, 255)
				blynk.virtual_write(2, 0)
				time.sleep(0.5)
				blynk.virtual_write(1,0)

			else:
				blynk.virtual_write(1,0)
				blynk.virtual_write(2,0)
		else:
			print("FAILED TO INITIATE START")



	# stuff to do
#@blynk.handle_event('write v11')
#def read_virtual_pin_handler(pin):
#	print(READ_PRINT_MSG.format(pin))
#	blynk.virtual_write(pin, state)

while True:
	blynk.run()

