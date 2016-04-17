# SensirionSmartGadget
https://www.sensirion.com/en/products/digital-humidity-sensors-for-reliable-measurements/development-kit/

##Sales blurb:
> "The Smart Gadget not only shows humidity and temperature values on the display, but can also communicate with a bluetooth SMART capable device like a smartphone."

##How to use on the Raspberry Pi? 
This is done with a Raspberry Pi 2B running Ubuntu Mate, but should work on other distributions.

##Use a compatable USB Blurtooth dongle. 
I use the Plugable one:
http://www.amazon.co.uk/Plugable-Bluetooth-Adapter-Raspberry-Compatible/dp/B009ZIILLI?ie=UTF8&psc=1&redirect=true&ref_=oh_aui_detailpage_o00_s00
Others may work.

##Install the BlueZ package. 
I downloaded the latest version from
https://www.kernel.org/pub/linux/bluetooth
Install instructions can be found here
http://www.elinux.org/RPi_Bluetooth_LE#BlueZ_installation
Or you can install from the repositry
```
$ sudo apt-get install bluez bluez-utils
```

##Test connecting. 
Press the button on the sensor gadget to switch on the bluetooth radio. Then :
```
$ sudo hcitool dev
Devices:
	hci0	5C:F3:70:75:C9:7B
```
```
$ sudo hcitool lescan
LE Scan ...
98:D6:BB:22:0B:19 (unknown)
98:D6:BB:22:0B:19 (unknown)
DC:88:34:2D:8E:DB (unknown)
DC:88:34:2D:8E:DB Smart Humigadget
```
```
$ sudo gatttool -I -b DC:88:34:2D:8E:DB -t random
[DC:88:34:2D:8E:DB][LE]> connect
Attempting to connect to DC:88:34:2D:8E:DB
Connection successful
```

##Reading the sensor data.
For this you need to know the UUID of the sensors. This can be found in the documentation from the Sensiron GitHub site.
- TEMPERATURE_UUID="00002235-b38d-4985-720e-0F993a68ee41"
- HUMIDITY_UUID="00001235-b38d-4985-720e-0F993a68ee41"
- BATTERY_UUID="2A19"

From the gatttols prompt:
```
[DC:88:34:2D:8E:DB][LE]> char-read-uuid 00002235-b38d-4985-720e-0F993a68ee
handle: 0x0037   value: 00 00 b2 41
```
The value is a 32bit floating point number. See bttest.py to see how to convert it to a readable number.

##Reading from a python script. 
I use the pygatt library.
https://github.com/peplin/pygatt
Install using pip
```
pip install pygatt
```
See btread.py to see how to read the sensors.

##References
https://github.com/Sensirion
https://rnestler.github.io/reading-the-shtc1-smart-gadget-ble-device.html
https://github.com/peplin/pygatt





