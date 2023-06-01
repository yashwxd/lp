from math import gcd
msg = int(input("Enter the number you want to encrypt: "))
p , q = map(int, input("Enter any two PRIME Numbers: ").split())
n = p*q
z = (p-1) * (q-1)
e = next(i for i in range(2,z) if gcd(i,z)==1)
def mod_inverse(e,z):
    for d in range (1,z):
        if (e * d) % z == 1:
            return d
d = mod_inverse(e,z)
c = pow(msg, e, n)
msgback = pow (c, d, n)
print("value of n is: ", n)
print("value of z is: ", z)
print("value of e is: ", e)
print("value of d is: ", d)
print("encrypted message is: ", c)
print("decrypted message is: ", msgback)
