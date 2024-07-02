
a=int(input("Enter the  prime number:")) #23
b=int(input("Enter the primitive Root:")) #9

p1=int(input("Enter Private Key for A:")) #4
p2=int(input("Enter Private Key for B:"))  #3

x=pow(b, p1, a)
 #x=9^4mod23

y=pow(b,p2,a)
  #y=9^3mod23

print("A receive the public key is :",y)
print("B recieve the public key is :",x)

ka=pow(y,p1,a)
kb=pow(x,p2,a)

print("Secreat key is :",ka)
#print("Secreat key is ",kb)


