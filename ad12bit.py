#!/usr/bin/env python3
# read abelectronics ADC Pi V2 board inputs with repeating reading from each channel 12 bit mode.
# uses quick2wire from http://quick2wire.com/ github: https://github.com/quick2wire/quick2wire-python-api
# Requries Python 3 
# GPIO API depends on Quick2Wire GPIO Admin. To install Quick2Wire GPIO Admin, follow instructions at http://github.com/quick2wire/quick2wire-gpio-admin
# I2C API depends on I2C support in the kernel

# Version 1.0  - 09/07/2013
# Version History:
# 1.0 - Initial Release
#
# Usage: changechannel(address, hexvalue) to change to new channel on adc chips
# Usage: getadcreading(address) to return value in volts from selected channel.
#
# address = adc_address1 or adc_address2 - Hex address of I2C chips as configured by board header pins.

import quick2wire.i2c as i2c

adc_address1 = 0x68
adc_address2 = 0x69

varDivisior = 1 # from pdf sheet on adc addresses and config
varMultiplier = (2.4705882/varDivisior)/1000

            
            
with i2c.I2CMaster() as bus:
	def changechannel(address, adcConfig):
		bus.transaction(i2c.writing_bytes(address, adcConfig))
		
	def getadcreading(address):
		h, l ,s = bus.transaction(i2c.reading(address,3))[0]
		while (s & 128):
			h, l, s  = bus.transaction(i2c.reading(address,3))[0]
		# shift bits to product result
		t = (h << 8) | l
		# check if positive or negative number and invert if needed
		if (h > 128):
			t = ~(0x020000 - t)
		return t * varMultiplier
	
	while True:
		changechannel(adc_address1, 0x90)
		print ("Channel 1: %02f" % getadcreading(adc_address1))
		changechannel(adc_address1, 0xB0)
		print ("Channel 2: %02f" % getadcreading(adc_address1))
		changechannel(adc_address1, 0xD0)
		print ("Channel 3 :%02f" % getadcreading(adc_address1))
		changechannel(adc_address1, 0xF0)
		print ("Channel 4: %02f" % getadcreading(adc_address1))
		changechannel(adc_address2, 0x90)
		print ("Channel 5: %02f" % getadcreading(adc_address2))
		changechannel(adc_address2, 0xB0)
		print ("Channel 6: %02f" % getadcreading(adc_address2))
		changechannel(adc_address2, 0xD0)
		print ("Channel 7 :%02f" % getadcreading(adc_address2))
		changechannel(adc_address2, 0xF0)
		print ("Channel 8: %02f" % getadcreading(adc_address2))
