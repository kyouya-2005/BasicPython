


# TODO
def gcd(a, b):
   while b != 0:
      a, b = b, a % b
   return a

a1 = 10
b1 = 20
GCD = gcd(a1, b1)
print(GCD)

a2 = 14
b2 = 91
GCD = gcd(a2, b2)
print(GCD)

a3 = 91
b3 = 14
GCD = gcd(a3, b3)
print(GCD)