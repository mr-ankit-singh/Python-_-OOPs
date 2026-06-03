'''
╔══════════════════════════════════════════════════════════════════╗
║               Properties — @property in Python                   ║
╚══════════════════════════════════════════════════════════════════╝

   Definition:
   @property is a built-in decorator in Python that allows you
   to define a method that can be accessed like an attribute
   (variable) — not like a method call.

   Simple words mein:
   → Normally getter likhte hain: obj.getName()  ← brackets lagte
   → @property se:                obj.name        ← attribute jaisa

   Why use @property?
   → Direct variable access dena — but control apne haath mein
   → Getter/Setter ka professional aur Pythonic tarika
   → Validation add kar sakte hain — bina interface change kiye
   → Private variable ko safely expose kar sakte hain
   → Read-only attributes bana sakte hain

   3 Parts of @property:
   ┌─────────────────────────────────────────────────────────────┐
   │  @property          →  Getter  — value padhna               │
   │  @name.setter       →  Setter  — value set karna            │
   │  @name.deleter      →  Deleter — value delete karna         │
   └─────────────────────────────────────────────────────────────┘
'''


# ══════════════════════════════════════════════════════════════════
#  PROBLEM — BINA @property KE
# ══════════════════════════════════════════════════════════════════
'''
Pehle samjho — problem kya hai bina @property ke

   Case 1: Direct variable access — No control
   Case 2: Getter/Setter — control hai, but ugly syntax

   Yeh dono problems @property solve karta hai.
'''

# ── Case 1: Direct Variable — Koi Control Nahi ───────────────────

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age  = age


s = Student("Ankit", 20)
print(s.age)            # 20 — theek hai

s.age = -5              # ❌ Invalid age — but Python rok nahi saka
print(s.age)            # -5 — galat value set ho gayi


# ── Case 2: Getter Setter — Control Hai, But Ugly ────────────────

class Student:
    def __init__(self, name, age):
        self.name  = name
        self.__age = age

    def getAge(self):
        return self.__age

    def setAge(self, age):
        if age < 0 or age > 120:
            print("❌ Invalid age")
        else:
            self.__age = age


s = Student("Ankit", 20)
print(s.getAge())       # getAge() — brackets lagte hain, ugly
s.setAge(25)            # setAge() — alag method, alag syntax
s.setAge(-5)            # blocked ✅ — but syntax acha nahi


# ── @property Solution — Best of Both Worlds ─────────────────────
# Variable jaisa simple syntax + Getter/Setter jaisa full control


# ══════════════════════════════════════════════════════════════════
#  @property — GETTER ONLY (READ-ONLY)
# ══════════════════════════════════════════════════════════════════
'''
@property — Getter
   - @property decorator method pe lagao.
   - Method ka naam hi property ka naam banega.
   - obj.method_naam se access hoga — brackets nahi lagte.
   - Sirf @property se — read-only property banti hai.
   - Write karne ki koshish → AttributeError

   Key Points:
   ┌─────────────────────────────────────────────────────────────┐
   │  ✦ @property decorator lagao method pe                      │
   │  ✦ obj.naam se access — obj.naam() nahi                     │
   │  ✦ Sirf getter — write karo toh AttributeError             │
   │  ✦ Private variable safely expose hoti hai                  │
   └─────────────────────────────────────────────────────────────┘
'''

class Circle:
    def __init__(self, radius):
        self.__radius = radius          # private variable

    @property
    def radius(self):                   # Getter — @property
        print("  [getter called]")
        return self.__radius

    @property
    def area(self):                     # Computed property — calculate karke deta hai
        return round(3.14 * self.__radius ** 2, 2)

    @property
    def perimeter(self):                # Computed property
        return round(2 * 3.14 * self.__radius, 2)


c = Circle(7)

# Variable ki tarah access karo — brackets nahi!
print(c.radius)         # getter call hoga   → 7
print(c.area)           # computed property  → 153.86
print(c.perimeter)      # computed property  → 43.96

# Write karne ki koshish — Read-only hai ❌
# c.radius = 10         # AttributeError: can't set attribute


# ══════════════════════════════════════════════════════════════════
#  @property + @name.setter — GETTER + SETTER
# ══════════════════════════════════════════════════════════════════
'''
@property + @name.setter
   - @property  →  getter define karo
   - @naam.setter  →  setter define karo — naam same rakhna zaroori
   - Setter mein validation add kar sakte hain
   - Bahar se variable ki tarah set bhi kar sakte hain

   IMPORTANT RULE:
   ┌─────────────────────────────────────────────────────────────┐
   │  ✦ Pehle @property (getter) define karo — HAMESHA          │
   │  ✦ Phir @naam.setter define karo                            │
   │  ✦ Dono ka method naam SAME hona chahiye                    │
   │  ✦ Private variable ka naam alag rakho — confusion na ho    │
   │     @property  def age → self.__age  (double underscore)    │
   └─────────────────────────────────────────────────────────────┘
'''

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age  = age                 # yahan setter call hoga — magic!

    @property
    def age(self):                      # Getter
        return self.__age               # private se deta hai

    @age.setter
    def age(self, value):               # Setter — validation ke saath
        if value < 0 or value > 120:
            print(f"❌ Invalid age: {value}")
        else:
            self.__age = value          # private mein store karta hai


s = Student("Ankit", 20)       # __init__ mein self.age = 20 → setter chalega
print(s.age)                    # getter chalega → 20

s.age = 25                      # setter chalega → valid ✅
print(s.age)                    # getter → 25

s.age = -5                      # setter chalega → blocked ❌
print(s.age)                    # 25 — purani value safe


# ══════════════════════════════════════════════════════════════════
#  __init__ MEIN SETTER AUTOMATICALLY CALL HOTA HAI — IMPORTANT!
# ══════════════════════════════════════════════════════════════════
'''
IMPORTANT — Confusion Door Karo:

   Jab hum __init__ mein likhte hain:
       self.age = age

   Agar @age.setter define kiya hai toh —
   Python automatically setter call karta hai!

   Matlab validation __init__ pe bhi kaam karti hai.
   Direct self.__age = age likhna bypass kar deta hai setter ko.

   self.age  = age  →  setter call hoga  ✅ (recommended)
   self.__age = age →  setter bypass     ⚠️ (avoid karo)
'''

class Product:
    def __init__(self, name, price, quantity):
        self.name     = name
        self.price    = price           # setter call hoga
        self.quantity = quantity        # setter call hoga

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            print(f"❌ Price negative nahi ho sakti: {value}")
            self.__price = 0            # default value
        else:
            self.__price = value

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        if value < 0:
            print(f"❌ Quantity negative nahi ho sakti: {value}")
            self.__quantity = 0
        else:
            self.__quantity = value

    @property
    def total_value(self):              # Computed — read only
        return self.__price * self.__quantity

    def display(self):
        print(f"Product  : {self.name}")
        print(f"Price    : ₹{self.price}")
        print(f"Quantity : {self.quantity}")
        print(f"Total    : ₹{self.total_value}")


p = Product("Laptop", 55000, 3)
p.display()

print()
p.price    = -100       # ❌ blocked — setter validation
p.quantity = -2         # ❌ blocked — setter validation
p.price    = 60000      # ✅ valid
p.display()


# ══════════════════════════════════════════════════════════════════
#  @name.deleter — DELETE KARNA
# ══════════════════════════════════════════════════════════════════
'''
@name.deleter
   - del obj.naam  →  deleter call hota hai
   - Cleanup logic likhne ke liye use hota hai
   - Rare case hai — par important hai jaanna

   Key Points:
   ┌─────────────────────────────────────────────────────────────┐
   │  ✦ @naam.deleter decorator lagao                            │
   │  ✦ del obj.naam  se call hota hai                           │
   │  ✦ Cleanup / resource release ke liye use hota hai         │
   └─────────────────────────────────────────────────────────────┘
'''

class Employee:
    def __init__(self, name, salary):
        self.name   = name
        self.salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            print("❌ Salary negative nahi ho sakti")
            self.__salary = 0
        else:
            self.__salary = value

    @salary.deleter
    def salary(self):                   # Deleter
        print(f"⚠️  {self.name} ki salary information delete ho rahi hai!")
        del self.__salary


e = Employee("Ankit", 75000)
print(e.salary)         # getter → 75000

e.salary = 80000        # setter → valid ✅
print(e.salary)         # 80000

del e.salary            # deleter → call hoga

# print(e.salary)       # ❌ AttributeError — delete ho gaya


# ══════════════════════════════════════════════════════════════════
#  TEENO SAATH — @property + @setter + @deleter
# ══════════════════════════════════════════════════════════════════

class BankAccount:
    def __init__(self, owner, balance):
        self.owner   = owner
        self.balance = balance          # setter call hoga

    @property
    def balance(self):                  # Getter
        return self.__balance

    @balance.setter
    def balance(self, amount):          # Setter
        if amount < 0:
            print("❌ Balance negative nahi ho sakta — 0 set kiya")
            self.__balance = 0
        else:
            self.__balance = amount

    @balance.deleter
    def balance(self):                  # Deleter
        print(f"🗑️  {self.owner} ka account close ho raha hai!")
        del self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount      # setter call hoga
            print(f"✅ ₹{amount} jama — Balance: ₹{self.balance}")
        else:
            print("❌ Invalid deposit")

    def withdraw(self, amount):
        if amount > self.balance:
            print("❌ Insufficient balance")
        elif amount <= 0:
            print("❌ Invalid amount")
        else:
            self.balance -= amount      # setter call hoga
            print(f"✅ ₹{amount} nikale — Balance: ₹{self.balance}")

    def display(self):
        print(f"Owner   : {self.owner}")
        print(f"Balance : ₹{self.balance}")


acc = BankAccount("Ankit", 10000)
acc.display()
acc.deposit(5000)
acc.withdraw(3000)
acc.balance = -500      # ❌ blocked
acc.display()
del acc.balance         # deleter — account close


# ══════════════════════════════════════════════════════════════════
#  READ-ONLY PROPERTY — COMPUTED VALUES
# ══════════════════════════════════════════════════════════════════
'''
Read-Only Property — Computed Values
   - Kuch properties calculate hoti hain — set nahi ki jaatein.
   - Sirf @property lagao — @setter mat lagao.
   - Write karne ki koshish → AttributeError automatically.
   - Real world use: age from birthdate, total from items, etc.
'''

class Rectangle:
    def __init__(self, length, breadth):
        self.length  = length
        self.breadth = breadth

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        if value <= 0:
            print("❌ Length 0 se zyada honi chahiye")
            self.__length = 1
        else:
            self.__length = value

    @property
    def breadth(self):
        return self.__breadth

    @breadth.setter
    def breadth(self, value):
        if value <= 0:
            print("❌ Breadth 0 se zyada honi chahiye")
            self.__breadth = 1
        else:
            self.__breadth = value

    @property
    def area(self):                     # Read-only computed property
        return self.__length * self.__breadth

    @property
    def perimeter(self):                # Read-only computed property
        return 2 * (self.__length + self.__breadth)

    @property
    def is_square(self):                # Read-only boolean property
        return self.__length == self.__breadth


r = Rectangle(5, 10)
print(f"Length    : {r.length}")
print(f"Breadth   : {r.breadth}")
print(f"Area      : {r.area}")
print(f"Perimeter : {r.perimeter}")
print(f"Is Square : {r.is_square}")

# Write karne ki koshish ❌
# r.area = 100          # AttributeError: can't set attribute

r.length = 10           # setter — valid ✅
print(f"Is Square : {r.is_square}")     # True — ab square ban gaya


# ══════════════════════════════════════════════════════════════════
#  CONFUSION CLEAR KARO — NAAM SAME RAKHNA KYUN ZAROORI
# ══════════════════════════════════════════════════════════════════
'''
Confusion — Naam Same Kyun?

   Private variable ka naam alag hona chahiye:
   ✅  @property  def age → self.__age    (double underscore)
   ✅  @age.setter        → self.__age    (same private var)

   Agar naam same rakha toh — infinite recursion hogi:
   ❌  @property  def age → self.age     (getter khud ko call karega)
   ❌  @age.setter        → self.age     (setter khud ko call karega)
   ❌  → RecursionError: maximum recursion depth exceeded

   Convention:
   Property naam  →  age
   Private var    →  __age     (same naam, double underscore)
'''

# ❌ GALAT — RecursionError
# class Student:
#     @property
#     def age(self):
#         return self.age      # ← khud ko call karega — infinite loop!
#
#     @age.setter
#     def age(self, value):
#         self.age = value     # ← khud ko call karega — infinite loop!


# ✅ SAHI — Private variable alag naam se
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age  = age             # setter call — bilkul sahi

    @property
    def age(self):
        return self.__age           # ✅ __age — alag naam

    @age.setter
    def age(self, value):
        if value < 0:
            print("❌ Invalid age")
        else:
            self.__age = value      # ✅ __age mein store


s = Student("Ankit", 20)
print(s.age)        # 20 — getter ✅
s.age = 25          # setter ✅
print(s.age)        # 25


# ══════════════════════════════════════════════════════════════════
#  @property + INHERITANCE
# ══════════════════════════════════════════════════════════════════
'''
@property aur Inheritance
   - Child class Parent ki property inherit karti hai.
   - Child apna setter override kar sakti hai — parent ka getter
     inherit karte hue.
   - Abstract class mein @property + @abstractmethod dono lagao.
'''

class Shape:
    @property
    def area(self):                     # Base property
        return 0

    def describe(self):
        print(f"Area : {self.area}")    # runtime pe sahi area chalega


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    @property
    def area(self):                     # Override ✅
        return round(3.14 * self.__radius ** 2, 2)


class Square(Shape):
    def __init__(self, side):
        self.__side = side

    @property
    def area(self):                     # Override ✅
        return self.__side ** 2


shapes = [Circle(7), Square(5), Circle(3)]
for s in shapes:
    s.describe()                        # har baar sahi area chalega


# ══════════════════════════════════════════════════════════════════
#  COMPLETE REAL WORLD EXAMPLE — EMPLOYEE SALARY SYSTEM
# ══════════════════════════════════════════════════════════════════

class Employee:
    def __init__(self, name, emp_id, basic_salary, experience_years):
        self.name             = name
        self.emp_id           = emp_id
        self.basic_salary     = basic_salary        # setter chalega
        self.experience_years = experience_years    # setter chalega

    @property
    def basic_salary(self):
        return self.__basic_salary

    @basic_salary.setter
    def basic_salary(self, value):
        if value < 10000:
            print(f"❌ Minimum salary ₹10,000 honi chahiye — ₹10,000 set kiya")
            self.__basic_salary = 10000
        else:
            self.__basic_salary = value

    @property
    def experience_years(self):
        return self.__experience_years

    @experience_years.setter
    def experience_years(self, value):
        if value < 0:
            print("❌ Experience negative nahi ho sakta")
            self.__experience_years = 0
        else:
            self.__experience_years = value

    @property
    def hra(self):                      # Read-only computed
        return self.__basic_salary * 0.4

    @property
    def da(self):                       # Read-only computed
        return self.__basic_salary * 0.2

    @property
    def experience_bonus(self):         # Read-only computed
        if self.__experience_years >= 10:
            return self.__basic_salary * 0.3
        elif self.__experience_years >= 5:
            return self.__basic_salary * 0.15
        else:
            return self.__basic_salary * 0.05

    @property
    def gross_salary(self):             # Read-only computed
        return (self.__basic_salary
                + self.hra
                + self.da
                + self.experience_bonus)

    @property
    def tax(self):                      # Read-only computed
        if self.gross_salary > 100000:
            return self.gross_salary * 0.3
        elif self.gross_salary > 50000:
            return self.gross_salary * 0.2
        else:
            return self.gross_salary * 0.1

    @property
    def net_salary(self):               # Read-only computed
        return self.gross_salary - self.tax

    def display(self):
        print(f"{'─'*38}")
        print(f"  Name          : {self.name}")
        print(f"  Emp ID        : {self.emp_id}")
        print(f"  Experience    : {self.experience_years} years")
        print(f"{'─'*38}")
        print(f"  Basic Salary  : ₹{self.basic_salary:,.0f}")
        print(f"  HRA (40%)     : ₹{self.hra:,.0f}")
        print(f"  DA  (20%)     : ₹{self.da:,.0f}")
        print(f"  Exp Bonus     : ₹{self.experience_bonus:,.0f}")
        print(f"  Gross Salary  : ₹{self.gross_salary:,.0f}")
        print(f"  Tax           : ₹{self.tax:,.0f}")
        print(f"  Net Salary    : ₹{self.net_salary:,.0f}")
        print(f"{'─'*38}")


e1 = Employee("Ankit",  "E001", 50000,  3)
e2 = Employee("Sophia", "E002", 80000,  7)
e3 = Employee("Rahul",  "E003", 120000, 12)
e4 = Employee("Priya",  "E004", 5000,   1)  # ❌ too low — 10000 set

print()
e1.display()
print()
e2.display()
print()
e3.display()
print()
e4.display()

# Salary update — setter se validation hogi
print()
e1.basic_salary = 60000         # ✅ valid
e1.basic_salary = -1000         # ❌ blocked
e1.display()


# ══════════════════════════════════════════════════════════════════
#  FLOW
# ══════════════════════════════════════════════════════════════════
'''
Flow
   Private variable banao  →  self.__naam
         ↓
   @property lagao (Getter)
   def naam(self):
       return self.__naam      ← private variable return karo
         ↓
   @naam.setter lagao (Setter)
   def naam(self, value):
       validation check karo
       self.__naam = value     ← private variable mein store karo
         ↓
   @naam.deleter lagao (optional)
   def naam(self):
       del self.__naam
         ↓
   __init__ mein self.naam = value likhne pe → setter automatically call
         ↓
   Bahar se:
   obj.naam          →  getter call
   obj.naam = value  →  setter call
   del obj.naam      →  deleter call
         ↓
   Computed / Read-only property:
   Sirf @property lagao — @setter mat lagao
   obj.naam = value karne pe → AttributeError automatically
         ↓
   NAAM SAME RAKHNA ZAROORI:
   Property naam  →  age
   Private var    →  __age
   Agar self.age = value likhoge setter mein → RecursionError ❌
'''


# ══════════════════════════════════════════════════════════════════
#  QUICK REVISION
# ══════════════════════════════════════════════════════════════════
'''
Quick Revision
   ┌──────────────────────┬────────────────────────────────────────┐
   │ Concept              │ Key Point                              │
   ├──────────────────────┼────────────────────────────────────────┤
   │ @property            │ Getter — obj.naam se access (no ())    │
   │ @naam.setter         │ Setter — obj.naam = value              │
   │ @naam.deleter        │ Deleter — del obj.naam                 │
   ├──────────────────────┼────────────────────────────────────────┤
   │ Pehle @property      │ HAMESHA getter pehle define karo       │
   │ Phir @setter         │ Setter baad mein — naam same rakhna    │
   ├──────────────────────┼────────────────────────────────────────┤
   │ Private var          │ self.__naam — property naam se alag    │
   │ RecursionError       │ self.naam = val setter mein → loop ❌  │
   │ Fix                  │ self.__naam = val → sahi ✅            │
   ├──────────────────────┼────────────────────────────────────────┤
   │ Read-only property   │ Sirf @property — no setter             │
   │                      │ Write karo → AttributeError ❌         │
   │ Computed property    │ Calculate karke return karo — no store │
   ├──────────────────────┼────────────────────────────────────────┤
   │ __init__ magic       │ self.naam = val → setter call hota hai │
   │ Bypass mat karo      │ self.__naam = val → setter skip hota   │
   ├──────────────────────┼────────────────────────────────────────┤
   │ vs Getter/Setter     │ getAge() → s.age  (clean syntax)       │
   │ Pythonic way         │ @property use karna standard practice  │
   └──────────────────────┴────────────────────────────────────────┘
'''