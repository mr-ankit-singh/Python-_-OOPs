'''
╔══════════════════════════════════════════════════════════════════╗
║                   Types of Variables in Python                   ║
╚══════════════════════════════════════════════════════════════════╝

   Types of Variables:
   ┌─────────────────────────────────────────────────────────────┐
   │  a) Instance Variable  ( Object level variable )            │
   │  b) Static Variable    ( Class level variable  )            │
   │  c) Local Variable     ( Method level variable )            │
   └─────────────────────────────────────────────────────────────┘
'''


# ══════════════════════════════════════════════════════════════════
#  a) INSTANCE VARIABLE — Object Level Variable
# ══════════════════════════════════════════════════════════════════
'''
Instance Variable
   - Python instance variables are owned by an instance of a class.
   - The value of an instance variable can be different depending
     on the instance with which the variable is associated.
   - This means that the value of each instance variable can vary.
   - This is unlike a class variable where the variable can only
     have one value that you assign.
   - Instance variables are declared inside a class method.

   Key Points:
   ┌─────────────────────────────────────────────────────────────┐
   │  ✦ self.variable_name se declare hoti hai                   │
   │  ✦ Har object ka apna alag data hota hai                    │
   │  ✦ __init__ ke andar declare hoti hai mostly                │
   │  ✦ Ek object ki value change karne se doosre pe             │ 
   │    koi fark nahi padta                                      │
   └─────────────────────────────────────────────────────────────┘
'''

# coffee_name and price are instance variables
class CoffeeOrder:
    def __init__(self, coffee_name, price):
        self.coffee_name = coffee_name        # instance variable
        self.price       = price              # instance variable


c1 = CoffeeOrder("Latte",    150)
c2 = CoffeeOrder("Espresso", 100)

# Har object ka apna alag data hai
print(c1.coffee_name)                         # Latte
print(c2.coffee_name)                         # Espresso


# ── Instance Variable — Baad Mein Bhi Add Kar Sakte Hain ─────────

class Student:
    def __init__(self, name):
        self.name = name


s = Student("Ankit")
s.age = 20                                    # baad mein add kiya
print(s.__dict__)                             # {'name': 'Ankit', 'age': 20}


# ══════════════════════════════════════════════════════════════════
#  b) STATIC VARIABLE — Class Level Variable
# ══════════════════════════════════════════════════════════════════
'''
Class | Static Variable
   - A Python class variable is shared by all object instances of a class.
   - Class variables are declared when a class is being constructed.
   - They are not defined inside any methods of a class.
   - Because a class variable is shared by instances of a class,
     the Python class owns the variable.
   - As a result, all instances of the class will be able to access that variable.
   - Class variables are shared by all instances that access the class.
   - Class variables are useful because they allow you to declare a variable when 
     a class has been built, which can then be used later in your class.

   Key Points:
   ┌─────────────────────────────────────────────────────────────┐
   │  ✦ Class ke andar, kisi bhi method ke bahar declare hoti   │
   │  ✦ Sab objects ek hi value share karte hain                │
   │  ✦ ClassName.variable se access karo                       │
   │  ✦ Ek jagah change karo — sab pe effect                    │
   └─────────────────────────────────────────────────────────────┘
'''

# menu_type is a class variable
class Espresso:
    menu_type = "Drink"                       # static / class variable


# ── Accessing a Class Variable ────────────────────────────────────

espresso_order = Espresso()
print(espresso_order.menu_type)               # Drink


# ── Changing a Class Variable ─────────────────────────────────────
'''
   Note: Object se change karne par sirf us object ki copy
         change hoti hai — class variable same rehta hai.
         Class variable change karne ke liye ClassName use karo.
'''

class Espresso:
    menu_type = "Drink"


espresso_order = Espresso()
espresso_order.menu_type = "Coffee"           # sirf is object ki copy change
print(espresso_order.menu_type)               # Coffee
print(Espresso.menu_type)                     # Drink — class variable same hai


# ── Class Variable — Sahi Tarika Change Karne Ka ─────────────────

class Espresso:
    menu_type = "Drink"


Espresso.menu_type = "Coffee"                 # class variable change kiya
e1 = Espresso()
e2 = Espresso()
print(e1.menu_type)                           # Coffee
print(e2.menu_type)                           # Coffee — dono pe effect


# ── Various Places — Static Variable Declare Karne Ki Jagah ──────
'''
Various Places we can declare Static Variable:
   ┌─────────────────────────────────────────────────────────────┐
   │  1. Within the class directly but outside of any method     │
   │  2. Inside constructor by using classname                   │
   │  3. Inside instance method by using classname               │
   │  4. Inside classmethod by using cls and classname           │
   │  5. Inside static method by using classname                 │
   │  6. From outside of class by using classname                │
   └─────────────────────────────────────────────────────────────┘
'''

class Test:
    a = 10                                    # 1. class ke andar directly

    def __init__(self):
        Test.b = 20                           # 2. constructor mein

    def m1(self):
        Test.c = 30                           # 3. instance method mein

    @classmethod
    def m2(cls):
        cls.d  = 40                           # 4. classmethod mein — cls se
        Test.e = 50                           # 4. classmethod mein — classname se

    @staticmethod
    def m3():
        Test.f = 60                           # 5. static method mein


Test.g = 70                                   # 6. class ke bahar se

print(Test.__dict__)                          # saare static variables dekho


# ══════════════════════════════════════════════════════════════════
#  c) LOCAL VARIABLE — Method Level Variable
# ══════════════════════════════════════════════════════════════════
'''
Local Variable
   - Local variables are confined to their method area where
     they have been declared.
   - Variables declared inside a method can be used in the
     same method only.
   - Method khatam hone ke baad local variable destroy ho jaata hai.

   Key Points:
   ┌─────────────────────────────────────────────────────────────┐
   │  ✦ Sirf us method ke andar accessible hai                   │
   │  ✦ Method khatam → variable destroy                         │
   │  ✦ self nahi lagta — seedha naam se access hota hai         │
   │  ✦ Bahar se access karne ki koshish → NameError             │
   └─────────────────────────────────────────────────────────────┘
'''

# Id, Name, Age, Gender are local variables (parameters)
class Employee:
    def __init__(self, Id, Name, Age, Gender):
        self.Id     = Id                      # local → instance variable bana
        self.Name   = Name
        self.Age    = Age
        self.Gender = Gender


# ── Local Variable — Sirf Method Ke Andar ────────────────────────

class Calculator:
    def add(self, a, b):
        result = a + b                        # result local variable hai
        print("Sum:", result)
        return result


c = Calculator()
c.add(10, 20)
# print(result)                              # NameError — bahar accessible nahi


# ══════════════════════════════════════════════════════════════════
#  INSTANCE vs STATIC vs LOCAL — EK SAATH DEKHO
# ══════════════════════════════════════════════════════════════════

class Employee:
    company = "Google"                        # Static  — sab share karte hain

    def __init__(self, name, salary):
        self.name   = name                    # Instance — har object ka alag
        self.salary = salary                  # Instance — har object ka alag

    def display(self):
        bonus = self.salary * 0.10            # Local    — sirf yahan kaam karega
        print(f"Name    : {self.name}")
        print(f"Company : {Employee.company}")
        print(f"Salary  : {self.salary}")
        print(f"Bonus   : {bonus}")


e1 = Employee("Ankit",  100000)
e2 = Employee("Sophia",  80000)

e1.display()
print()
e2.display()


# ══════════════════════════════════════════════════════════════════
#  FLOW
# ══════════════════════════════════════════════════════════════════
'''
Flow
   Class define karo
         ↓
   Static Variable → class ke andar define karo (method ke bahar)
         ↓
   Object banao → __init__ call hota hai
         ↓
   Instance Variable → self.variable se set hota hai
         ↓
   Method call karo
         ↓
   Local Variable → method ke andar declare hota hai
         ↓
   Method khatam → Local variable destroy ho jaata hai
         ↓
   Object destroy → Instance variable destroy ho jaata hai
         ↓
   Class destroy → Static variable destroy ho jaata hai
'''


# ══════════════════════════════════════════════════════════════════
#  QUICK REVISION
# ══════════════════════════════════════════════════════════════════
'''
Quick Revision
   ┌──────────────────┬────────────────┬──────────────┬────────────┐
   │                  │ Instance Var   │ Static Var   │ Local Var  │
   ├──────────────────┼────────────────┼──────────────┼────────────┤
   │ Level            │ Object         │ Class        │ Method     │
   │ Declare          │ self.var       │ class andar  │ method     │
   │ Access           │ self.var       │ Class.var    │ var        │
   │ Shared?          │ Nahi           │ Haan         │ Nahi       │
   │ Lifetime         │ Object alive   │ Class alive  │ Method run │
   │ Har object alag? │ Haan ✅        │ Nahi ❌      │ Haan ✅    │
   └──────────────────┴────────────────┴──────────────┴────────────┘
'''