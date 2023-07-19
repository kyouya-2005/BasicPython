def GCD(a, b):
    def euclid(a, b):
        while b != 0:
            a, b = b, a % b

        return a
    gcd = euclid(a, b)
    return gcd == 1

a1 = 10
b1 = 20
coprime = GCD(a1, b1)
print(coprime)

a2 = 14
b2 = 91
coprime = GCD(a2, b2)
print(coprime)

a3 = 91
b3 = 14
coprime = GCD(a3, b3)
print(coprime)