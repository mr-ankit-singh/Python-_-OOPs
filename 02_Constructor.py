'''
╔══════════════════════════════════════════════════════════════════╗
║                  __init__ Constructor in Python                  ║
╚══════════════════════════════════════════════════════════════════╝

   - Constructors are generally used for instantiating an object.
   - __init__ is a special method which is first run as soon as
     the object is created.
   - __init__ method is also known as constructor.
   - It takes self argument and can also take further arguments.
   - The main purpose of the constructor is to declare and
     initialize instance variables.
   - The constructor takes atleast one argument (which is self).
   - Note: The __init__() function is called automatically every
     time the class is being used to create a new object.
     The constructor will be executed automatically if we are
     creating object.

   Syntax of constructor declaration:
        def __init__(self):
            # body of the constructor

   Types of Constructors:
   ┌─────────────────────────────────────────────────────────────┐
   │  a) Default Constructor                                     │
   │  b) Parameterized Constructor                               │
   └─────────────────────────────────────────────────────────────┘
'''


# ══════════════════════════════════════════════════════════════════
#  a) DEFAULT CONSTRUCTOR
# ══════════════════════════════════════════════════════════════════
'''
Default Constructor
   - The default constructor is a simple constructor which doesn't
     accept any arguments.
   - Its definition has only one argument which is a reference to
     the instance being constructed (self).
   - Agar hum koi argument nahi dete toh default constructor
     use hota hai.
'''

class GeekforGeeks:

    # default constructor
    def __init__(self):
        self.geek = "GeekforGeeks"

    # a method for printing data members
    def print_Geek(self):
        print(self.geek)


# creating object of the class
obj = GeekforGeeks()

# calling the instance method using the object obj
obj.print_Geek()


# ══════════════════════════════════════════════════════════════════
#  b) PARAMETERIZED CONSTRUCTOR
# ══════════════════════════════════════════════════════════════════
'''
Parameterized Constructor
   - Constructor with parameters is known as parameterized
     constructor.
   - The parameterized constructor takes its first argument as a
     reference to the instance being constructed known as self and
     the rest of the arguments are provided by the programmer.
   - Object banate waqt values pass karni padti hain.
'''

class Student:
    def __init__(self, name, rollno):
        print("Constructor Execution....")
        self.name   = name
        self.rollno = rollno

    def display(self):
        print("Method Execution...")
        print(f"My name is {self.name}")
        print("My rollno is {}".format(self.rollno))


# constructor execution
s = Student('Nandini', 100)

# method execution
s.display()


# ══════════════════════════════════════════════════════════════════
#  NO METHOD / CONSTRUCTOR OVERLOADING
# ══════════════════════════════════════════════════════════════════
'''
No Concept of Constructor Overloading in Python
   - Python mein constructor overloading nahi hoti.
   - Agar ek se zyada __init__ define karo toh sirf last
     wala kaam karta hai — baaki overwrite ho jaate hain.
   - Java/C++ mein overloading hoti hai — Python mein nahi.
'''

class Student:
    def __init__(self):
        print("Constructor Execution....")        # ye overwrite ho jaayega

    def __init__(self, name):
        print("Constructor Execution....")        # sirf ye chalega
        self.name = name
        print(self.name)


# Error — kyunki pehla __init__ overwrite ho gaya
# obj1 = Student()      ← TypeError: __init__() missing argument

# Sirf doosra constructor execute hoga
obj2 = Student('Ankit')


# ══════════════════════════════════════════════════════════════════
#  DEFAULT PARAMETER VALUE — Overloading ka alternative
# ══════════════════════════════════════════════════════════════════
'''
Default Parameter — Overloading ki jagah use karo
   - Python mein overloading nahi hoti.
   - Default values deke dono cases handle kar sakte hain.
   - Agar argument diya → woh use hoga.
   - Agar argument nahi diya → default value use hogi.
'''

class Student:
    def __init__(self, name="Unknown", rollno=0):
        self.name   = name
        self.rollno = rollno

    def display(self):
        print(f"Name   : {self.name}")
        print(f"Rollno : {self.rollno}")


s1 = Student()                   # default values use hongi
s2 = Student("Ankit", 100)       # passed values use hongi

s1.display()
s2.display()


# ══════════════════════════════════════════════════════════════════
#  __del__ — DESTRUCTOR
# ══════════════════════════════════════════════════════════════════
'''
__del__ Destructor
   - Jab object destroy hota hai tab __del__ automatically
     call hota hai.
   - Constructor ka opposite hai destructor.
   - Memory free karne ke kaam aata hai.
   - del keyword se object manually destroy kar sakte hain.
'''

class Student:
    def __init__(self, name):
        self.name = name
        print(f"Object banaya  : {self.name}")

    def __del__(self):
        print(f"Object destroy : {self.name}")


s = Student("Ankit")
del s                            # manually destroy kiya


# ══════════════════════════════════════════════════════════════════
#  __dict__ — OBJECT KE SAARE ATTRIBUTES DEKHO
# ══════════════════════════════════════════════════════════════════
'''
__dict__
   - Object ke andar jo bhi instance variables hain
     unhe dictionary format mein dikhata hai.
   - Debugging ke kaam aata hai.
'''

class Student:
    def __init__(self, name, rollno):
        self.name   = name
        self.rollno = rollno


s = Student("Ankit", 100)
print(s.__dict__)                # {'name': 'Ankit', 'rollno': 100}


# ══════════════════════════════════════════════════════════════════
#  FLOW
# ══════════════════════════════════════════════════════════════════
'''
Flow
   Class define karo
         ↓
   Object banao  →  __init__ automatically call hota hai
         ↓
   Arguments pass karo  →  Instance variables set hote hain
         ↓
   Methods call karo  →  self se variables access hote hain
         ↓
   Object ka kaam khatam  →  __del__ call hota hai
         ↓
   Memory free ho jaati hai
'''


# ══════════════════════════════════════════════════════════════════
#  QUICK REVISION
# ══════════════════════════════════════════════════════════════════
'''
Quick Revision
   ┌──────────────────────────┬─────────────────────────────────────┐
   │ __init__                 │ Constructor — object bante hi chale │
   │ Default Constructor      │ Koi argument nahi leta              │
   │ Parameterized Constructor│ Arguments leta hai                  │
   │ Overloading              │ Python mein nahi hoti               │
   │ Last __init__            │ Sirf ye execute hota hai            │
   │ Default Parameter        │ Overloading ka Python alternative   │
   │ __del__                  │ Destructor — object destroy hone pe │
   │ __dict__                 │ Object ke saare attributes dict mein│
   │ self                     │ Current object ka reference         │
   └──────────────────────────┴─────────────────────────────────────┘
'''