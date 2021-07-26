#!/usr/bin/python3


import sys
import hashlib




arg1_bytes = bytes(sys.argv[1], 'utf-8')
dk = hashlib.pbkdf2_hmac('sha512',arg1_bytes,b'Km5d5ivMy8iexuHcZrsD',200000)


print ('output', dk.hex())


