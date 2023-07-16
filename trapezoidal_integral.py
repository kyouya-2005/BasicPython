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
s = ( h / 3 ) * sum( (f( h*i ) + 4*f( h*( i + 1 ) ) + f( h*( i + 2 ) ) ) for i in range(0, N - 1, 2) )
print(s)