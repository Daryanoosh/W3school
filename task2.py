# Python Booleans
""" print(10 > 9)
ordprint(10 == 9)
print(10 <= 9)

a = 200
b = 300
if b > a:
	print("b is greater than a")
else:
	print("b is not greater than a") """

print(bool("Hello"))
print(bool(10))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


class myclass():
    def __len__(self):
        return 0


myobj = myclass()
print(bool(myobj))


def myFunction():
    return True


print(myFunction())


def myFunction():
    return True


if myFunction():
    print("YES!")
else:
    print("NO!")

x = 300
print(isinstance(x, int))

# Python Operators

print(10 + 5)

x = 5
y = 3
print(x + y)

x = 5
y = 3

print(x - y)

x = 5
y = 3

print(x * y)

x = 12
y = 3

print(x / y)

x = 5
y = 2

print(x % y)

x = 2
y = 5

print(x ** y)

x = 15
y = 2

print(x // y)

x = 5

print(x)

x = 5
x += 3

print(x)

x = 5
x -= 3
print(x)

x = 5
x *= 3

print(x)

x = 5
x /= 3
print(x)

x = 5
x %= 3

print(x)

x = 5
x //= 3
print(x)

x = 2
x **= 3
print(x)

x = 5
x &= 3
print(x)

x = 5
x |= 3
print(x)

x = 5
x ^= 3
print(x)

x = 5
x >>= 3
print(x)

x = 5
x <<= 3
print(x)

print(x := 3)

x = 5
y = 3

print(x == y)

x = 5
y = 3

print(x != y)

x = 5
y = 3

print(x > y)

x = 5
y = 3

print(x < y)

x = 3
y = 5

print(x >= 5)

x = 3
y = 5

print(x <= y)

x = 5

print(x > 3 and x < 10)

x = 5
print(x > 2 or x < 20)

x = 5
print(not (x > 2 and x < 10))

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(y is z)
print(x == y)

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)
print(x is not y)
print(y is not z)
print(x != y)

x = ["tamana", "Ahmad"]

print("tamana" in x)

x = ["tamana", "Ahmad"]

print("tamana" not in x)

print(6 & 3)
print(6 | 3)
print(6 ^ 3)
print(~3)
print(3 << 2)
print(8 >> 2)

print((6 + 3) - (6 + 3))

print(100 + 5 * 3)

print(100 - 3 * 3)

print(100 + ~3)

print(100 + 5 * 3)

print(100 - 5 * 3)

print(8 >> 4 - 2)

print(6 & 2 + 1)

print(6 ^ 2 + 1)

print(6 | 2 + 1)

print(5 == 4 + 1)

print(not 5 == 5)

print(1 or 2 and 3)

print(4 or 5 + 10 or 8)

print(5 + 4 - 7 + 3)

list = ["Darya", "Tamana", "Sahar"]
print(list)

list = ["Darya", "Tamana", "Sahar", "Darya", "Tamana"]
print(list)

list = ["Darya", "Tamana", "Sahar"]
print(len(list))

list1 = ["Darya", "Tamana", "Sahar"]
list2 = [1, 5, 3, 9]
list3 = [True, False, True]

print(list1)
print(list2)
print(list3)

list1 = ["abc", 34, True, 30, "male"]
print(list1)

list = ["Darya", "Tamana", "Sahar", "Darya", "Tamana"]
print(list)
print(type(list))

x = list(("apple", "banana", "cherry"))
print(x)

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

Fruits = ["apple", "banana", "cherry"]
Fruits[1] = "blackcurrant"

print(Fruits)

myFruits = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
myFruits[1:3] = ["blackcurrant", "watermelon"]
print(myFruits)

thislist = ["apple", "banana", "cherry"]

thislist[1:3] = ["watermelon"]

print(thislist)

thislist = ["apple", "banana", "cherry"]

thislist.insert(2, "watermelon")

print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]

thislist.extend(tropical)

print(thislist)

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")

thislist.extend(thistuple)

print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")

print(thislist)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.pop(1)

print(thislist)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.pop()

print(thislist)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
del thislist[0]

print(thislist)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
del thislist

print(thislist)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.clear()

print(thislist)

# Loop through a list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
# range(start, stop, steps)
# range(len(thislist)), starts at zero and ends in 3 exlusive
for i in range(len(thislist)):
    print(thislist[i])

i = 0
while i < len(thislist):
    print(thislist[i])
    i += 1


# Looping Using List Comprehension
# List Comprehension offers the shortest syntax for looping through lists:
thislist = ["Tamana", "Sahar", "Ahmad Ali"]
[print(x) for x in thislist]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)
newlist = [newlist.append(x) for x in fruits if "a" in x]
# newlist = [expression for item in iterable if condition == True]
newlist = [x for x in newlist if x != "apple"]

newlist = [x for x in fruits]
newlist = [x for x in range(10)]
print(newlist)

newlist = [x for x in range(10) if x < 5]
newlist = [x.upper() for x in fruits]
newlist = ["hello" for x in fruits]
newlist = [x if x != "banana" else "orange" for x in fruits]

# sort()
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# to sort descending, use the keyword argument reverse = True
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)

# Customize Sort Function
# You can also customize your own function by using the keyword argument key = function.

# The function will return a number that will be used to sort the list (the lowest number first):


def myfunc(n):
    return abs(n - 50)


# Sort the list based on how close the number is to 50:
thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)

# Case Insensitive Sort
# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)


# reverse()
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# copy()
# You can't do such thing. Because whatever changes you make to your list1, the list2 will also automatically get updated. So that's why you should use copy instead of list2 = list1
list1 = ["apple", "banana", "cherry"]
list2 = list1
print(list2)
list1.append("watermelon")
print(list1)
print(list2)

list2 = list1.copy()
print(list2)
list1.append("new fruit")
print(list1)
print(list2)

# another method for copying one list according to the another
thislist = ["apple", "banana", "cherry"]
# using list method
mylist = list(thislist)
print(mylist)

# another method using the slice operator
thislist = ["apple", "banana", "cherry"]
myNewList = thislist[:]
print(myNewList)

# Join two lists
# 1st way
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

# 2nd way
for x in list2:
    list1.append(x)
print(list1)

# 3rd way
# extend()
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

# list methods
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
fruits = ['apple', 'banana', 'cherry']
x = fruits.count("cherry")
print(x)
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list


# Python Tuples
mytuple = ("apple", "banana", "cherry")

# Tuples are used to store multiple items in a single variable.A tuple is a collection which is ordered and unchangeable.
#
thistuple = ("apple", "banana", "cherry")
print(thistuple)


thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

thistuple = ("apple",)
print(type(thistuple))

# NOT a tuple
thistuple = ("apple")
print(type(thistuple))

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

tuple1 = ("abc", 34, True, 40, "male")
# <class 'tuple'>

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))


# note the double round-brackets
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

# Access Tuple Items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])


thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])


thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")


# Update Tuples
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


# Add Items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)


thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple)  # this will raise an error because the tuple no longer exists


# Unpacking a Tuple
fruits = ("apple", "banana", "cherry")

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


# using asterisk *
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)


fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)


# Loop Tuples
# Loop Through a tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

# Loop through the index numbers
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])


thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1


# Join Tuples
# Join Two Tuples
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)


fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)


# Tuple Methods
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found


# Python Sets
myset = {"apple", "banana", "cherry"}


thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)


thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)


thisset = {"apple", "banana", "cherry"}

print(len(thisset))


set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

set1 = {"abc", 34, True, 40, "male"}

myset = {"apple", "banana", "cherry"}
print(type(myset))

# the set() constructor
thisset = set(("apple", "banana", "cherry"))  # note the double round-brackets
print(thisset)

# access items
thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)


thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)


thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset)


# Add set items
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)


thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)


thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

# Remove set items
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)


thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)


thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)


thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)


thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)


# Loop items
thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)


# Join sets
# union()
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)


# |
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 | set4
print(myset)

# update()
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

# intersection()
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

# &
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)

# intersection_update()
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)


set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)

# difference()
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3)

# difference_update
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)

# symmetric_difference()
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)

# ^
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2
print(set3)

# symmetric_difference_update()
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)


# set methods
# add()	 	Adds an element to the set
# clear()	 	Removes all the elements from the set
# copy()	 	Returns a copy of the set
# difference()	-	Returns a set containing the difference between two or more sets
# difference_update()	-=	Removes the items in this set that are also included in another, specified set
# discard()	 	Remove the specified item
# intersection()	&	Returns a set, that is the intersection of two other sets
# intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	 	Returns whether two sets have a intersection or not
# issubset()	<=	Returns whether another set contains this set or not
# 	<	Returns whether all items in this set is present in other, specified set(s)
# issuperset()	>=	Returns whether this set contains another set or not
# 	>	Returns whether all items in other, specified set(s) is present in this set
# pop()	 	Removes an element from the set
# remove()	 	Removes the specified element
# symmetric_difference()	^	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
# union()	|	Return a set containing the union of sets
# update()	|=	Update the set with the union of this set and others


# Python Dictionaries
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["brand"])


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(thisdict)

print(len(thisdict))

thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(type(thisdict))


thisdict = dict(name="John", age=36, country="Norway")
print(thisdict)

# Access Dictionary Items
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]

x = thisdict.get("model")

x = thisdict.keys()

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.keys()
print(x)  # before the change
car["color"] = "white"
print(x)  # after the change

x = thisdict.values()

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.values()
print(x)  # before the change
car["year"] = 2020
print(x)  # after the change


car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.values()
print(x)  # before the change
car["color"] = "red"
print(x)  # after the change


x = thisdict.items()


car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.items()
print(x)  # before the change
car["year"] = 2020
print(x)  # after the change


car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.items()
print(x)  # before the change
car["color"] = "red"
print(x)  # after the change

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")


# Change Values
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["year"] = 2018

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"year": 2020})


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["color"] = "red"
print(thisdict)


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"color": "red"})


# Remove Dictionary Items
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.pop("model")
print(thisdict)


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.popitem()
print(thisdict)


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict["model"]
print(thisdict)


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict
# this will cause an error because "thisdict" no longer exists.
print(thisdict)


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.clear()
print(thisdict)

# Loop Through a Dictionary
for x in thisdict:
    print(x)


for x in thisdict:
    print(thisdict[x])


for x in thisdict.values():
    print(x)


for x in thisdict.keys():
    print(x)


for x, y in thisdict.items():
    print(x, y)


# Copy Dictionaries
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = thisdict.copy()
print(mydict)


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = dict(thisdict)
print(mydict)


# Nested Dictionaries
myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}


child1 = {
    "name": "Emil",
    "year": 2004
}
child2 = {
    "name": "Tobias",
    "year": 2007
}
child3 = {
    "name": "Linus",
    "year": 2011
}

myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}


print(myfamily["child2"]["name"])


for x, obj in myfamily.items():
    print(x)

    for y in obj:
        print(y + ':', obj[y])


# Python Dictionary Methods
# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary


# Python If ... Else
a = 33
b = 200
if b > a:
    print("b is greater than a")


a = 33
b = 200
if b > a:
    print("b is greater than a")  # you will get an error

a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")


if a > b:
    print("a is greater than b")

a = 2
b = 330
print("A") if a > b else print("B")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")


a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")


a = 33
b = 200
if not a > b:
    print("a is NOT greater than b")


x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")


a = 33
b = 200

if b > a:
    pass


# Python Match Statement
""" match expression:
  case x:
    code block
  case y:
    code block
  case z:
    code block """


day = 4
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")


day = 4
match day:
    case 6:
        print("Today is Saturday")
    case 7:
        print("Today is Sunday")
    case _:
        print("Looking forward to the Weekend")


day = 4
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Today is a weekday")
    case 6 | 7:
        print("I love weekends!")


month = 5
day = 4
match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("A weekday in April")
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("A weekday in May")
    case _:
        print("No match")


# While Loops
i = 1
while i < 6:
    print(i)
    i += 1

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)


i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")


# Foor Loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)


for x in "banana":
    print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break


fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)


for x in range(6):
    print(x)

for x in range(2, 6):
    print(x)


for x in range(2, 30, 3):
    print(x)


for x in range(6):
    print(x)
else:
    print("Finally finished!")


for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("Finally finished!")


# Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)


for x in [0, 1, 2]:
    pass
