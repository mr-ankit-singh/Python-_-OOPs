'''
╔══════════════════════════════════════════════════════════════════╗
║           Object Oriented Programming in Python                  ║
╚══════════════════════════════════════════════════════════════════╝

   - Python is an object oriented programming language.
   - It aims to implement real-world entities like inheritance,
     polymorphisms, encapsulation, etc. in the programming.
   - The main concept of OOPs is to bind the data and the functions
     that work on that together as a single unit so that no other
     part of the code can access this data.
   - Python allows developers to develop applications using the OOPs
     approach with the major focus on code reusability.
   - It is very easy to create classes and objects in Python.

   Major principles of object-oriented programming system are :
   ┌─────────────────────────────┐
   │  1. Class                   │
   │  2. Object                  │
   │  3. Method                  │
   │  4. Inheritance             │
   │  5. Polymorphism            │
   │  6. Data Abstraction        │
   │  7. Encapsulation           │
   └─────────────────────────────┘
'''


# ══════════════════════════════════════════════════════════════════
#  CLASS
# ══════════════════════════════════════════════════════════════════
'''
Class
   - A Class is like an object constructor, or a "blueprint" for
     creating objects.
   - The class can be defined as a collection of objects.
   - It is a logical entity that has some specific attributes
     and methods.
   - A Class in Python is a logical grouping of data and functions.
   - It gives the freedom to create data structures that contains
     arbitrary content and hence easily accessible.
   - To create a class, use the keyword 'class'.

   Syntax:
        class ClassName:
                <statement-1>
                .
                .
                <statement-N>
'''


# ══════════════════════════════════════════════════════════════════
#  OBJECT
# ══════════════════════════════════════════════════════════════════
'''
Objects
   - The object is an entity that has state and behavior.
   - It may be any real-world object.
   - Everything in Python is an object, and almost everything has
     attributes and methods.
   - We use the class name to create objects.
   - An object is an instantiation of a class.
   - When class is defined, a template(info) is defined.
   - Memory is allocated only after object instantiation.
'''


# ══════════════════════════════════════════════════════════════════
#  REFERENCE VARIABLE
# ══════════════════════════════════════════════════════════════════
'''
Reference Variable
   - This variable is a reference or a pointer to an object to
     perform operations on that object.
   - Reference variables always points to an object.
'''


# ══════════════════════════════════════════════════════════════════
#  METHOD
# ══════════════════════════════════════════════════════════════════
'''
Method
   - The method is a function that is associated with an object.
   - In Python, a method is not unique to class instances.
   - Any object type can have methods.
'''


# ══════════════════════════════════════════════════════════════════
#  CODE — Class, Object, Reference Variable, Method
# ══════════════════════════════════════════════════════════════════

class Student:
    def __init__(self, rollno, name):
        self.rollno = rollno
        self.name   = name

    def talk(self):
        print("Hello , My Roll number is: ", self.rollno)
        print("My name is:", self.name)


# stu1 is reference variable
stu1 = Student(100, 'Ankit')
print(stu1.name)
print(stu1.rollno)
stu1.talk()

# we can create multiple objects
s1 = Student(200, "Sophia")
s1.talk()


# ══════════════════════════════════════════════════════════════════
#  SELF PARAMETER
# ══════════════════════════════════════════════════════════════════
'''
Self Parameter
   - The self parameter is a reference to the current instance of the class.
   - It is used to access variables that belongs to the class.
   - It is automatically passed with a function call from an object.
'''

class Employee:
    company = "Google"

    def getSalery(self):
        print("Salery is 100k")
        print(f"sophia salery is {self.salery}")


ankit  = Employee()
sophia = Employee()

sophia.salery = 100000
# ankit.getSalery()
sophia.getSalery()


# ══════════════════════════════════════════════════════════════════
#  __init__ CONSTRUCTOR
# ══════════════════════════════════════════════════════════════════
'''
__init__ Constructor
   - __init__ is a special method which is first run as soon as the object is created.
   - __init__ method is also known as constructor.
   - It takes self argument and can also take further arguments.
   - Note: The __init__() function is called automatically every
     time the class is being used to create a new object.
'''

class Employee:
    company = "google"

    def __init__(self):
        print("Employee is created")

    def __init__(self, name, salery, company):
        self.name    = name
        self.salery  = salery
        self.company = company
        print("Emplye detail")

    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salery of the employee is {self.salery}")
        print(f"The company of the employee is {self.company}")


# ankit = Employee()
ankit = Employee("Ankit", 1000000000, "Youtube")
ankit.getDetails()

# show the complete value associated with the object
print(ankit.__dict__)


# ══════════════════════════════════════════════════════════════════
#  FLOW
# ══════════════════════════════════════════════════════════════════
'''
Flow
   Class define karo
         ↓
   Object banao  →  __init__ automatically call hota hai
         ↓
   self se attributes set hote hain
         ↓
   Methods call karo  →  self se attributes access hote hain
         ↓
   __dict__ se sab attributes dekh sakte ho
'''


# ══════════════════════════════════════════════════════════════════
#  QUICK REVISION
# ══════════════════════════════════════════════════════════════════
'''
Quick Revision
   ┌─────────────────┬──────────────────────────────────────────────┐
   │ class           │ Blueprint — template banao                   │
   │ object          │ Class ka instance — actual cheez             │
   │ __init__        │ Constructor — object bante hi chalta hai     │
   │ self            │ Current object ka reference                  │
   │ method          │ Class ke andar ka function                   │
   │ reference var   │ Object ko point karne wala variable          │
   │ __dict__        │ Object ke saare attributes dict mein         │
   └─────────────────┴──────────────────────────────────────────────┘
'''