from __future__ import print_function
from __future__ import division

# Variables and Types
cost = 1
y = 2.5
name = "Kevin"
active = True

print("hello")
print(cost)
print(y)
print()
print("cost is", cost, "and y is", y)

print(type(cost), type(y), type(name), type(active))

# Converting between types

cost = 2.5
string_cost = str(cost)
int_cost = int(cost)
factor = '3.14'
float_factor = float(factor)
print(type(float_factor), type(cost))

print(int(float_factor*cost))

# Operations

print(5*5)
print(3+2)
print(7/5)
print("3 squared is", 3**2)
print("sqrt(2) is", 2**0.5)
print(15%10)

# Containers

## Lists
### Basic Operations

x = []
x = ['hello', 1, 1.2, [2, 3]]
x = [1, 2, 3, 4, 5]
print(x)

three = x[2]
print(three)
last = x[-1]
print(last)
length = len(x)
print(length)

### Slicing

x = [1, 2, 3, 4, 5]
first_three = x[0:3]
print(first_three)
first_three = x[:3]
print(first_three)
last_three = x[-3:]
print(last_three)

### Append, Extend, Concatenate

x = [1]
x.append(2)
x.extend([3, 4])
print(x)
y = x + [6, 7, 8]
print(y)
x.remove(2)
print(x)

### Iteration

for item in x:
    print(item)

for i, item in enumerate(x):
    print(i, item)

## Dictionaries

### Creating Dictionaries

extensions = {}
extensions['Kevin'] = 6007
extensions['Yann'] = 6008

print(extensions)

extensions = {
    'Kevin': 6007,
    'Yann': 6008
}

print(extensions)

### Lookup

kevin_ext = extensions['Kevin']
print(kevin_ext)
print('Bob' in extensions)

ext = extensions.get('Bob', None)
print(ext)
print(extensions.keys())
print(extensions.values())

# Control Flow

x = 10
y = 15
if x < y:
    message = 'x is less than y'
else:
    message = 'x is greater than y'

for i in range(10):
    print(i, end=' ')

print()

while x < y:
    x += 1

if message.startswith('x is'):
    pass
elif message.startswith('y is'):
    pass
else:
    message = None