# Programming Syllabus
## Overview
This is an outline of the entire programming course timeline. It includes expectations on what is to be learned, the projects accompanying each lesson, and a recap of the learned skills. As thorough as this guide may be, it is always the job of the programmer to practice in order to maintain, reinforce, and improve their skills.

**Estimated Time**: 1.5–2 hours/day  
**Tools**: Python 3.x, VS Code or [Replit](https://replit.com/languages/python3)

## Lessons
### 🗓️ Day 1 – What is Programming? + Input, Variables & Data Types
*Introduces the programmer to foundational concepts such as what a program is, what it's used for, and why it's important to learn programming as a skill.*

#### Concepts Introduced:
- What is a program?
- What is a programming language?
- Syntax & indentation
- Data types: `str`, `int`, `float`, `bool`
- Variable assignment
- `print()` function
- `input()` function
- Type casting
- Comments

#### Activities:
- **1**. Install Python or use [Replit](https://replit.com/languages/python3)  
- **2**. Create a file: `basics.py`  
- **3**. Print your name or a fun message  
- **4**. Add a second `print()` line  
    - **4a**. Use variables to store the name or message  
    - **4b**. Call the `input()` function in conjunction with variables
- **5**. Run and debug

### Class Project:
- Profile Generator
    - Ask for name, age, and favorite animal
    - Output a sentence describing the user based on their provided input

### Homework:
- Tip calculator
    - Ask for total + tip %
    - Show the final total
    - Include comments, if necessary

---

### 🗓️ Day 2 – Conditional Logic & Loops
*Revists the previous day's concepts and integrates even more by showcasing new logical operators and looping mechanisms to further enhance the capabilities of the programmer. Checking input, filtering objects, or even printing several values is useful in many situations.*

**Objective**: Use `if`, `elif`, and `else` to make decisions and utilize loops to repeat tasks.

### Concepts Introduced:
- Data types: `list`, `dict`
- Comparison: `==`, `!=`, `>`, `<`, `>=`, `<=`
- Logical ops: `and`, `or`, `not`
- Looping ops: `for`, `while`, `break`, `continue`, `in`
- Boolean expressions
- Flow control

#### Activities:
- **1**. Create a file: `logic.py`  
- **2**. Get two numbers from the user and check which is bigger
- **3**. Make a list of numbers and use a `for` loop to print all of them
    - **3a**. Check for a specific number in the list using the `if` & `in` operators
- **4**. Make a dictionary of numbers and print one
- **5**. Run and debug

### Class Project:
**1**. Login check – Match username and password to stored values  
**2**. Countdown timer using `while` loop

### Homework:
- Temperature checker:
    - ">85"......→ Hot
    - "60–85"..→ Cool
    - "<60"......→ Cold

- Number guessing game (random number 1–10) 
    - User keeps guessing until correct

---

### 🗓️ Day 3 – Functions & Object-Oriented Programming
*Introduces modular and object-oriented programming by covering how to define and reuse functions, the basics of object-oriented structure, and the role of constructors and encapsulation.*

**Objective**: Write clean, modular code using functions and begin working with classes and objects.

#### Concepts Introduced:
- Functions: definition, calling, parameters, return values
- Local vs global scope
- Type hints and default arguments
- Classes and objects
- `__init__()` constructor
- `self` keyword
- Attributes and methods
- Encapsulation
- Dot notation and object interaction

#### Activities:
- **1**. Create a file: `functions.py`
- **2**. Write basic functions using `def`, `return`, and parameters
- **3**. Experiment with scope and type hints
- **4**. Define your first class (`Dog`) and add attributes
- **5**. Add behavior (methods) like `.bark()`
- **6**. Understand and implement `__init__()` for clean object construction
- **7**. Practice encapsulating data inside objects
- **8**. Run and debug

### Class Projects:
- Calculator app using functions with looping input
- Pet class with species, name, and speak method

### Homework:
- Book class
    - Attributes: title, author, year
    - Method: `describe()` prints book info
- Quiz app with 3 questions and score tracker
- Bonus: Extend calculator with power, modulus, and input validation
