import hashlib
# Take input from the user
str = input("Enter the string to hash: ")
# Hashing the input string using MD5
r1 = hashlib.md5(str.encode())
r2 = hashlib.sha1(str.encode()) 
print("The hexadecimal equivalent of hash is : ", end ="")
print(r1.hexdigest())
print("sha1:",r2.hexdigest())