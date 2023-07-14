text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO
import re

a = re.sub('[,.]',' ', text)
b =  a.split( )
print( *list( map(len, (b) ) ), sep = '')