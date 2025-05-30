# Day 3 – Functions & Object-Oriented Programming

# A foundation for building structured, modular programs using functions, and then explore the foundations of object-oriented programming (OOP) to create reusable and organized code. Today is a major step toward writing clean, efficient, and maintainable code.

#=============================================================
#! Section 1: Functions – The Building Blocks of Modularity
#=============================================================
'''
A function is a named, reusable block of code designed to perform a specific task.

Why use functions?
- Reduces code duplication (DRY: Don't Repeat Yourself)
- Improves readability and maintainability
- Allows better testing and debugging

Syntax:

def function_name(parameters):
    # code block
    return result (optional)

A function is only executed when called.
'''

# Function with no parameters and no return value
def greet():
    print("Hello, welcome to Python!")

greet()  # Function call

# Function with a parameter
def greet_user(name):
    print(f"Hello, {name}! Welcome back.")

greet_user("Jules")

# Function with return value
def square(number):
    return number * number

result = square(5)
print("Square of 5 is", result)

'''
🧠 Tip: Always name your functions with action words like `calculate_tax`, `send_email`, or `print_report` to describe what they do.
'''

#=============================================================
#! Section 2: Parameters, Scope, and Return Values
#=============================================================
'''
- Parameter: a variable defined in the function header.
- Argument: the actual value passed to the function.
- Scope: where a variable can be accessed (local or global).
- return: sends back a result to the function caller.

All function parameters are local unless specified otherwise. Once the function ends, local variables are destroyed and can't be accessed outside.
'''

def add_values(a, b):
    return a + b

x = 3
y = 7
sum_result = add_values(x, y)
print("Sum:", sum_result)

# Local scope – variable only exists within the function
def show_number():
    number = 10
    print("Local number:", number)

show_number()
# print(number)  # Error: 'number' is not defined globally

#=============================================================
#! Section 3: Type Hints and Default Parameters
#=============================================================
'''
Python is dynamically typed, but starting with version 3.5+, it supports optional type hints.

Type hints:
- Improve readability and clarity
- Aid in catching bugs using tools like mypy

Default parameters:
- Used when an argument is not provided
- Must come after required parameters
'''

def multiply_values(a: int, b: int = 2) -> int:
    return a * b

print(multiply_values(5))      # b defaults to 2
print(multiply_values(5, 3))   # Overrides default b

'''
⚠️ Default parameters must come after required ones in function signatures.
'''

#=============================================================
#! Section 4: Object-Oriented Programming – Introduction
#=============================================================
'''
Object-Oriented Programming (OOP) is a programming paradigm that organizes code around objects.

Think of objects like real-world things: a car, a dog, a book.
Each object has:
- Attributes (data) → like color, age, title
- Methods (behavior) → like drive(), bark(), read()

Main principles of OOP:
1. Encapsulation - Bundling data and code that manipulates it
2. Abstraction - Hiding unnecessary details
3. Inheritance - Sharing behavior between related classes
4. Polymorphism - Using shared method names for different behavior

In Python, we define objects using classes.
A class is like a blueprint. You can use a class to create multiple similar objects.

Every object is an instance of a class.
'''

# Basic class example
class Dog:
    def __init__(self, name, age):
        self.name = name     # instance attribute
        self.age = age       # instance attribute

    def bark(self):         # instance method
        print(f"{self.name} says: Woof!")

my_dog = Dog("Buddy", 4)
print("Dog's name:", my_dog.name)
print("Dog's age:", my_dog.age)
my_dog.bark()

#=============================================================
#! Section 5: Understanding __init__ (Constructor)
#=============================================================
'''
The __init__ method is a special method in Python classes.
It's called automatically when a new object is created.

Why use it?
- It lets you initialize the object with custom values
- Without __init__, all attributes would have to be set manually after creation

Syntax:

def __init__(self, param1, param2):
    self.param1 = param1
    self.param2 = param2

Note: `self` refers to the current instance of the class. It must always be the first parameter in instance methods.
'''

# Without constructor (manual)
class Cat:
    name = "Luna"
    age = 2

my_cat = Cat()
print(my_cat.name, my_cat.age)

# With constructor
class Bird:
    def __init__(self, name, age):
        self.name = name
        self.age = age

my_bird = Bird("Milo", 3)
print(my_bird.name, my_bird.age)

#=============================================================
#! Section 6: Attributes, Methods, and Encapsulation
#=============================================================
'''
Attributes are variables that belong to the object.
Methods are functions defined inside the class that operate on the object.
Encapsulation keeps related logic bundled within the object.

Use dot notation to access attributes and methods.
'''

class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return 3.14159 * (self.radius ** 2)

    def describe(self):
        print(f"This circle has radius {self.radius} and area {self.area():.2f}")

c1 = Circle(5)
c1.describe()

#=============================================================
#! Section 7: Mini Projects
#=============================================================
'''
Project 1: Function-Based Calculator
-----------------------------------
Build a calculator using separate functions for operations:
- add(x, y)
- subtract(x, y)
- multiply(x, y)
- divide(x, y)

Include user input and a loop to repeat until the user chooses to exit.
'''

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Cannot divide by zero"

while True:
    print("\nCalculator Menu")
    print("1. Add 2. Subtract 3. Multiply 4. Divide 5. Exit")
    choice = input("Choose an option: ")

    if choice == "5": break

    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        continue

    if choice == "1": print("Result:", add(a, b))
    elif choice == "2": print("Result:", subtract(a, b))
    elif choice == "3": print("Result:", multiply(a, b))
    elif choice == "4": print("Result:", divide(a, b))
    else: print("Invalid option")

'''
Project 2: Pet Class
--------------------
Create a Pet class with attributes name, species, and sound.
Add a method speak() that introduces the pet.
'''

class Pet:
    def __init__(self, name: str, species: str, sound: str):
        self.name = name
        self.species = species
        self.sound = sound

    def speak(self):
        print(f"Hi, I'm {self.name}, a {self.species}, and I say '{self.sound}'!")

my_pet = Pet("Whiskers", "cat", "meow")
my_pet.speak()

#=============================================================
#! Section 8: Homework Assignments
#=============================================================
'''
📗 1. Book Class
-----------------
Create a class called Book with:
- Attributes: title, author, year
- Method: describe() that prints all info
'''

class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def describe(self):
        print(f"'{self.title}' by {self.author} ({self.year})")

b = Book("1984", "George Orwell", 1949)
b.describe()

'''
📗 2. Quiz App Using Functions
------------------------------
Build a simple quiz with:
- 3 questions (multiple choice or true/false)
- A function to ask each question
- Score counter
'''

def ask_question(prompt, correct_answer):
    answer = input(prompt)
    return answer.lower() == correct_answer.lower()

score = 0
if ask_question("What is 2 + 2? ", "4"): score += 1
if ask_question("What color is the sky on a clear day? ", "blue"): score += 1
if ask_question("True or False: Python is a snake. ", "false"): score += 1

print(f"You got {score}/3 correct.")

'''
📗 3. Bonus - Extend your Calculator
------------------------------------
Add support for:
- Power (e.g. x ** y)
- Modulus (e.g. x % y)
- Input validation (check for non-numeric input)
'''

def power(x, y): return x ** y
def mod(x, y): return x % y
