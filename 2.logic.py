# Day 2 – Conditional Logic & Loops

# Deepen your understanding of program flow using if-else logic and loops. This lesson builds on your understanding of input and data types, showing how code can respond and repeat based on logic and conditions.

#=============================================================
#! Section 1: Comparison Operators
#=============================================================
'''
Comparison operators (similar to those taught to us in math class) allow us to compare values and evaluate expressions that result in True or False.

These are essential for writing meaningful conditional logic:

- `==`  → Equal to (e.g. a == b)
- `!=`  → Not equal to (e.g. a != b)
- `>`   → Greater than (e.g. a > b)
- `<`   → Less than (e.g. a < b)
- `>=`  → Greater than or equal to (e.g. a >= b)
- `<=`  → Less than or equal to (e.g. a <= b)

All of these return boolean values: True or False.
'''

x = 10
y = 5
print("x == y:", x == y)   # False
print("x != y:", x != y)   # True
print("x > y:", x > y)     # True
print("x < y:", x < y)     # False
print("x >= y:", x >= y)   # True
print("x <= y:", x <= y)   # False

#=============================================================
#! Section 2: Conditional Logic (if / elif / else)
#=============================================================
'''
Conditional logic lets your program make decisions. This is essential for writing code that behaves differently under different conditions and it usually involves utilizing comparison operators in order to determine the next step or action to take.

In Python, conditional logic is implemented using `if`, `elif`, and `else`.

- `if` checks a condition: if it's true, that block of code runs.
- `elif` (short for 'else if') checks another condition if the first one fails.
- `else` runs if none of the previous conditions were true.

All code blocks in Python must be indented (typically 4 spaces or a tab).
'''

# Basic age checker
age = int(input("Enter your age: "))
if age >= 18:
    print("You're an adult.")
else:
    print("You're a minor.")

# Using multiple branches with elif
score = int(input("Enter your test score: "))
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

'''
🔍 Pro Tip:
Order of your conditions matters. Python checks them top-down and stops at the first match.
'''

#=============================================================
#! Section 3: Logical Operators
#=============================================================
'''
Logical operators allow combining multiple conditions:

- `and`: All conditions must be true.
- `or`: At least one must be true.
- `not`: Reverses the truth value.
'''

# Checking multiple conditions
has_id = input("Do you have an ID? (yes/no): ") == "yes" #? Gets user input and checks if it is equal to 'yes' resulting in True or False.
age = int(input("What is your age? "))

if age >= 18 and has_id:
    print("Entry granted.")
else:
    print("Entry denied.")

# Checking for contradiction
if not has_id:
    print("You cannot proceed without an ID.")

#=============================================================
#! Section 4: Loops (for, while, control flow)
#=============================================================
'''
Loops let us repeat actions.

Use `for` when iterating over a sequence or range (list of integers from start "inclusive" to stop "exclusive" by a step, or specific amount).
Use `while` when the number of repetitions is unknown ahead of time.

Control keywords:
- `break`: exits the loop early
- `continue`: skips the rest of the current loop iteration
'''

# For loop
for i in range(1, 6):
    print(f"This is loop number {i}")

# While loop
counter = 3
while counter > 0:
    print(f"Counter is at {counter}")
    counter -= 1

# Loop with break
for n in range(10):
    if n == 5:
        break
    print("n is:", n)

# Loop with continue
for n in range(5):
    if n == 2:
        continue
    print("This is:", n)
    
#=============================================================
#! Section 5: Data Structures – Lists and Dictionaries
#=============================================================
'''
Python includes powerful built-in data structures that let us organize and store multiple values efficiently.

➤ List:
- Ordered, indexed by integers (starting at 0)
- Mutable (can be changed)
- Created using square brackets []

➤ Dictionary:
- Unordered collection of key-value pairs
- Indexed by keys (which can be strings, numbers, etc.)
- Mutable
- Created using curly braces {}

Use lists when order matters. Use dictionaries when mapping one thing to another.

NOTE: Lists and dictionaries cannot be modified while iterating (looping) over them.
'''

# List example
colors = ["red", "blue", "green", "yellow"]
print("Colors:")
for color in colors:
    print("-", color)

# Check if a value exists in a list
if "blue" in colors:
    print("Blue is in the list!")

# Modify a list
colors.append("purple")
colors.remove("green")
print("Updated list:", colors)

# Dictionary example
grades = {
    "Alice": 95,
    "Bob": 82,
    "Clara": 78
}
print("Clara's grade:", grades["Clara"])

# Add/update/delete from dictionary
grades["Jason"] = 100  # Add
grades["Bob"] = 90     # Update
del grades["Clara"]     # Delete
print("All grades:", grades)

#=============================================================
#! Section 6: Mini Projects
#=============================================================
'''
These mini projects use everything covered today.
'''

## 🔐 Login Checker
username = "admin"
password = "pass123"

user_input = input("Enter username: ")
pass_input = input("Enter password: ")

if user_input == username and pass_input == password:
    print("Access granted.")
else:
    print("Access denied.")

## ⏳ Countdown Timer
n = 10
while n >= 0:
    print(n)
    n -= 1
print("Blast off!")

## 🥕 Food list
favorite_food = ["Pizza", "Ice Cream", "Fruits", "Vegetables", "Other"]
for food in favorite_food:
    print(food)

#=============================================================
#! Section 7: Homework Assignments
#=============================================================
'''
🧊 1. Temperature Checker
Prompt the user to enter a temperature (°F):
- > 85 → "Hot"
- 60 to 85 → "Cool"
- < 60 → "Cold"
'''
temp = int(input("Enter the temperature in Fahrenheit: "))
if temp > 85:
    print("It's hot!")
elif temp >= 60:
    print("It's cool.")
else:
    print("It's cold.")

'''
📋 Print out a list of items such as food, games, movies, etc.
'''
console_companies = ["Sony", "Microsoft", "Nintendo"]
for company in console_companies:
    print(company)

'''
🎯 2. Number Guessing Game
- Use the random module
- Generate a number from 1-10
- Ask the user to guess until they get it right
- Tell them if the guess is too high or too low
'''
import random

secret = random.randint(1, 10)
guess = 0

while guess != secret:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")

print("🎉 You guessed it!")