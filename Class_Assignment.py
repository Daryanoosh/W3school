# Python Iterators and Generators

mylist = [10, 20, 30, 40]
Iter = iter(mylist)
print(next(Iter))
print(next(Iter))
print(next(Iter))
print(next(Iter))

# Python Scope
# 1st
x = 10
def myfunc():
  x = 5
  print(x)
myfunc()
print(x)

print("")
# 2nd

x = 10
def myfunc():
  global x
  x = 5
  print(x)
myfunc()
print(x)

# Python Modules

def add(a, b):
  return a + b 

# Python Modules
import c1
x = c1.add(2, 3)
print(x)

# Python Modules
import random
x = random.randrange(1, 100)
print(x)
# Python Dates

import datetime
x = datetime.datetime.now()
print(f"{x.strftime('%d')}-{x.strftime('%m')}-{x.strftime('%Y')}")

x = datetime.datetime(2026, 4, 16)
y = datetime.datetime.now()
result = abs(x - y)
print(result)

# Python Math
# 1st
  # a)
import math
x = int(math.sqrt(81))
print(x)

  # b)
x = math.pi
print(x)

  # c)
x = math.floor(5.9)
y = math.ceil(5.9)
print(x)
print(y)

# 2nd
r = int(input())
x = math.pi
C = x * r ** 2
print(C)

# 1st
import json
thisdict = {"name": "Darya", 
            "age": 20, 
            "GPA": 3.81
            }
y = json.dumps(thisdict)
print(y)

# 2nd
Json = '{"course": "Python", "level": "beginner"}'

z = json.loads(Json)
print(z)