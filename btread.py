#!/usr/bin/python

import binascii
import struct
import pygatt.backends


MACADDR='DC:88:34:2D:8E:DB'
TEMPERATURE_UUID="00002235-b38d-4985-720e-0F993a68ee41"
HUMIDITY_UUID="00001235-b38d-4985-720e-0F993a68ee41"
BATTERY_UUID="2A19"


adapter = pygatt.backends.GATTToolBackend()
adapter.start()

device = adapter.connect(MACADDR,5,'random')
print "connected"

temp = device.char_read(TEMPERATURE_UUID)
tempf = struct.unpack('<f',temp)
print "read temp : %.2f" % tempf


humi = device.char_read(HUMIDITY_UUID)
humif = struct.unpack('<f',humi)
print "read humi : %.2f" % humif


batt = device.char_read(BATTERY_UUID)
print "read batt : %d" % batt[0]


device.disconnect()
adapter.stop()
