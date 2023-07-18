a = 61
b = 10

# TODO
def sosuu(x):
     if x <= 1:
        return False
     for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
        return True
     

print(sosuu(a))
print(sosuu(b))