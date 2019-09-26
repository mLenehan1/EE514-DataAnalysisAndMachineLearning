from __future__ import print_function
from __future__ import division
import sys
import numpy
from math import cos, sin, pi

# Packages and Modules

print(pi)
print(cos(pi))
print(round(sin(1), 3))

a = numpy.array([1, 2, 3])
print(a)

## Creating a Module

from mymodule import Particle

# Creating a Package

import mypackage.mymodule

# Error Handling

d = {"a": 1, "b": 2}
try:
    z = d['c']
except KeyError as e:
    print('c is not a key')

try:
    z = non_existant['c']
except:
    print('a NameError was caught!')

## Raising Exceptions

# raise Exception('boom')

class MyException(Exception):
    pass

# raise MyException('bang')

try:
    raise MyException('boom')
except MyException as e:
    print(e)
except Exception as e:
    print('Error', e)
finally:
    print('always executed')

## Python philosophy

# prefer

try:
    r = d['a']
except KeyError:
    print('a missing')
    r = None
print(r)

# to

if 'a' in d:
    r = d['a']
else:
    print('a missing')
    r = None
print(r)