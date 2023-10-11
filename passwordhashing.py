import hashlib
from hashlib import pbkdf2_hmac
import os

def remove(s):
	return s.replace("  ", "")
	
	
salt = os.urandom(16)

userIn = input("Please enter your password: ")

print("You entered: \n", userIn)

toSecure = input("Would you like to secure your password (y/n): ")

while(toSecure != 'y' and toSecure != 'n'):
	print("Invalid input, please try y or n")
	toSecure = input("Would you like to secure your password (y/n): ")
	if(toSecure == "n"):
		break


while(toSecure == 'y'):
	method = input("would you like to have it done automatically or manually? (a/m): ")
	if(method != 'a' and method != 'm'):
		print("Invalid input, please put a or m")
		method = input("Would you like to have it done automatically or manually? (a/m): ")
	
	if(method == "a"):
		tohex = input("Would you like to hex your password?: (y/n)")
		passk = pbkdf2_hmac('sha256', b'userIn', b'salt', 16)
		if(tohex == 'y'):
			print(passk.hex())
			break
		elif(tohex == 'n'):
			print(passk)
			break
		else:
			break
			
	if(method == "m"):
		print("Please select between these hash digest algorithms(sha1, sha256, sha384, sha512, sha224)")
		digest = input("Please provide the hash digest algorithm you would like to use(5 choices): ")
		
		if(digest == 'sha1'):
			tohex = input("Would you like to hex your password?: (y/n)")
			if(tohex != 'y' and tohex!= 'n'):
				break
			newSalt = input("Please enter a desired salt string: ")
			keyLen = input("Please enter the desired length of key: ")
			keyLen = int(keyLen)
			passk = pbkdf2_hmac('sha1', b'userIn', b'newSalt', keyLen)
			if(tohex == 'y'):
				print(passk.hex())
			elif(tohex == 'n'):
				print(passk)
		if(digest == 'sha256'):
			tohex = input("Would you like to hex your password?: (y/n)")
			if(tohex != 'y' and tohex!= 'n'):
				break
			newSalt = input("Please enter a desired salt string: ")
			keyLen = input("Please enter the desired length of key: ")
			keyLen = int(keyLen)
			passk = pbkdf2_hmac('sha256', b'userIn', b'newSalt', keyLen)
			if(tohex == 'y'):
				print(passk.hex())
			elif(tohex == 'n'):
				print(passk)
		if(digest == 'sha384'):
			tohex = input("Would you like to hex your password?: (y/n)")
			if(tohex != 'y' and tohex!= 'n'):
				break
			newSalt = input("Please enter a desired salt string: ")
			keyLen = input("Please enter the desired length of key: ")
			keyLen = int(keyLen)
			passk = pbkdf2_hmac('sha384', b'userIn', b'newSalt', keyLen)
			if(tohex == 'y'):
				print(passk.hex())
			elif(tohex == 'n'):
				print(passk)
		if(digest == 'sha512'):
			tohex = input("Would you like to hex your password?: (y/n)")
			if(tohex != 'y' and tohex!= 'n'):
				break
			newSalt = input("Please enter a desired salt string: ")
			keyLen = input("Please enter the desired length of key: ")
			keyLen = int(keyLen)
			passk = pbkdf2_hmac('sha512', b'userIn', b'newSalt', keyLen)
			if(tohex == 'y'):
				print(passk.hex())
			elif(tohex == 'n'):
				print(passk)
			
		if(digest == 'sha224'):
			tohex = input("Would you like to hex your password?: (y/n)")
			if(tohex != 'y' and tohex!= 'n'):
				break
			newSalt = input("Please enter a desired salt string: ")
			keyLen = input("Please enter the desired length of key: ")
			keyLen = int(keyLen)
			passk = pbkdf2_hmac('sha512', b'userIn', b'newSalt', keyLen)
			if(tohex == 'y'):
				print(passk.hex())
			elif(tohex == 'n'):
				print(passk)
	break