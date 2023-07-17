from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------
import math
def f(x):
    return sin(x)
N = 100
a = 0
b = math.pi / 2
h = ( b - a ) / N
s = ( h / 2 ) * (sum(f( a + ( i - 1 ) * h ) + f( a + i * h) for i in range(1, N + 1)))
print(s)