from pyDes import *

key = input("Enter Key: ").encode()
data = input("Enter data to encrypt: ")
des = des(key, CBC ,b"\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)

da = des.encrypt(data)
print("%r" %da)

print("%r" %des.decrypt(da))
