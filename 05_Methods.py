'''
╔══════════════════════════════════════════════════════════════════╗
║                      Methods in Python                           ║
╚══════════════════════════════════════════════════════════════════╝

   - The method can be anything.
   - Method will be executed only when we call it.
   - A method is a collection of statements that perform some
     specific task and return the result to the caller.
   - A method can perform some specific task without returning
     anything.
   - Methods allow us to reuse the code without retyping the code.

   Types of Methods:
   ┌─────────────────────────────────────────────────────────────┐
   │  a) Instance Method  ( Object Related Method  )             │
   │  b) Class Method     ( Class Related Method   )             │
   │  c) Static Method    ( Utility Method         )             │
   └─────────────────────────────────────────────────────────────┘
'''


# ══════════════════════════════════════════════════════════════════
#  a) INSTANCE METHOD — Object Related Method
# ══════════════════════════════════════════════════════════════════
'''
Instance Method
   - Instance methods are the most common type of methods in Python.
   - They are defined inside a class and require self as the
     first parameter.
   - self automatically refers to the current object.
   - Instance methods can access and modify instance variables
     as well as class variables.
   - Called using object — obj.method()

   Key Points:
   ┌─────────────────────────────────────────────────────────────┐
   │  ✦ Pehla argument hamesha self hota hai                     │
   │  ✦ Object se call hota hai                                  │
   │  ✦ Instance variables access aur modify kar sakta hai       │
   │  ✦ Class variables bhi access kar sakta hai                 │
   └─────────────────────────────────────────────────────────────┘
'''

class Student:
    course = 'BTech'                          # class variable

    def __init__(self, name, rollno):
        self.name   = name                    # instance variable
        self.rollno = rollno                  # instance variable

    # instance method
    def display(self):
        print('Name   :', self.name)
        print('RollNo :', self.rollno)
        print('Course :', self.course)        # class variable bhi access ho sakta


s1 = Student('Ankit',  101)
s2 = Student('Sophia', 102)

s1.display()
print()
s2.display()


# ── Instance Method — Grade Example ──────────────────────────────

class Student:
    def __init__(self, name, marks):
        self.name  = name
        self.marks = marks

    def detail(self):
        print(f"Name  : {self.name}")
        print(f"Marks : {self.marks}")

    def grade(self):
        if self.marks >= 60:
            print("Grade : First  ✅")
        elif self.marks >= 50:
            print("Grade : Second ✅")
        elif self.marks >= 30:
            print("Grade : Third  ✅")
        else:
            print("Grade : Fail   ❌")


n = int(input("Enter number of students: "))
for i in range(n):
    name  = input("Enter name  : ")
    marks = int(input("Enter marks : "))
    std   = Student(name, marks)
    std.detail()
    std.grade()
    print()


# ══════════════════════════════════════════════════════════════════
#  b) CLASS METHOD — Class Related Method
# ══════════════════════════════════════════════════════════════════
'''
Class Method
   - Class methods are bound to the class, not the object.
   - They are defined using the @classmethod decorator.
   - First parameter is cls — which refers to the class itself,
     not the instance.
   - Class methods can access and modify class variables.
   - They cannot access instance variables directly.
   - Can be called using class name or object — both work.

   Key Points:
   ┌─────────────────────────────────────────────────────────────┐
   │  ✦ @classmethod decorator lagana zaroori hai                │
   │  ✦ Pehla argument cls hota hai — self nahi                  │
   │  ✦ Class variables access aur modify kar sakta hai          │
   │  ✦ Instance variables access nahi kar sakta                 │
   │  ✦ ClassName.method() ya object.method() — dono se call    │
   └─────────────────────────────────────────────────────────────┘
'''

class Employee:
    company  = "Google"                       # class variable
    employee_count = 0                        # class variable

    def __init__(self, name, salary):
        self.name   = name
        self.salary = salary
        Employee.employee_count += 1          # har object banne pe count badhao

    # class method
    @classmethod
    def getCompany(cls):
        print(f"Company : {cls.company}")

    # class method — class variable modify karna
    @classmethod
    def changeCompany(cls, new_name):
        cls.company = new_name
        print(f"Company changed to : {cls.company}")

    # class method — factory method pattern
    @classmethod
    def getCount(cls):
        print(f"Total Employees : {cls.employee_count}")


e1 = Employee("Ankit",  100000)
e2 = Employee("Sophia",  80000)

Employee.getCompany()                         # class name se call
e1.getCompany()                               # object se bhi call ho sakta

Employee.changeCompany("Microsoft")           # class variable change kiya
e1.getCompany()                               # Microsoft — sab pe effect
e2.getCompany()                               # Microsoft

Employee.getCount()                           # Total Employees : 2


# ══════════════════════════════════════════════════════════════════
#  c) STATIC METHOD — Utility Method
# ══════════════════════════════════════════════════════════════════
'''
Static Method
   - Static methods are independent — na self na cls.
   - They are defined using the @staticmethod decorator.
   - They cannot access instance variables or class variables
     directly.
   - They are used for utility functions that are related to
     the class but do not need class or instance data.
   - Can be called using class name or object.

   Key Points:
   ┌─────────────────────────────────────────────────────────────┐
   │  ✦ @staticmethod decorator lagana zaroori hai               │
   │  ✦ Na self na cls — koi automatic argument nahi             │
   │  ✦ Instance ya class variables access nahi kar sakta        │
   │  ✦ Utility kaam ke liye use hota hai                        │
   │  ✦ ClassName.method() ya object.method() — dono se call    │
   └─────────────────────────────────────────────────────────────┘
'''

class Calculator:
    # static methods — utility kaam ke liye
    @staticmethod
    def add(x, y):
        print(f"{x} + {y} = {x + y}")

    @staticmethod
    def multiply(x, y):
        print(f"{x} x {y} = {x * y}")

    @staticmethod
    def isEven(n):
        if n % 2 == 0:
            print(f"{n} is Even")
        else:
            print(f"{n} is Odd")


Calculator.add(10, 20)                        # class name se call
Calculator.multiply(5, 6)
Calculator.isEven(7)

c = Calculator()
c.add(3, 4)                                   # object se bhi call ho sakta


# ══════════════════════════════════════════════════════════════════
#  INSTANCE vs CLASS vs STATIC — EK SAATH DEKHO
# ══════════════════════════════════════════════════════════════════

class Student:
    school = "ABC School"                     # class variable

    def __init__(self, name, marks):
        self.name  = name                     # instance variable
        self.marks = marks                    # instance variable

    # instance method — self chahiye
    def display(self):
        print(f"Name  : {self.name}")
        print(f"Marks : {self.marks}")

    # class method — cls chahiye
    @classmethod
    def getSchool(cls):
        print(f"School : {cls.school}")

    # static method — kuch nahi chahiye
    @staticmethod
    def greet():
        print("Welcome to the school!")


s = Student("Ankit", 85)

s.display()                                   # instance method
Student.getSchool()                           # class method
Student.greet()                               # static method


# ══════════════════════════════════════════════════════════════════
#  SETTER & GETTER METHOD
# ══════════════════════════════════════════════════════════════════
'''
Setter & Getter Method
   - Getter method → instance variable ki value return karta hai.
   - Setter method → instance variable ki value set karta hai.
   - Encapsulation ke saath use hota hai — direct access ki
     jagah methods se data control karo.
   - Validation add kar sakte ho setter mein.

   Key Points:
   ┌─────────────────────────────────────────────────────────────┐
   │  ✦ setVariable() → value set karna                         │
   │  ✦ getVariable() → value return karna                      │
   │  ✦ Data validation setter mein ho sakti hai                │
   │  ✦ Direct access se better — encapsulation maintain hoti   │
   └─────────────────────────────────────────────────────────────┘
'''

class Student:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setMarks(self, marks):
        self.marks = marks

    def getMarks(self):
        return self.marks


n = int(input("Enter number of students: "))
for i in range(n):
    name  = input("Enter name  : ")
    marks = int(input("Enter marks : "))
    std   = Student()
    std.setName(name)
    std.setMarks(marks)
    print(f"Hi.. {std.getName()}")
    print(f"Your Marks is {std.getMarks()}")
    print()


# ── Setter with Validation ────────────────────────────────────────
'''
Setter mein Validation
   - Setter ke andar condition laga sakte hain.
   - Invalid data set hone se rok sakte hain.
   - Ye encapsulation ka real fayda hai.
'''

class BankAccount:
    def __init__(self, owner):
        self.owner   = owner
        self.__balance = 0                    # private variable

    def setBalance(self, amount):
        if amount < 0:
            print("❌ Invalid — Balance negative nahi ho sakta")
        else:
            self.__balance = amount
            print(f"✅ Balance set : {self.__balance}")

    def getBalance(self):
        return self.__balance

    def display(self):
        print(f"Owner   : {self.owner}")
        print(f"Balance : {self.getBalance()}")


acc = BankAccount("Ankit")
acc.setBalance(5000)                          # valid
acc.setBalance(-100)                          # invalid — error message
acc.display()


# ══════════════════════════════════════════════════════════════════
#  METHOD CHAINING
# ══════════════════════════════════════════════════════════════════
'''
Method Chaining
   - Ek method ke result pe seedha doosra method call karna.
   - Iske liye method ko self return karna hota hai.
   - Code concise aur readable banta hai.
'''

class Student:
    def __init__(self):
        self.name  = None
        self.marks = None

    def setName(self, name):
        self.name = name
        return self                           # self return karo

    def setMarks(self, marks):
        self.marks = marks
        return self                           # self return karo

    def display(self):
        print(f"Name  : {self.name}")
        print(f"Marks : {self.marks}")
        return self


# Method chaining — ek line mein sab
Student().setName("Ankit").setMarks(95).display()


# ══════════════════════════════════════════════════════════════════
#  FLOW
# ══════════════════════════════════════════════════════════════════
'''
Flow
   Class define karo
         ↓
   Instance Method  →  self se instance/class data access
   Class Method     →  cls se class data access
   Static Method    →  independent utility kaam
         ↓
   Object banao
         ↓
   Instance Method  →  object.method()     call karo
   Class Method     →  Class.method()      call karo
   Static Method    →  Class.method()      call karo
         ↓
   Getter  →  data return karta hai
   Setter  →  data set karta hai (validation bhi ho sakti)
         ↓
   Method Chaining  →  self return karo → ek line mein sab
'''


# ══════════════════════════════════════════════════════════════════
#  QUICK REVISION
# ══════════════════════════════════════════════════════════════════
'''
Quick Revision
   ┌─────────────────┬──────────────┬──────────────┬──────────────┐
   │                 │ Instance     │ Class        │ Static       │
   ├─────────────────┼──────────────┼──────────────┼──────────────┤
   │ Decorator       │ Koi nahi     │ @classmethod │ @staticmethod│
   │ First Argument  │ self         │ cls          │ Koi nahi     │
   │ Instance Var    │ Access ✅    │ Access ❌    │ Access ❌   │
   │ Class Var       │ Access ✅    │ Access ✅    │ Access ❌   │
   │ Call karo       │ object.m()   │ Class.m()    │ Class.m()    │
   │ Use             │ Object kaam  │ Class kaam   │ Utility kaam │
   ├─────────────────┼──────────────┼──────────────┼──────────────┤
   │ Getter          │ Variable ki value return karta hai         │
   │ Setter          │ Variable ki value set karta hai            │
   │ Validation      │ Setter mein condition laga sakte hain      │
   │ Method Chaining │ self return karo — ek line mein sab call   │
   └─────────────────┴────────────────────────────────────────────┘
'''