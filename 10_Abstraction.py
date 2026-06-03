'''
╔══════════════════════════════════════════════════════════════════╗
║                   Abstraction in Python                          ║
╚══════════════════════════════════════════════════════════════════╝

   Definition:
   Abstraction means hiding the internal implementation details
   and showing only the essential features to the user.

   "What it does" is visible — "How it does" is hidden.

   Real life examples:
   → Car     : You press the accelerator — engine ka kaam hidden
   → ATM     : You press buttons — andar ka circuit hidden
   → TV      : You press remote — andar ki wiring hidden
   → Mobile  : You tap icons — OS ka kaam hidden

   In Python:
   We define what methods a class MUST have — without writing
   the actual implementation. The child class is forced to
   provide the implementation.
   This is done using the ABC module — Abstract Base Class.

   Abstract Class:
   → A class that cannot be instantiated (object nahi ban sakta).
   → It contains at least one abstract method.
   → It acts as a blueprint / contract for child classes.

   Abstract Method:
   → A method declared in the abstract class — but has no body.
   → Every child class MUST override it — compulsory.
   → If not overridden → TypeError at runtime.

   ┌─────────────────────────────────────────────────────────────┐
   │  Abstraction  →  abc module use karo                        │
   │  ABC          →  Abstract Base Class — import karo          │
   │  @abstractmethod → method ko abstract banao                 │
   │  Child class  →  har abstract method override karna zaroori │
   └─────────────────────────────────────────────────────────────┘
'''


# ══════════════════════════════════════════════════════════════════
#  IMPORT — ABC MODULE
# ══════════════════════════════════════════════════════════════════
'''
ABC Module
   - Python mein abstraction ke liye abc module use hota hai.
   - ABC  →  Abstract Base Class
   - abstractmethod  →  method ko abstract banane ka decorator

   from abc import ABC, abstractmethod
'''

from abc import ABC, abstractmethod


# ══════════════════════════════════════════════════════════════════
#  BASIC SYNTAX
# ══════════════════════════════════════════════════════════════════
'''
Basic Syntax

   class MyAbstractClass(ABC):          ← ABC se inherit karo
       @abstractmethod
       def my_method(self):             ← abstract method — body nahi
           pass

   class ConcreteClass(MyAbstractClass):
       def my_method(self):             ← override karna COMPULSORY
           print("Implementation here")
'''

class Shape(ABC):                       # Abstract class
    @abstractmethod
    def area(self):                     # Abstract method — body nahi
        pass

    @abstractmethod
    def perimeter(self):                # Abstract method — body nahi
        pass

    def describe(self):                 # Normal method — body hai ✅
        print("Main ek Shape hoon.")
        print(f"Area      : {self.area()}")
        print(f"Perimeter : {self.perimeter()}")


# Abstract class ka object nahi ban sakta ❌
# s = Shape()    # TypeError: Can't instantiate abstract class


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):                     # Override — COMPULSORY ✅
        return round(3.14 * self.radius ** 2, 2)

    def perimeter(self):                # Override — COMPULSORY ✅
        return round(2 * 3.14 * self.radius, 2)


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length  = length
        self.breadth = breadth

    def area(self):                     # Override — COMPULSORY ✅
        return self.length * self.breadth

    def perimeter(self):                # Override — COMPULSORY ✅
        return 2 * (self.length + self.breadth)


c = Circle(7)
r = Rectangle(5, 10)

c.describe()
print()
r.describe()


# ══════════════════════════════════════════════════════════════════
#  WHAT HAPPENS IF ABSTRACT METHOD NOT OVERRIDDEN
# ══════════════════════════════════════════════════════════════════
'''
Abstract Method Override Nahi Kiya Toh?
   - TypeError aata hai — class ka object nahi banega.
   - Yahi Abstraction ka fayda hai — implementation force hoti hai.
   - Child class ko poori responsibility leni padti hai.
'''

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Dog(Animal):
    def sound(self):                    # Override ✅
        print("Woof Woof!")

    # move() override nahi kiya ❌
    # Dog() banane pe TypeError aayega:
    # TypeError: Can't instantiate abstract class Dog
    # with abstract method move


class Cat(Animal):
    def sound(self):                    # Override ✅
        print("Meow Meow!")

    def move(self):                     # Override ✅
        print("Cat quietly walks...")


# d = Dog()     # ❌ TypeError — move() override nahi kiya
c = Cat()       # ✅ Dono override kiye — object ban gaya
c.sound()
c.move()


# ══════════════════════════════════════════════════════════════════
#  ABSTRACT CLASS WITH __init__
# ══════════════════════════════════════════════════════════════════
'''
Abstract Class mein __init__
   - Abstract class ka apna __init__ ho sakta hai.
   - Child class super().__init__() se use kar sakti hai.
   - Common data jo sab children share karein — abstract mein
     rakhte hain.
'''

class Employee(ABC):
    def __init__(self, name, emp_id):
        self.name   = name
        self.emp_id = emp_id

    @abstractmethod
    def calculate_salary(self):         # Har employee ka alag formula
        pass

    @abstractmethod
    def role(self):                     # Har employee ka alag role
        pass

    def display(self):                  # Common method — sab ke liye same
        print(f"Name   : {self.name}")
        print(f"Emp ID : {self.emp_id}")
        print(f"Role   : {self.role()}")
        print(f"Salary : ₹{self.calculate_salary()}")


class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, monthly_salary):
        super().__init__(name, emp_id)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):         # Override ✅
        return self.monthly_salary

    def role(self):                     # Override ✅
        return "Full-Time Employee"


class PartTimeEmployee(Employee):
    def __init__(self, name, emp_id, hourly_rate, hours_worked):
        super().__init__(name, emp_id)
        self.hourly_rate  = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):         # Override ✅ — apna formula
        return self.hourly_rate * self.hours_worked

    def role(self):                     # Override ✅
        return "Part-Time Employee"


class FreelanceEmployee(Employee):
    def __init__(self, name, emp_id, project_fee, projects):
        super().__init__(name, emp_id)
        self.project_fee = project_fee
        self.projects    = projects

    def calculate_salary(self):         # Override ✅ — apna formula
        return self.project_fee * self.projects

    def role(self):                     # Override ✅
        return "Freelancer"


employees = [
    FullTimeEmployee("Ankit",  "E001", 75000),
    PartTimeEmployee("Sophia", "E002", 500, 80),
    FreelanceEmployee("Rahul", "E003", 15000, 3)
]

for emp in employees:
    emp.display()
    print()


# ══════════════════════════════════════════════════════════════════
#  ABSTRACT CLASS + ABSTRACT PROPERTY
# ══════════════════════════════════════════════════════════════════
'''
Abstract Property
   - Sirf methods nahi — properties bhi abstract ho sakti hain.
   - @property aur @abstractmethod dono decorators lagao.
   - Child class mein @property se implement karna hoga.
'''

class Vehicle(ABC):
    def __init__(self, brand):
        self.brand = brand

    @property
    @abstractmethod
    def fuel_type(self):                # Abstract property
        pass

    @property
    @abstractmethod
    def max_speed(self):                # Abstract property
        pass

    @abstractmethod
    def start(self):
        pass

    def info(self):
        print(f"Brand     : {self.brand}")
        print(f"Fuel      : {self.fuel_type}")
        print(f"Max Speed : {self.max_speed} km/h")
        self.start()


class PetrolCar(Vehicle):
    @property
    def fuel_type(self):                # Override property ✅
        return "Petrol"

    @property
    def max_speed(self):                # Override property ✅
        return 180

    def start(self):                    # Override method ✅
        print(f"{self.brand} petrol engine start — Vroom! 🚗")


class ElectricCar(Vehicle):
    @property
    def fuel_type(self):                # Override property ✅
        return "Electric"

    @property
    def max_speed(self):                # Override property ✅
        return 250

    def start(self):                    # Override method ✅
        print(f"{self.brand} electric motor start — Swoosh! ⚡")


p = PetrolCar("Toyota")
e = ElectricCar("Tesla")

p.info()
print()
e.info()


# ══════════════════════════════════════════════════════════════════
#  ABSTRACTION + ENCAPSULATION SAATH SAATH
# ══════════════════════════════════════════════════════════════════
'''
Abstraction + Encapsulation
   - Dono ka saath use karna real world pattern hai.
   - Abstraction  →  "kya karna hai" define karo (blueprint)
   - Encapsulation →  "data chupaao" + controlled access
   - Saath mein use karne se secure aur clean design milta hai.
'''

class BankAccount(ABC):
    def __init__(self, owner, balance):
        self.owner     = owner
        self.__balance = balance        # Encapsulation — private

    def getBalance(self):               # Getter — controlled access
        return self.__balance

    def _setBalance(self, amount):      # Protected setter — internal use
        self.__balance = amount

    @abstractmethod
    def deposit(self, amount):          # Abstraction — child implement kare
        pass

    @abstractmethod
    def withdraw(self, amount):         # Abstraction — child implement kare
        pass

    def display(self):
        print(f"Owner   : {self.owner}")
        print(f"Balance : ₹{self.getBalance()}")


class SavingsAccount(BankAccount):
    MIN_BALANCE = 1000                  # class variable

    def deposit(self, amount):          # Override ✅
        if amount <= 0:
            print("❌ Invalid deposit amount")
        else:
            self._setBalance(self.getBalance() + amount)
            print(f"✅ ₹{amount} jama — Balance: ₹{self.getBalance()}")

    def withdraw(self, amount):         # Override ✅
        if amount <= 0:
            print("❌ Invalid amount")
        elif self.getBalance() - amount < self.MIN_BALANCE:
            print(f"❌ Minimum balance ₹{self.MIN_BALANCE} maintain karna zaroori")
        else:
            self._setBalance(self.getBalance() - amount)
            print(f"✅ ₹{amount} nikale — Balance: ₹{self.getBalance()}")


class CurrentAccount(BankAccount):
    OVERDRAFT_LIMIT = 10000             # class variable

    def deposit(self, amount):          # Override ✅
        if amount <= 0:
            print("❌ Invalid deposit amount")
        else:
            self._setBalance(self.getBalance() + amount)
            print(f"✅ ₹{amount} jama — Balance: ₹{self.getBalance()}")

    def withdraw(self, amount):         # Override ✅ — overdraft allowed
        if self.getBalance() - amount < -self.OVERDRAFT_LIMIT:
            print(f"❌ Overdraft limit ₹{self.OVERDRAFT_LIMIT} exceed")
        else:
            self._setBalance(self.getBalance() - amount)
            print(f"✅ ₹{amount} nikale — Balance: ₹{self.getBalance()}")


print("═" * 40)
print("SAVINGS ACCOUNT")
print("═" * 40)
s = SavingsAccount("Ankit", 5000)
s.display()
s.deposit(3000)
s.withdraw(6000)        # min balance violation
s.withdraw(4000)        # valid ✅

print()
print("═" * 40)
print("CURRENT ACCOUNT")
print("═" * 40)
c = CurrentAccount("Sophia", 2000)
c.display()
c.withdraw(5000)        # overdraft — allowed ✅
c.withdraw(10000)       # overdraft limit cross ❌


# ══════════════════════════════════════════════════════════════════
#  COMPLETE REAL WORLD EXAMPLE — FOOD ORDERING SYSTEM
# ══════════════════════════════════════════════════════════════════

class FoodItem(ABC):
    def __init__(self, name, price):
        self.name  = name
        self.__price = price            # private — encapsulation

    def getPrice(self):
        return self.__price

    @abstractmethod
    def prepare(self):                  # Har food ka preparation alag
        pass

    @abstractmethod
    def category(self):                 # Har food ki category alag
        pass

    @abstractmethod
    def estimated_time(self):           # Har food ka time alag
        pass

    def order_summary(self):
        print(f"Item     : {self.name}")
        print(f"Category : {self.category()}")
        print(f"Price    : ₹{self.getPrice()}")
        print(f"Time     : {self.estimated_time()} mins")
        self.prepare()


class Pizza(FoodItem):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def prepare(self):                  # Override ✅
        print(f"🍕 {self.name} ({self.size}) ban rahi hai — dough stretch, sauce, cheese, oven!")

    def category(self):                 # Override ✅
        return "Italian"

    def estimated_time(self):           # Override ✅
        return 20


class Burger(FoodItem):
    def __init__(self, name, price, patty_type):
        super().__init__(name, price)
        self.patty_type = patty_type

    def prepare(self):                  # Override ✅
        print(f"🍔 {self.name} ({self.patty_type} patty) ban raha hai — grill, assemble, wrap!")

    def category(self):                 # Override ✅
        return "Fast Food"

    def estimated_time(self):           # Override ✅
        return 10


class Biryani(FoodItem):
    def __init__(self, name, price, spice_level):
        super().__init__(name, price)
        self.spice_level = spice_level

    def prepare(self):                  # Override ✅
        print(f"🍛 {self.name} (spice: {self.spice_level}) ban rahi hai — rice, masala, dum pe pakao!")

    def category(self):                 # Override ✅
        return "Indian"

    def estimated_time(self):           # Override ✅
        return 35


class Sushi(FoodItem):
    def __init__(self, name, price, roll_type):
        super().__init__(name, price)
        self.roll_type = roll_type

    def prepare(self):                  # Override ✅
        print(f"🍣 {self.name} ({self.roll_type}) ban raha hai — rice, fish, roll, slice!")

    def category(self):                 # Override ✅
        return "Japanese"

    def estimated_time(self):           # Override ✅
        return 15


# Order place karo
order = [
    Pizza("Margherita",    350, "Medium"),
    Burger("Aloo Tikki",   150, "Veg"),
    Biryani("Hyderabadi",  280, "Medium"),
    Sushi("California",    450, "Maki")
]

total = 0
print("╔══════════════════════════════════╗")
print("║         YOUR ORDER               ║")
print("╚══════════════════════════════════╝")
for item in order:
    item.order_summary()
    total += item.getPrice()
    print("─" * 36)

print(f"\nTotal Amount : ₹{total}")
print("Thank you for ordering! 🎉")


# ══════════════════════════════════════════════════════════════════
#  ABSTRACTION vs ENCAPSULATION — DIFFERENCE
# ══════════════════════════════════════════════════════════════════
'''
Abstraction vs Encapsulation
   ┌──────────────────┬──────────────────────────────────────────┐
   │                  │ Abstraction        │ Encapsulation        │
   ├──────────────────┼────────────────────┼──────────────────────┤
   │ Matlab           │ Hide complexity    │ Hide data            │
   │ "Kya chupaate"   │ Implementation     │ Variables            │
   │ Focus            │ Design / Blueprint │ Data Protection      │
   │ Kaise            │ Abstract class,    │ private, protected   │
   │                  │ abstract method    │ getter, setter       │
   │ Example          │ ATM ka button      │ ATM ka balance       │
   │                  │ (internal circuit  │ (seedha access nahi, │
   │                  │ hidden)            │ sirf method se)      │
   └──────────────────┴────────────────────┴──────────────────────┘

   Dono milke kaam karte hain — Real projects mein saath use hota.
'''


# ══════════════════════════════════════════════════════════════════
#  FLOW
# ══════════════════════════════════════════════════════════════════
'''
Flow
   from abc import ABC, abstractmethod
         ↓
   Abstract Class banao  →  class MyClass(ABC):
         ↓
   Abstract Method lagao →  @abstractmethod
                             def method(self): pass
         ↓
   Abstract class ka object nahi ban sakta → TypeError ❌
         ↓
   Child class banao → Abstract class se inherit karo
         ↓
   Har abstract method override karo → COMPULSORY
   Ek bhi miss kiya → TypeError ❌
         ↓
   Normal methods bhi ho sakte hain abstract class mein → ✅
   __init__ bhi ho sakta hai → super().__init__() se use karo
         ↓
   Abstract Property bhi ho sakti hai →
   @property + @abstractmethod dono lagao
         ↓
   Abstraction + Encapsulation saath use karo →
   Secure + Clean design milta hai
'''


# ══════════════════════════════════════════════════════════════════
#  QUICK REVISION
# ══════════════════════════════════════════════════════════════════
'''
Quick Revision
   ┌──────────────────────┬────────────────────────────────────────┐
   │ Concept              │ Key Point                              │
   ├──────────────────────┼────────────────────────────────────────┤
   │ Abstraction          │ Implementation hide karo — sirf        │
   │                      │ "kya karna hai" dikhao                 │
   ├──────────────────────┼────────────────────────────────────────┤
   │ ABC                  │ Abstract Base Class — abc module se    │
   │ Import               │ from abc import ABC, abstractmethod    │
   ├──────────────────────┼────────────────────────────────────────┤
   │ Abstract Class       │ class MyClass(ABC): — object nahi banta│
   │ Abstract Method      │ @abstractmethod — body nahi, pass only │
   ├──────────────────────┼────────────────────────────────────────┤
   │ Child Class          │ Har abstract method override karna     │
   │                      │ COMPULSORY — varna TypeError ❌        │
   ├──────────────────────┼────────────────────────────────────────┤
   │ Normal Method        │ Abstract class mein bhi ho sakta ✅    │
   │ __init__             │ Abstract class mein bhi ho sakta ✅    │
   │ Abstract Property    │ @property + @abstractmethod dono       │
   ├──────────────────────┼────────────────────────────────────────┤
   │ Abstraction          │ Blueprint / contract deta hai          │
   │ Encapsulation        │ Data chupaata hai — private/protected  │
   │ Dono saath           │ Real projects ka standard pattern      │
   └──────────────────────┴────────────────────────────────────────┘
'''