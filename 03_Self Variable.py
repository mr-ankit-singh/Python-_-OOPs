'''
╔══════════════════════════════════════════════════════════════════╗
║                    Self Variable in Python                       ║
╚══════════════════════════════════════════════════════════════════╝

   - self is a reference variable or implicit variable which is
     always pointing to current object.
   - self represents the instance of the class.
   - By using the "self" keyword we can access the attributes
     and methods of the class in python.
   - To refer current object we use self variable.
   - It binds the attributes with the given arguments.
   - Self is always pointing to Current Object.
   - Self is the first argument to be passed in Constructor
     and Instance Method.
   - self can be used to declare instance variable and to
     access variables.
   - Self is a convention and not a Python keyword.

   Note: Python Virtual Machine is responsible to provide value
         for self argument.
         We are not required to provide it explicitly.
'''


# ══════════════════════════════════════════════════════════════════
#  __dict__ AND help() — CLASS KI INFO DEKHO
# ══════════════════════════════════════════════════════════════════

class Student:
    ''' This is documentation string '''

print(Student.__dict__)          # class ke saare attributes dict mein
help(Student)                    # documentation string dikhata hai


# ══════════════════════════════════════════════════════════════════
#  SELF — INSTANCE VARIABLES DECLARE AUR ACCESS KARNA
# ══════════════════════════════════════════════════════════════════
'''
Self se Instance Variables
   - self.variable_name  →  instance variable declare karta hai
   - Har object ka apna alag data hota hai
   - self ke bina variables class ke bahar accessible nahi honge
'''

class Employee:
    def __init__(self, Id, Name, Age, Gender):
        self.Id     = Id
        self.Name   = Name
        self.Age    = Age
        self.Gender = Gender

    def info(self):
        print('--' * 10)
        print("My Id is    :", self.Id)
        print("My name is  :", self.Name)
        print(f"My Age is   : {self.Age}")
        print("My gender is: {}".format(self.Gender))


# Creating objects
e1 = Employee(1, 'Ankit Singh', 20, 'Male')
e2 = Employee(2, 'Sophia',      18, 'Female')

e1.info()
e2.info()


# ══════════════════════════════════════════════════════════════════
#  SELF AUR OBJECT — SAME ADDRESS POINT KARTE HAIN
# ══════════════════════════════════════════════════════════════════
'''
Self is always pointing to Current Object
   - self aur object dono ek hi memory address point karte hain.
   - id() se address dekh sakte hain.
   - Ye prove karta hai ki self == current object.
'''

class Check:
    def __init__(self):
        print("Address of self          =", id(self))


obj = Check()
print("Address of class object  =", id(obj))

# Output dono ka same aayega — self aur obj ek hi object hai


# ══════════════════════════════════════════════════════════════════
#  SELF KA NAAM BADAL SAKTE HAIN
# ══════════════════════════════════════════════════════════════════
'''
Self ek Convention hai — Keyword Nahi
   - self ki jagah koi bhi naam use kar sakte hain.
   - Lekin self likhna industry standard hai — hamesha self likho.
   - Python Virtual Machine pehle argument ko hi current object
     maanta hai — naam kuch bhi ho.
'''

class Student:
    def __init__(this, name):      # self ki jagah 'this' likha
        this.name = name

    def display(this):
        print("Name:", this.name)


s = Student("Ankit")
s.display()                        # bilkul kaam karega


# ══════════════════════════════════════════════════════════════════
#  SELF — INSTANCE METHOD VS CLASS METHOD
# ══════════════════════════════════════════════════════════════════
'''
Self kahan use hota hai
   - Instance Method  →  self use karta hai  (most common)
   - Class Method     →  cls use karta hai   (@classmethod)
   - Static Method    →  na self na cls      (@staticmethod)
'''

class Employee:
    company = "Google"             # class variable

    def __init__(self, name):
        self.name = name           # instance variable

    # instance method — self chahiye
    def getName(self):
        return self.name

    # class method — cls chahiye, self nahi
    @classmethod
    def getCompany(cls):
        return cls.company

    # static method — na self na cls
    @staticmethod
    def greet():
        print("Welcome to the company!")


e = Employee("Ankit")
print(e.getName())                 # Ankit
print(Employee.getCompany())       # Google
Employee.greet()                   # Welcome to the company!


# ══════════════════════════════════════════════════════════════════
#  SELF SE DYNAMICALLY ATTRIBUTE ADD KARO
# ══════════════════════════════════════════════════════════════════
'''
Dynamic Attribute
   - self se object ke baad bhi nayi attribute add kar sakte hain.
   - Ye Python ki flexibility hai.
'''

class Student:
    def __init__(self, name):
        self.name = name


s = Student("Ankit")
s.age = 20                         # baad mein add kiya
print(s.name)                      # Ankit
print(s.age)                       # 20
print(s.__dict__)                  # {'name': 'Ankit', 'age': 20}


# ══════════════════════════════════════════════════════════════════
#  FLOW
# ══════════════════════════════════════════════════════════════════
'''
Flow
   Object banao  →  e1 = Employee(1, "Ankit", 20, "Male")
         ↓
   Python automatically self = e1 pass karta hai
         ↓
   __init__(self, ...)  →  self.name = "Ankit" set hota hai
         ↓
   Method call karo  →  e1.info()
         ↓
   Python automatically self = e1 pass karta hai
         ↓
   self.name se "Ankit" access hota hai
         ↓
   Dono self aur e1 same memory address point karte hain
'''


# ══════════════════════════════════════════════════════════════════
#  QUICK REVISION
# ══════════════════════════════════════════════════════════════════
'''
Quick Revision
   ┌──────────────────────────┬─────────────────────────────────────┐
   │ self                     │ Current object ka reference         │
   │ Implicit variable        │ PVM automatically value deta hai    │
   │ self keyword?            │ Nahi — convention hai               │
   │ self naam badal sakte?   │ Haan — lekin mat karo               │
   │ self ka address          │ Object ke address se same hota hai  │
   │ Instance variable        │ self.variable se declare hota hai   │
   │ Instance method          │ Pehla argument hamesha self         │
   │ Class method             │ self nahi — cls use hota hai        │
   │ Static method            │ Na self na cls                      │
   │ Dynamic attribute        │ Baad mein bhi self se add ho sakta  │
   │ __dict__                 │ Object ke saare attributes          │
   └──────────────────────────┴─────────────────────────────────────┘
'''