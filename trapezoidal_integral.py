from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------
import math
def f(x):
    return x**5.0
N = 100
a = sin(0)
b = sin( math.pi / 2 )
h = (b - a) / N
s = (h / 2) * (f(a) + 2*sum(f(h*i) for i in range(1, N - 1) ) + f(b) )
print(s)