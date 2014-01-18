ADC Pi Version 2
=======
Demo code for the ADC Pi version 2 board from http://www.abelectronics.co.uk/products/3/Raspberry-Pi/17/ADC-Pi-V2---Raspberry-Pi-Analogue-to-Digital-converter

Code demos are available in C and Python 2.7 / 2.8
Old quick2wire demos have been removed as the quick2wire lib appears to be no longer maintained. 

Requries Python 2.7
Requires SMBus 

install SMBus with:
	sudo apt-get install python-smbus

adclogger.py - Samples at 18bit rate and saves to a text file with timestamp

adcpi12.py - Samples at 12bit rate and outputs to console/terminal
adcpi16.py - Samples at 16bit rate and outputs to console/terminal
adcpi18.py - Samples at 18bit rate and outputs to console/terminal

adc.c - C language demo which samples at 18bit rate and outputs to console/terminal