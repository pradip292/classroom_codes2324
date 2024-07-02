from Crypto.Cipher import AES
key=b'Abc@)12[OklVDyfe'
cipher=AES.new(key,AES.MODE_EAX)
msg="Welcome to TYIT".encode()
nonce=cipher.nonce
ct=cipher.encrypt(msg)
print("ciphertext is:",ct)
cipher=AES.new(key,AES.MODE_EAX,nonce=nonce)
pt=cipher.decrypt(ct)
msg2=pt.decode()
print("Plaintext is:",msg2)
