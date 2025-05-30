# Day 1 – What is Programming? + Input, Variables & Data Types

#=============================================================
#! Section 0: Introduction
#=============================================================
'''
💻 What is Programming?

Programming is the process of telling a computer what to do by writing a set of instructions.

Think of a computer like a super-fast, very literal robot. It doesn't think for itself — it follows your instructions exactly as you give them.

These instructions are written using something called a programming language.

---

🔤 What is a Programming Language?

A programming language is a special kind of language used to communicate with a computer.

Just like we use English or Spanish to talk to people, we use languages like:

- Python
- JavaScript
- C++
- Java
- Go

...to talk to computers.

Each language has its own rules (called syntax) and is better suited for different kinds of tasks.

---

🧭 What's the Point of Programming?

The goal of programming is to create software — useful or fun tools that run on computers, phones, or even cars.

Examples of what programming can create:

- 🎮 Video games  
- 📱 Mobile apps  
- 🌐 Websites  
- 📊 Business tools  
- 🤖 Robots and AI  
- 🚀 Software for planes, rockets, and self-driving cars  

Programming helps us solve problems, automate tasks, and build new technology.
'''

#=============================================================
#! Section 1: Syntax & Indentation
#=============================================================
'''
In programming, syntax refers to the rules that define the correct structure of code. Like grammar in human languages, programming syntax tells the computer how to interpret our writing.

Python is known for having a clear, readable syntax, which makes it a top choice for beginners. Unlike many other programming languages, Python doesn't use curly braces {} or semicolons ; to define blocks of code. Instead, it uses indentation, making the code look clean and easy to follow. So, let us start by understanding what indentation is.

In Python, indentation isn't just for readability -- it's required. Unlike other languages that use braces or keywords to define code blocks, Python uses whitespace (indentation) via spaces or tabs (and it doesn't matter which is better as long as the codebase is consistent) to group statements together.

Why is indentation important in Python?

Indentation tells Python where blocks of code begin and end. This is especially important in control flow structures like "if", "for", "while", and function definitions. If our indentation is incorrect, Python will raise an error called an "IndentationError".

Look below for examples of correct vs incorrect indentation.

NOTE: *After the usage of a conditional, or while declaring a signature of a function or class (example below and in the next lessons), a colon is used to signify the end of the line and continuation of the definition of the condition, function, or class being defined.*
'''

#? Correct indentation using tabs (runs normally)
'''
if grade > 80:
    print("You passed!")
'''

#? Correct indentation using spaces (runs normally)
'''
if grade > 80:
  print("You passed!")
'''

#? Incorrect indentation (will raise an error described above)
'''
if score > 80: 
print("You passed!")
'''

#=============================================================
#! Section 2: Comments
#=============================================================
'''
Hello, World!

Comments in Python are pretty cool and extremely useful just like in any language. They are normal language ideas expressed within the code, however, they are not compiled nor interpreted in any way that would affect normal operation of the program. The most important idea to understand though is that of letting code "speak" for itself. Overusing comments is generally considered the practice of a beginner and more than often frowned upon. Comments can be powerful and the profressional way is to use them in order to describe "why" something is rather than "what" something is. This allows another programmer to somewhat "get in the head" of the original author(s) and be able to maintain, or even extend existing code.

There are two main flavors of comments and they are the following:

Single line comments: They start with a "#" followed by the comment
Multi line comments: They start with three ' (apostrophes) followed by the comment and then closing with another three ' (apostrophes); just like this long message.

If are using an IDE (integrated development environment), usually you will see comment syntax highlighted and of a darker color than the rest of the code.

Below are examples of comments. Also, comments other than normal single and multi line comments, such as those shown below with importance, inquiry, etc, may require an extension to properly highlight them. Typically something such as "Better Comments" by Aaron Bond will allow for better looking and more prescise comments.
'''

# This is a normal single line comment!
#! This is a comment with importance -- notice the "!" after the "#"
#? This is a comment with inquiry -- notice the "?" after the "#"
#* This is a comment with information -- notice the "*" after the "#"
#TODO: This is a comment as a todo -- notice the "TODO" after the "#"
#NOTE: This is a comment as a note -- notice the "NOTE" after the "#"


'''This is a multi line commnet! It can be used like a single line comment.'''


'''
This is also a multi line comment!
Notice the apostrophes above the first comment and below this one.
'''

#=============================================================
#! Section 3: Variables & Data Types
#=============================================================
'''
Variables are just as you remember from math class: X = 1 or Y = 2, however, in programming the symbols, or variables more rather, are often more complex in nature as there is usually more to define/declare when using them. In math, a simple letter, very short string of letters, or even a more arbitrary symbol may be used to represent the value or object we are trying to calculate with. In programming though, it is much more common (and preferred in professional environments) to use explicit and more descriptive language when defining variables, and sometimes, albeit rarely, their values too. Depending on programming language it may even be required to define the data type expected to be working with as well.

Uniquely, in Python, variables do not need to have a specific data type declared when defining them as the language automatically infers them as lines of code are interpreted. This is called dynamic typing as opposed to strongly typing (explicitly declaring the variable's date type), and means that the language is only semi-type safe due to types being checked only during runtime, or the interpretation of each line of code.

The great thing about Python -- especially since version 3.5 is the addition of something called "type hints". These wonderful sprinkles of syntactical sugar helps understand exactly what data to expect from a function/method, class, or variable.

Below are a few examples of variables being declared without types and then more variables being declared using type hinting.

NOTE: There are data types which can and those that cannot be changed while the program is running. These are called "non-primitive" and "primitive" data types respectivally. Primitive data types are generally immutable, meaning their value cannot be changed once created. Non-primitive data structures are mutable, meaning their contents can be modified. All data types being presented in this lesson are primitives (immutable). These types are generally used to construct more complex and dynamic non-primitive data structures.
'''

#**************************************************
#* Variables without defining types
#**************************************************
user_name = "Jason" #? String, and it is used as "str"
user_age = 28 #? Integer, and it is used as "int"
user_height = 6.2 #? Float or Decimal, and it is used as "float" or "decimal"
is_cool = True #? Boolean, and it is used as "bool"
'''
NOTE: The choice between float and decimal depends on the specific requirements of the application. If speed is paramount and minor precision errors are tolerable, float is the preferred choice. However, when accuracy and exact decimal representation are essential, decimal should be used, even at the cost of performance.
'''

#**************************************************
#* Variables using type hints
#**************************************************
# NOTE: Using type hints requires the variable name, a colon, and the value type as displayed before actually setting the value of the variable.
user_name: str = "Jason"
user_age: int = 28
user_height: float = 6.2
is_cool: bool = True


#=============================================================
#! Section 4: Input & Output
#=============================================================
'''
Using variables is extremely important for programs, however, sometimes a programmer would like to ask the user for a value of their own, and so below is an example of the first two major functions of Python -- input() and print()!
'''

# Get the input of user and set it to a variable.
favorite_color = input("What's your favorite color?: ")

# Display the given color to the terminal/console.
print("Chosen color: ", favorite_color, "\n")


# Another fun example.
favorite_food = input("What's your favorite food?: ")
print("Yum! I like", favorite_food, "too.\n")


# An example of input & output using "string interpolation" added in Python 3.6.
current_age = int(input("Enter you current age: ")) #? Same usage of input() like above except we're using something called "type casting" in order to ensure we're receiving an integer as input

print(f"Next year you'll be {current_age + 1}\n") #? This is using f-strings which is how to use string interpolation in Python