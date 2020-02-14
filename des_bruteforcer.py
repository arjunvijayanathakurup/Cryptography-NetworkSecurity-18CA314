import pyDes as pd

# key = input("Enter Key: ").encode()
# data = input("Enter data to encrypt: ")
for i in range(10000000, 99999999):
    des = pd.des((str(i).encode()), pd.CBC ,b"\0\0\0\0\0\0\0\0", pad=None, padmode=pd.PAD_PKCS5)

# da = des.encrypt(data).hex()
# print("%r" %da)

    da = "4B518774A408E3E5"
    val = des.decrypt(bytes.fromhex(da))
    print("%r" %val)
