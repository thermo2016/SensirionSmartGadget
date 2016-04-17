#!/usr/bin/python

import binascii
import struct

#temphex='7b 14 BE 41'
#41bbae14
temphex='14 AE BB 41'

tempfloat=struct.unpack('<f', binascii.unhexlify(temphex.replace(' ', '')))

print "%.18f" % tempfloat
