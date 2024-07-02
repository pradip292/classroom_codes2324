def is_primitive_root(g, p):
    coprimes = {pow(g, k, p) for k in range(1, p)}
    return len(coprimes) == p - 1

def find_primitive_root(p):
    for g in range(2, p):
        if is_primitive_root(g, p):
            return g
    return None

a = int(input("Enter the prime number: "))  # 23
b = find_primitive_root(a)  # Find primitive root for a
print(f"The primitive root modulo {a} is {b}")

p1 = int(input("Enter Private Key for A: "))  # 4
p2 = int(input("Enter Private Key for B: "))  # 3

x = pow(b, p1, a)  # x = b^p1 mod a
y = pow(b, p2, a)  # y = b^p2 mod a

print("A receive the public key is %d." % y)
print("B recieve the public key is %d." % x)

ka = pow(y, p1, a)  # ka = y^p1 mod a
kb = pow(x, p2, a)  # kb = x^p2 mod a

print("Secret key is %d" % ka)
#print("Secret key is %d" % kb)
