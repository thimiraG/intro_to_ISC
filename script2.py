#!/usr/bin/python3


import sys
import hashlib, uuid



salt = uuid.uuid4().hex

print (salt)

arg1_bytes = bytes(sys.argv[1], 'utf-8')
dk = hashlib.pbkdf2_hmac('sha512',arg1_bytes,b'salt',200000)


print ('output', dk.hex())

