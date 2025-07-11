# Python Functions
# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result

# Creating a Function
# In Python we can create a function by using the keyword def:

def my_function():
    print("Hello from a function")

# Calling a Function
# In order to call a function we can use the name of the function followed by parenthesis:


def my_function():
    print("Hello from a function")


my_function()

# Arguments
# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
# The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:
# The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:


def my_function(fname):
    print(fname + "Daryayee")


my_function("Ali ")
my_function("Tamana ")
my_function("Sahar ")

# Difference Between Paramaters or Arguments
# A parameter is the variable listed inside the parentheses in the function definition.

# An argument is the value that is sent to the function when it is called.

# Number of Arguments
# The number of parameters and arguments should be equal in a function.


def my_function(fname, lname):
    print(fname + " " + lname)


my_function("Ahmad", "Daryayee")

# This will raise an error
""" def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Ahmad") """

# Arbitrary Arguments, *args
# If you do not know how many arguments you will pass as parameters, then add an * before the parameter name.


def myfunc(*vip):
    print("The most important guy is " + vip[1])


myfunc("Darya", "Alizada", "Hussaini")

# Keyword Arguments
# You can also send arguments with the key = value syntax.

# This way the order of the arguments does not matter.


def myfunc(vip3, vip2, vip1):
    print("The most important guy is " + vip2)


myfunc(vip1="Darya", vip2="Alizada", vip3="Hussaini")

# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

# This way the function will receive a dictionary of arguments, and can access the items accordingly:


def myfunc(**friends):
    print("My close friend is " + friends["lname"])


myfunc(fname="Tamana", lname="Alizada")

# Default Parameter Value
# The following example shows how to use a default parameter value.

# If we call the function without argument, it uses the default value:


def myfunction(country="Afghanistan"):
    print("I am from " + country)


myfunction("Kazakhstan")
myfunction("Tajikstan")
myfunction()
myfunction("Brazil")

# Passing a List as an Argument
# You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.

# E.g. if you send a List as an argument, it will still be a List when it reaches the function:


def myfunction(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]
myfunction(fruits)

# Return Values
# To let a function return a value, use the return statement:


def myfunction(x):
    return 5 * x


print(myfunction(3))
print(myfunction(5))
print(myfunction(9))

# The pass Statement
# function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.


def myfunction():
    pass

# having an empty function definition like this, would raise an error without the pass statement

# Positional-Only Arguments
# You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
# To specify that a function can have only positional arguments, add , / after the arguments.


def my_function(x, /):
    print(x)


my_function(3)

# Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:


def my_function(x):
    print(x)


my_function(x=3)

# BUT this will raise an error:


def my_function(x, /):
    print(x)


my_function(x=3)

# Keyword-Only Arguments
# To specify that a function can have only keyword arguments, add *, before the arguments:


def my_function(*, x):
    print(x)


my_function(x=3)

# Without the *, you are allowed to use positional arguments even if the function expects keyword arguments:


def my_function(x):
    print(x)


my_function(3)

# BUT this will raise an error:


def my_function(*, x):
    print(x)


my_function(3)

# Combine Positional-Only and Keyword-Only
# You can combine the two argument types in the same function.

# Any argument before the / , are positional-only, and any argument after the *, are keyword-only.


def my_function(a, b, /, *, c, d):
    print(a + b + c + d)


my_function(5, 6, c=7, d=8)

# Recursion
# function recursion means that calling a function itself.


def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("Recursion Example Results:")
tri_recursion(6)

# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.

x = lambda a: a + 10
print(x(5))

# Lambda functions can take any number of arguments:
x = lambda a, b: a * b
print(x(5, 6))

x = lambda a, b, c: a + b + c
print(x(3, 4, 5))

def myFunc(n):
    return lambda a: a * n

# Use that function definition to make a function that always doubles the number you send in:
x = myFunc(2)
print(x(11))

# Or, use the same function definition to make a function that always triples the number you send in:z
x = myFunc(3)
print(x(44))

# Arrays:
# Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.

# Note: This page shows you how to use LISTS as ARRAYS, however, to work with arrays in Python you will have to import a library, like the NumPy library.

# What is an Array?
# An array is a special variable, which can hold more than one value at a time.

car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"

# You can access to an element of an array by referring to the index number of that.

cars = ['Ford', 'Volvo', 'BMW']
x = cars[0]
print(x)

# also by using index number we can modify the elements of our array.

cars[0] = "Toyota"

x = len(cars)

# Looping Array Elements

for x in cars:
    print(x)

cars.append("Honda")
cars.pop(1)
cars.remove("Volvo")
# Note: The list's remove() method only removes the first occurrence of the specified value.
# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list


# OOP
# In OOP, you create objects. Each object can store data and have functions that work with that data.

# Advantages of OOP
# Provides a clear structure to programs
# Makes code easier to maintain, reuse, and debug
# Helps keep your code DRY (Don't Repeat Yourself)
# Allows you to build reusable applications with less code
# Tip: The DRY principle means you should avoid writing the same code more than once. Move repeated code into functions or classes and reuse it.

# What are Classes and Objects?
# Classes and objects are the two core concepts in object-oriented programming.

# A class defines what an object should look like, and an object is created based on that class. For example:

# Class	Objects
# Fruit	Apple, Banana, Mango
# Car	Volvo, Audi, Toyota
# When you create an object from a class, it inherits all the variables and functions defined inside that class.


# Python Classes/Objects
# Python is an object oriented programming language.

# Almost everything in Python is an object, with its properties and methods.

# A Class is like an object constructor, or a "blueprint" for creating objects.

class MyClass:
    x = 5


p1 = MyClass()
print(p1.x)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)

print(p1.name)
print(p1.age)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)

print(p1)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"


p1 = Person("John", 36)

print(p1)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("John", 36)
p1.myfunc()


# Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.


# The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

# It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class:

# Use the words mysillyobject and abc instead of self:

class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)


p1 = Person("John", 36)
p1.myfunc()

# modify object properties
p1.age = 40

del p1.age

del p1


class Person:
    pass

# Python Inheritance
# Parent class
# Child class


# Parent class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# Use the Person class to create an object, and then execute the printname method:


x = Person("John", "Doe")
x.printname()


# Child class
class Student(Person):
    pass
# Note: Use the pass keyword when you do not want to add any other properties or methods to the class.


x = Student("Mike", "Olsen")
x.printname()


""" class Student(Person):
    def __init__(self, fname, lname):
        # add properties etc.


class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)


class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname) """


# Add Properties
# Add a property called graduationyear to the Student class:

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2019

# Add a year parameter, and pass the correct year when creating objects:


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year


x = Student("Mike", "Olsen", 2019)


# Add a method called welcome to the Student class:
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname,
              "to the class of", self.graduationyear)
