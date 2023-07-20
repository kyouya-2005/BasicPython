from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------
a = 0
b = 1
n = 100
import math
def f( x ):
    return sin( x )
def trapezoidal( f, a, b, n ):
    h = ( b - a ) / n
    s = ( h / 2 ) * (sum( f( a + ( i + 1 ) * h ) + f( a + i * h ) for i in range( 1, n + 1 ) ) )
    return s

def g( x ):
    return 4 / ( 1 + x ** 2 )

def j( x ):
    return ( ( ( math.pi ) ** ( 1 / 2 ) ) * math.exp( - x ** 2 ) )

print( trapezoidal( sin, 0, math.pi / 2, 50 ) )

print( trapezoidal( g, 0, 1, 100 ) )

print( trapezoidal( j, - 100, 100, 1000 ) )