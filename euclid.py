


# TODO
def gcd(a, b):

    while b != 0:
        a, b = b, a / b
        return b
num1 = 10
num2 = 20
GCD = gcd(num1, num2)
print(f"({num1}, {num2}) -> gcd: {GCD}")

num1 = 14
num2 = 91
GCD = gcd(num1, num2)
print(f"({num1}, {num2}) -> gcd: {GCD}")

num1 = 91
num2 = 14
GCD = gcd(num1, num2)
print(f"({num1}, {num2}) -> gcd: {GCD}")