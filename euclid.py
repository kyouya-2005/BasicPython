a = 10
b = 20

# TODO
def gcd(a, b):
    r = a % b

    while r != 0:
       a, b = b, r
       r = a % b
       return b
if __name__ == '__main__':
    num1 = a
    num2 = b
    GCD = gcd(num1, num2)
    print(f"({num1}, {num2}) -> gcd: {GCD}")

    a = 14
    b = 91
def gcd(a, b):
    r = a % b

    while r != 0:
       a, b = b, r
       r = a % b
       return b
if __name__ == '__main__':
    num1 = a
    num2 = b
    GCD = gcd(num1, num2)
    print(f"({num1}, {num2}) -> gcd: {GCD}")

a = 91
b = 14
def gcd(a, b):
    r = a % b

    while r != 0:
       a, b = b, r
       r = a % b
       return b
if __name__ == '__main__':
    num1 = a
    num2 = b
    GCD = gcd(num1, num2)
    print(f"({num1}, {num2}) -> gcd: {GCD}")