#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
	if file == "ifty.py" or file == "thekey.key" or file == "difty.py" :
		continue
	if os.path.isfile(file):
		files.append(file)
print(files)


with open("thekey.key","rb") as key:
	secretkey = key.read()

skey = "ifty1234"

ukey = input("enter the key u got\n")

if ukey == skey:
	for file in files:
		with open(file,"rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)
		with open(file,"wb") as thefile:
			thefile.write(contents_decrypted)
		print("congo all are now decrypted")
else :
	print("wrong key give the real one")
