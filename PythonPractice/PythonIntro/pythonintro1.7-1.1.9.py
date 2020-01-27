from __future__ import print_function
from __future__ import division
import sys

# Functions
## Using optional arugements

def square(x):
    return x**2

def panic(message):
    print(message, file=sys.stderr)

print(square(3))
panic('something went wrong')

def parse_text(text, sep=',',strip=True):
    parts = text.split(sep)
    if strip:
        for i, part in enumerate(parts):
            parts[i] = part.strip()
    return parts

print(parse_text('some text, separated, by , commas'))
print(parse_text('some text, separated, by , commas', strip=False))

## Returning multiple values

x = (1, True, 'x')
print(x)
x = 1, 2, 3
print(x)
x = 1,
print(x)

x = 1, 2, 3
first, second, third = x
print(second)

## Using tuples to return multiple values

def split_extension(filename):
    """
    Splits the filename into a tuple (name, extension).
    """

    index = filename.rfind('.')
    if index < 1:
        return filename, None
    name = filename[:index]
    extension = filename[index+1:]
    return name, extension

name, ext = split_extension('image.jpg')
print(name, ext)
parts = split_extension('archive.tar.gz')
print(parts)
print(parts[1])
name, ext = parts

## Variadic arguments

def print_all(*args):
    for arg in args:
        print(arg, end=', ')
    print()

print_all(1, 2, 3)

# Classes and OO

class Particle(object):
    """
    This class models a particle with a name and a speed.
    """

    def __init__(self, name, speed=1):
        self.name = name
        self.speed = speed
    
    def speed_up(self):
        self.speed += 1.0

    def slow_down(self):
        self.speed -=1.0

p = Particle('x')
p.speed_up()
print(p.name, p.speed)
p.slow_down()
print(p.name, p.speed)

## Special Methods

class BetterParticle(Particle):
    """
    Like a Particle, but knows how to convert itself to a string!
    """

    def __str__(self):
        return '{} with speed {}'.format(self.name, self.speed)

q = BetterParticle('y')
q.speed_up()
print(q)