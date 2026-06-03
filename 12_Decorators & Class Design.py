'''
╔══════════════════════════════════════════════════════════════════╗
║           Decorators & Class Design in Python                    ║
╚══════════════════════════════════════════════════════════════════╝

   Definition:
   A decorator is a function that takes another function (or class)
   as input, adds some extra behavior to it, and returns it —
   without modifying the original function's code.

   Simple words mein:
   → Ek wrapper jo kisi function ke upar chadh jaata hai.
   → Function ka kaam wahi rehta hai — extra kaam badhta hai.
   → @ symbol se lagate hain.

   Real life example:
   → Pizza base hai ← original function
   → Cheese, toppings baad mein daalte hain ← decorator
   → Pizza wahi rehti hai — taste badh jaata hai

   Topics Covered:
   ┌─────────────────────────────────────────────────────────────┐
   │  a) Function Decorator — basics                             │
   │  b) Decorator with Arguments                                │
   │  c) Chaining Multiple Decorators                            │
   │  d) Class Decorator                                         │
   │  e) @staticmethod, @classmethod — revisit                   │
   │  f) @property — revisit with internals                      │
   │  g) @dataclass — Class Design                               │
   │  h) __slots__ — Memory Optimization                         │
   │  i) __repr__, __str__ — Class Design Best Practice          │
   │  j) MRO — Method Resolution Order Deep Dive                 │
   └─────────────────────────────────────────────────────────────┘
'''


# ══════════════════════════════════════════════════════════════════
#  a) FUNCTION DECORATOR — BASICS
# ══════════════════════════════════════════════════════════════════
'''
Function Decorator — Step by Step

   Step 1: Pehle samjho — function ek object hai Python mein.
           Dusre function ko argument mein de sakte hain.
           Function ke andar se function return kar sakte hain.

   Step 2: Decorator ek function hai jo:
           → Dusra function accept karta hai
           → Uske upar extra kaam karta hai
           → Wrapper function return karta hai

   Step 3: @ symbol shortcut hai manually call karne ka.
'''

# ── Step 1: Functions are Objects ────────────────────────────────

def greet():
    print("Hello!")

# Function ko variable mein store kar sakte hain
say_hello = greet
say_hello()                 # Hello! — same function call hua


def apply(func):            # Function ko argument mein le sakte hain
    func()                  # call karo

apply(greet)                # Hello!


# ── Step 2: Manually Decorator Banana ────────────────────────────

def my_decorator(func):             # Decorator function
    def wrapper():                  # Wrapper — extra kaam yahan
        print("=== START ===")      # Extra — before
        func()                      # Original function
        print("=== END ===")        # Extra — after
    return wrapper                  # Wrapper return karo


def greet():
    print("Hello, World!")


# Manual way — decorator apply karna
greet = my_decorator(greet)         # greet ab wrapper hai
greet()                             # START → Hello → END


# ── Step 3: @ Shortcut — Same Kaam, Short Syntax ─────────────────

def my_decorator(func):
    def wrapper():
        print("=== START ===")
        func()
        print("=== END ===")
    return wrapper


@my_decorator                       # ← yeh line = greet = my_decorator(greet)
def greet():
    print("Hello, World!")


greet()                             # START → Hello → END


# ── Real Example: Timer Decorator ────────────────────────────────

import time

def timer(func):
    def wrapper(*args, **kwargs):   # *args, **kwargs — koi bhi arguments
        start  = time.time()
        result = func(*args, **kwargs)
        end    = time.time()
        print(f"⏱️  '{func.__name__}' chalane mein laga: {end - start:.4f} seconds")
        return result
    return wrapper


@timer
def slow_task():
    time.sleep(0.5)
    print("Kaam ho gaya!")


@timer
def add(a, b):
    return a + b


slow_task()
result = add(10, 20)
print(f"Result: {result}")


# ── Real Example: Logger Decorator ───────────────────────────────

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"📋 [{func.__name__}] called with args={args} kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"📋 [{func.__name__}] returned: {result}")
        return result
    return wrapper


@logger
def multiply(x, y):
    return x * y


@logger
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"


multiply(5, 6)
greet("Ankit")
greet("Sophia", greeting="Namaste")


# ══════════════════════════════════════════════════════════════════
#  functools.wraps — IMPORTANT!
# ══════════════════════════════════════════════════════════════════
'''
functools.wraps — Kyun Zaroori Hai?

   Decorator lagate hi function ka naam aur docstring change
   ho jaata hai — wrapper ban jaata hai internally.

   Problem:
   @timer lagao greet pe → greet.__name__ → "wrapper" (wrong!)

   Fix:
   @functools.wraps(func) wrapper ke upar lagao →
   Original function ka naam aur docstring preserve hoga.

   Har decorator mein @functools.wraps lagana — best practice.
'''

import functools

# ❌ Bina wraps ke — naam change ho jaata
def bad_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@bad_decorator
def greet():
    """Greeting function"""
    print("Hello!")

print(greet.__name__)       # wrapper — galat ❌
print(greet.__doc__)        # None    — docstring gayi


# ✅ wraps ke saath — naam preserve hota
def good_decorator(func):
    @functools.wraps(func)          # ← yeh lagao
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@good_decorator
def greet():
    """Greeting function"""
    print("Hello!")

print(greet.__name__)       # greet  — sahi ✅
print(greet.__doc__)        # Greeting function ✅


# ══════════════════════════════════════════════════════════════════
#  b) DECORATOR WITH ARGUMENTS
# ══════════════════════════════════════════════════════════════════
'''
Decorator with Arguments
   - Kabhi kabhi decorator ko bhi arguments chahiye hote hain.
   - Jaise @repeat(3) — 3 baar chalao
   - Iske liye ek extra outer function banana padta hai.

   Structure:
   def decorator_with_args(arg1, arg2):     ← arguments receive karo
       def decorator(func):                 ← actual decorator
           @functools.wraps(func)
           def wrapper(*args, **kwargs):    ← wrapper
               ... use arg1, arg2 ...
               return func(*args, **kwargs)
           return wrapper
       return decorator                     ← decorator return karo

   3 levels ki nesting hoti hai!
'''

import functools

def repeat(times):                          # Outer — argument lega
    def decorator(func):                    # Middle — function lega
        @functools.wraps(func)
        def wrapper(*args, **kwargs):       # Inner — extra kaam karega
            for i in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@repeat(3)                                  # 3 baar chalao
def greet(name):
    print(f"Hello, {name}!")


@repeat(5)
def clap():
    print("👏", end=" ")


greet("Ankit")
print()
clap()
print()


# ── Real Example: Retry Decorator ────────────────────────────────

import functools
import random

def retry(max_attempts, delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"⚠️  Attempt {attempt} failed: {e}")
                    if attempt == max_attempts:
                        print(f"❌ Saare {max_attempts} attempts fail ho gaye!")
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator


@retry(max_attempts=3, delay=0.1)
def unstable_api_call():
    if random.random() < 0.7:              # 70% chance of failure
        raise ConnectionError("Server se connect nahi ho pa raha")
    return "✅ Data successfully fetch kiya!"


try:
    result = unstable_api_call()
    print(result)
except ConnectionError:
    print("API finally fail ho gayi.")


# ══════════════════════════════════════════════════════════════════
#  c) CHAINING MULTIPLE DECORATORS
# ══════════════════════════════════════════════════════════════════
'''
Chaining Multiple Decorators
   - Ek function pe kai decorators laga sakte hain.
   - NEECHE wala pehle apply hota hai — upar wala baad mein.
   - @d1 @d2 def f() → d1(d2(f)) — d2 pehle, d1 baad mein.

   Order yaad rakho:
   @decorator1    ← 2nd apply hoga (outer)
   @decorator2    ← 1st apply hoga (inner)
   def function(): ...
'''

import functools

def bold(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<b>{result}</b>"
    return wrapper


def italic(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<i>{result}</i>"
    return wrapper


def underline(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<u>{result}</u>"
    return wrapper


@bold                           # 3rd — sabse bahar
@italic                         # 2nd
@underline                      # 1st — sabse andar
def greet(name):
    return f"Hello, {name}!"


print(greet("Ankit"))           # <b><i><u>Hello, Ankit!</u></i></b>


# ── Real Chaining: Logger + Timer + Validator ─────────────────────

import functools, time

def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"📋 Calling: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"📋 Done: {func.__name__}")
        return result
    return wrapper


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start  = time.time()
        result = func(*args, **kwargs)
        print(f"⏱️  Time: {time.time() - start:.4f}s")
        return result
    return wrapper


def validate_positive(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError(f"❌ Negative value not allowed: {arg}")
        return func(*args, **kwargs)
    return wrapper


@logger
@timer
@validate_positive
def calculate_discount(price, discount_percent):
    discount = price * discount_percent / 100
    return price - discount


result = calculate_discount(1000, 20)
print(f"Final price: ₹{result}")

print()
try:
    calculate_discount(-500, 20)    # ❌ Validation fail
except ValueError as e:
    print(e)


# ══════════════════════════════════════════════════════════════════
#  d) CLASS DECORATOR
# ══════════════════════════════════════════════════════════════════
'''
Class Decorator
   - Function ki jagah Class bhi decorator ka kaam kar sakti hai.
   - __init__ mein function receive karo.
   - __call__ mein wrapper logic likho — object function ki tarah
     call hoga.
   - State maintain karna ho toh class decorator better hota hai.
'''

import functools

class CountCalls:
    """Kitni baar function call hua — track karta hai"""

    def __init__(self, func):
        functools.update_wrapper(self, func)    # wraps ka class version
        self.func       = func
        self.call_count = 0                     # state maintain hoti hai

    def __call__(self, *args, **kwargs):        # function call hone pe
        self.call_count += 1
        print(f"📊 '{self.func.__name__}' call #{self.call_count}")
        return self.func(*args, **kwargs)


@CountCalls
def greet(name):
    print(f"Hello, {name}!")


@CountCalls
def add(a, b):
    return a + b


greet("Ankit")
greet("Sophia")
greet("Rahul")
print(f"greet called {greet.call_count} times")

print()
add(5, 3)
add(10, 20)
print(f"add called {add.call_count} times")


# ── Class Decorator — Singleton Pattern ──────────────────────────
'''
Singleton Pattern:
   Ek class ka sirf EK object ban sake — kabhi bhi call karo,
   same object milega. Class decorator se easily ban sakta hai.
'''

def singleton(cls):
    instances = {}                              # sab classes ke instances store

    @functools.wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)   # pehli baar banana
        return instances[cls]                        # hamesha same return
    return get_instance


@singleton
class DatabaseConnection:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        print(f"🟢 DB Connection created: {host}:{port}")

    def query(self, sql):
        print(f"🔍 Running on {self.host}: {sql}")


db1 = DatabaseConnection("localhost", 5432)
db2 = DatabaseConnection("localhost", 5432)  # naya nahi banega!
db3 = DatabaseConnection("localhost", 5432)  # same object milega

print(db1 is db2)           # True — same object ✅
print(db2 is db3)           # True
db1.query("SELECT * FROM users")
db2.query("SELECT * FROM orders")    # same connection use hua


# ══════════════════════════════════════════════════════════════════
#  e) @staticmethod & @classmethod — INTERNALS
# ══════════════════════════════════════════════════════════════════
'''
@staticmethod aur @classmethod — Revisit
   - Ye dono bhi built-in decorators hain.
   - @staticmethod  →  self ya cls nahi chahiye
   - @classmethod   →  cls chahiye — class pe kaam
   - Pehle padhein hain — yahan internals samjho.

   When to use what:
   ┌────────────────┬────────────────────────────────────────────┐
   │ Instance method│ Object ka data chahiye — self              │
   │ @classmethod   │ Class ka data chahiye — cls                │
   │ @staticmethod  │ Koi class/object data nahi chahiye         │
   │                │ Utility kaam hai — class se related        │
   └────────────────┴────────────────────────────────────────────┘
'''

class Date:
    def __init__(self, day, month, year):
        self.day   = day
        self.month = month
        self.year  = year

    def __str__(self):
        return f"{self.day:02d}/{self.month:02d}/{self.year}"

    # @classmethod — Alternative constructor (factory method)
    @classmethod
    def from_string(cls, date_string):      # "25-12-2024" se object banana
        day, month, year = map(int, date_string.split("-"))
        return cls(day, month, year)        # cls se object banao

    @classmethod
    def today(cls):                         # Aaj ki date
        import datetime
        t = datetime.date.today()
        return cls(t.day, t.month, t.year)

    # @staticmethod — Utility
    @staticmethod
    def is_leap_year(year):                 # class/object data nahi chahiye
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    @staticmethod
    def days_in_month(month, year):         # Utility kaam
        import calendar
        return calendar.monthrange(year, month)[1]


d1 = Date(25, 12, 2024)
d2 = Date.from_string("01-01-2025")        # classmethod se object ✅
d3 = Date.today()                          # classmethod se aaj ✅

print(d1)
print(d2)
print(d3)
print(Date.is_leap_year(2024))             # True  — staticmethod ✅
print(Date.is_leap_year(2023))             # False
print(Date.days_in_month(2, 2024))         # 29    — leap year


# ══════════════════════════════════════════════════════════════════
#  f) @property — INTERNALS
# ══════════════════════════════════════════════════════════════════
'''
@property — Internally Kaise Kaam Karta Hai?
   - @property actually ek built-in class hai — function nahi.
   - property(fget, fset, fdel, doc) — char arguments.
   - @property syntax sirf sugar coat hai isi ka.

   Ye dono ek hi kaam karte hain:
   ┌─────────────────────────────────────────────────────────────┐
   │  @property + @setter  ←→  property(getter, setter)         │
   └─────────────────────────────────────────────────────────────┘
'''

# Long way — property() directly
class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius

    def get_celsius(self):
        return self.__celsius

    def set_celsius(self, value):
        if value < -273.15:
            raise ValueError("Absolute zero se neeche nahi ja sakte!")
        self.__celsius = value

    # Long way
    celsius = property(get_celsius, set_celsius)


t = Temperature(100)
print(t.celsius)        # get_celsius() call hoga
t.celsius = 25          # set_celsius() call hoga
print(t.celsius)


# Short way — @property (recommended)
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius          # setter call hoga

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Absolute zero se neeche nahi ja sakte!")
        self.__celsius = value

    @property
    def fahrenheit(self):               # Computed — read only
        return (self.__celsius * 9/5) + 32

    @property
    def kelvin(self):                   # Computed — read only
        return self.__celsius + 273.15


t = Temperature(100)
print(f"Celsius    : {t.celsius}")
print(f"Fahrenheit : {t.fahrenheit}")
print(f"Kelvin     : {t.kelvin}")

t.celsius = 0
print(f"Celsius    : {t.celsius}")
print(f"Fahrenheit : {t.fahrenheit}")


# ══════════════════════════════════════════════════════════════════
#  g) @dataclass — CLASS DESIGN
# ══════════════════════════════════════════════════════════════════
'''
@dataclass — Python 3.7+
   - Boilerplate code (repetitive code) bahut kam ho jaata hai.
   - Normally likhne par: __init__, __repr__, __eq__ — sab
     manually likhna padta hai.
   - @dataclass ye sab automatically generate karta hai!

   from dataclasses import dataclass, field

   What @dataclass auto-generates:
   ┌─────────────────────────────────────────────────────────────┐
   │  __init__   →  automatic — parameters se                    │
   │  __repr__   →  automatic — clean representation             │
   │  __eq__     →  automatic — fields compare karta hai         │
   └─────────────────────────────────────────────────────────────┘
'''

from dataclasses import dataclass, field

# ── Bina @dataclass — Boilerplate ─────────────────────────────────

class StudentManual:
    def __init__(self, name, age, marks):
        self.name  = name
        self.age   = age
        self.marks = marks

    def __repr__(self):
        return f"Student(name={self.name!r}, age={self.age!r}, marks={self.marks!r})"

    def __eq__(self, other):
        return (self.name, self.age, self.marks) == (other.name, other.age, other.marks)


# ── @dataclass ke saath — Clean ───────────────────────────────────

@dataclass
class Student:
    name  : str
    age   : int
    marks : float

    # Apne methods bhi add kar sakte hain
    def grade(self):
        if   self.marks >= 75: return "Distinction ⭐"
        elif self.marks >= 60: return "First Class ✅"
        elif self.marks >= 45: return "Second Class"
        else:                  return "Fail ❌"


s1 = Student("Ankit",  20, 85.5)
s2 = Student("Sophia", 22, 92.0)
s3 = Student("Ankit",  20, 85.5)

print(s1)               # __repr__ auto → Student(name='Ankit', age=20, marks=85.5)
print(s1 == s3)         # __eq__  auto  → True
print(s1 == s2)         # False

print(s1.grade())
print(s2.grade())


# ── @dataclass — Default Values ───────────────────────────────────

@dataclass
class Employee:
    name       : str
    emp_id     : str
    department : str  = "General"       # Default value
    salary     : float = 30000.0        # Default value
    is_active  : bool  = True

    def display(self):
        status = "Active" if self.is_active else "Inactive"
        print(f"{self.emp_id} | {self.name} | {self.department} | ₹{self.salary} | {status}")


e1 = Employee("Ankit",  "E001", "Engineering", 75000)
e2 = Employee("Sophia", "E002")                         # defaults use hoga
e3 = Employee("Rahul",  "E003", salary=50000, is_active=False)

e1.display()
e2.display()
e3.display()


# ── @dataclass — field() — Mutable Defaults ───────────────────────
'''
IMPORTANT:
   List ya dict ko default value mein seedha nahi de sakte —
   sab objects same list share kar lenge.
   field(default_factory=list) use karo.
'''

@dataclass
class Student:
    name   : str
    age    : int
    # subjects : list = []            # ❌ Wrong — sab share karenge
    subjects : list = field(default_factory=list)   # ✅ Har object ki apni list

    def add_subject(self, subject):
        self.subjects.append(subject)


s1 = Student("Ankit", 20)
s2 = Student("Sophia", 22)

s1.add_subject("Math")
s1.add_subject("Physics")
s2.add_subject("Chemistry")

print(s1.subjects)      # ['Math', 'Physics'] — sirf s1 ka ✅
print(s2.subjects)      # ['Chemistry']       — sirf s2 ka ✅


# ── @dataclass options ────────────────────────────────────────────
'''
@dataclass ke options:
   frozen=True   →  Immutable — set karne pe FrozenInstanceError
   order=True    →  <, >, <=, >= operators auto generate
   eq=False      →  __eq__ mat banao
'''

@dataclass(frozen=True)             # Immutable — tuple jaisa
class Point:
    x : float
    y : float


p1 = Point(3.0, 4.0)
p2 = Point(1.0, 2.0)

print(p1)
# p1.x = 10              # ❌ FrozenInstanceError — immutable hai

@dataclass(order=True)
class Product:
    price : float
    name  : str

p1 = Product(500,  "Phone")
p2 = Product(1200, "Laptop")
p3 = Product(300,  "Book")

products = [p1, p2, p3]
products.sort()             # price se sort hoga — order=True se auto ✅
for p in products:
    print(p)


# ══════════════════════════════════════════════════════════════════
#  h) __slots__ — MEMORY OPTIMIZATION
# ══════════════════════════════════════════════════════════════════
'''
__slots__
   - By default Python har object ke liye ek __dict__ (dictionary)
     banata hai — sab attributes store karne ke liye.
   - __dict__ bahut memory leta hai.
   - __slots__ se hum pehle hi bata dete hain kaun se attributes
     honge — Python dict nahi banata.
   - Memory bahut kam lagti hai — especially lakhon objects ho toh.

   Key Points:
   ┌─────────────────────────────────────────────────────────────┐
   │  ✦ __slots__ = ['attr1', 'attr2']                           │
   │  ✦ __dict__ nahi banta — memory save ✅                    │
   │  ✦ Sirf listed attributes allowed — baaki → AttributeError  │
   │  ✦ Lakhon objects ho tab use karo — micro-optimization      │
   └─────────────────────────────────────────────────────────────┘
'''

# Bina __slots__ — normal
class PointNormal:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = PointNormal(1, 2)
p.z = 10                    # naya attribute add kar sakte hain ✅
print(p.__dict__)           # {'x': 1, 'y': 2, 'z': 10}


# __slots__ ke saath
class PointSlots:
    __slots__ = ['x', 'y']  # Sirf yahi allowed

    def __init__(self, x, y):
        self.x = x
        self.y = y


ps = PointSlots(1, 2)
print(ps.x)                 # 1 ✅
print(ps.y)                 # 2 ✅
# ps.z = 10                 # ❌ AttributeError — z allowed nahi
# print(ps.__dict__)        # ❌ AttributeError — __dict__ nahi hai


# Memory Comparison
import sys

normal = [PointNormal(i, i) for i in range(1000)]
slotted = [PointSlots(i, i) for i in range(1000)]

print(f"Normal  object size: {sys.getsizeof(normal[0])} bytes")
print(f"Slotted object size: {sys.getsizeof(slotted[0])} bytes")


# __slots__ + @dataclass saath
from dataclasses import dataclass

@dataclass
class FastPoint:
    __slots__ = ['x', 'y']
    x : float
    y : float


fp = FastPoint(3.0, 4.0)
print(fp)


# ══════════════════════════════════════════════════════════════════
#  i) __repr__ & __str__ — CLASS DESIGN BEST PRACTICE
# ══════════════════════════════════════════════════════════════════
'''
__repr__ vs __str__ — Theek Se Samjho

   __str__   →  print(obj) → user ke liye — human readable
               str(obj) se bhi call hota hai

   __repr__  →  repr(obj) → developer ke liye — unambiguous
               Shell mein obj type karne pe bhi yahi dikhta
               Ideally → isko copy karke object recreate ho sake

   Rule:
   ┌─────────────────────────────────────────────────────────────┐
   │  __repr__ → HAMESHA likho — debugging ke liye zaroori      │
   │  __str__  → Optional — user-facing string chahiye toh likho │
   │  Agar sirf __repr__ likho → str() bhi wahi use karta hai   │
   └─────────────────────────────────────────────────────────────┘
'''

class Student:
    def __init__(self, name, age, marks):
        self.name  = name
        self.age   = age
        self.marks = marks

    def __repr__(self):
        # Developer ke liye — object recreate ho sake iska format
        return f"Student(name={self.name!r}, age={self.age!r}, marks={self.marks!r})"

    def __str__(self):
        # User ke liye — readable
        return f"{self.name} (Age: {self.age}, Marks: {self.marks})"


s = Student("Ankit", 20, 85)

print(s)                    # __str__  → Ankit (Age: 20, Marks: 85)
print(repr(s))              # __repr__ → Student(name='Ankit', age=20, marks=85)

students = [Student("Ankit", 20, 85), Student("Sophia", 22, 92)]
print(students)             # list mein __repr__ use hota hai


# ══════════════════════════════════════════════════════════════════
#  j) MRO — METHOD RESOLUTION ORDER DEEP DIVE
# ══════════════════════════════════════════════════════════════════
'''
MRO — Method Resolution Order
   - Multiple inheritance mein same method kai jagah ho toh
     Python C3 Linearization algorithm se order decide karta hai.
   - ClassName.__mro__ ya ClassName.mro() se dekh sakte hain.

   C3 Rule:
   → Child pehle — phir left parent — phir right parent
   → Koi class apne parent se pehle nahi aayegi
   → DRY — ek class sirf ek baar aayegi
'''

class A:
    def hello(self): print("A.hello")

class B(A):
    def hello(self): print("B.hello")

class C(A):
    def hello(self): print("C.hello")

class D(B, C):
    pass

class E(C, B):
    pass


d = D()
e = E()

d.hello()                       # B.hello — MRO: D→B→C→A
e.hello()                       # C.hello — MRO: E→C→B→A

print(D.__mro__)                # D, B, C, A, object
print(E.__mro__)                # E, C, B, A, object


# ── super() aur MRO saath ─────────────────────────────────────────
'''
super() MRO Follow Karta Hai
   - super() sirf "parent" nahi — MRO mein agle class ko call karta.
   - Isliye cooperative multiple inheritance possible hoti hai.
'''

class A:
    def greet(self):
        print("A greet")

class B(A):
    def greet(self):
        print("B greet")
        super().greet()         # MRO mein next → C

class C(A):
    def greet(self):
        print("C greet")
        super().greet()         # MRO mein next → A

class D(B, C):
    def greet(self):
        print("D greet")
        super().greet()         # MRO mein next → B


D().greet()
# D greet → B greet → C greet → A greet
# MRO: D → B → C → A — perfectly cooperative!
print(D.__mro__)


# ══════════════════════════════════════════════════════════════════
#  COMPLETE REAL WORLD EXAMPLE — ECOMMERCE PRODUCT SYSTEM
# ══════════════════════════════════════════════════════════════════

import functools
import time
from dataclasses import dataclass, field
from abc import ABC, abstractmethod

# Decorator — logging
def log_action(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"  📋 Action: {func.__name__}")
        result = func(*args, **kwargs)
        return result
    return wrapper

# Decorator — timing
def measure_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start  = time.time()
        result = func(*args, **kwargs)
        elapsed = (time.time() - start) * 1000
        print(f"  ⏱️  {func.__name__}: {elapsed:.2f}ms")
        return result
    return wrapper


# Abstract Base
class BaseProduct(ABC):
    __slots__ = ['name', 'price', 'stock']      # Memory optimization

    def __init__(self, name, price, stock):
        self.name  = name
        self.price = price
        self.stock = stock

    @abstractmethod
    def category(self): pass

    @abstractmethod
    def discount(self): pass

    @property
    def final_price(self):
        return round(self.price * (1 - self.discount() / 100), 2)

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, price={self.price})"

    def __str__(self):
        return f"{self.name} — ₹{self.final_price} ({self.discount()}% off)"

    @log_action
    @measure_time
    def purchase(self, qty):
        if qty > self.stock:
            print(f"  ❌ Insufficient stock. Available: {self.stock}")
            return False
        self.stock -= qty
        print(f"  ✅ {qty}x '{self.name}' purchased! Remaining: {self.stock}")
        return True


class ElectronicProduct(BaseProduct):
    __slots__ = ['name', 'price', 'stock', 'warranty_years']

    def __init__(self, name, price, stock, warranty_years):
        super().__init__(name, price, stock)
        self.warranty_years = warranty_years

    def category(self): return "Electronics"
    def discount(self): return 10                   # 10% off always


class FashionProduct(BaseProduct):
    __slots__ = ['name', 'price', 'stock', 'size']

    def __init__(self, name, price, stock, size):
        super().__init__(name, price, stock)
        self.size = size

    def category(self): return "Fashion"
    def discount(self): return 25                   # 25% off always


class GroceryProduct(BaseProduct):
    __slots__ = ['name', 'price', 'stock', 'expiry_days']

    def __init__(self, name, price, stock, expiry_days):
        super().__init__(name, price, stock)
        self.expiry_days = expiry_days

    def category(self): return "Grocery"
    def discount(self):                             # Expiry pe based
        if self.expiry_days <= 3: return 40
        elif self.expiry_days <= 7: return 20
        else: return 5


# Cart — @dataclass use kiya
@dataclass
class Cart:
    customer_name : str
    items         : list = field(default_factory=list)

    def add(self, product, qty):
        self.items.append((product, qty))
        print(f"  🛒 Added: {qty}x {product.name}")

    @property
    def total(self):
        return sum(p.final_price * q for p, q in self.items)

    def checkout(self):
        print(f"\n{'═'*44}")
        print(f"  ORDER SUMMARY — {self.customer_name}")
        print(f"{'═'*44}")
        for product, qty in self.items:
            product.purchase(qty)
        print(f"{'─'*44}")
        print(f"  TOTAL : ₹{self.total:,.2f}")
        print(f"{'═'*44}")


# Use karo
laptop  = ElectronicProduct("Dell Laptop",  65000, 5, 2)
shirt   = FashionProduct("Polo Shirt",  1200, 20, "L")
milk    = GroceryProduct("Amul Milk",    60, 50, 2)    # 40% off — expiry 2 days!

print("PRODUCTS:")
print(laptop)
print(shirt)
print(milk)
print()

cart = Cart("Ankit")
cart.add(laptop, 1)
cart.add(shirt,  2)
cart.add(milk,   3)
cart.checkout()


# ══════════════════════════════════════════════════════════════════
#  FLOW
# ══════════════════════════════════════════════════════════════════
'''
Flow
   Function Decorator
         ↓
   def decorator(func):           ← function accept karo
       @functools.wraps(func)     ← naam preserve karo — HAMESHA
       def wrapper(*args, **kwargs):
           ... extra kaam before ...
           result = func(*args, **kwargs)
           ... extra kaam after ...
           return result
       return wrapper             ← wrapper return karo
         ↓
   @decorator lagao function pe
         ↓
   Arguments chahiye → 3 levels: outer(args) → decorator(func) → wrapper()
         ↓
   Multiple Decorators → Neeche wala pehle, upar wala baad
         ↓
   Class Decorator → __init__ mein func, __call__ mein logic
         ↓
   Built-in Decorators:
   @staticmethod  →  self/cls nahi chahiye
   @classmethod   →  cls chahiye — factory methods
   @property      →  getter/setter/deleter
         ↓
   @dataclass     →  __init__, __repr__, __eq__ auto generate
                     field() for mutable defaults
                     frozen=True for immutable
                     order=True for comparison operators
         ↓
   __slots__      →  Memory save — lakhon objects ke liye
         ↓
   __repr__       →  HAMESHA likho — developer ke liye
   __str__        →  Optional — user ke liye
         ↓
   MRO            →  Child → Left Parent → Right Parent → object
   super()        →  MRO ke hisaab se next class call karta hai
'''


# ══════════════════════════════════════════════════════════════════
#  QUICK REVISION
# ══════════════════════════════════════════════════════════════════
'''
Quick Revision
   ┌──────────────────────┬────────────────────────────────────────┐
   │ Concept              │ Key Point                              │
   ├──────────────────────┼────────────────────────────────────────┤
   │ Decorator            │ Function wrap karo — extra behavior    │
   │ @functools.wraps     │ HAMESHA lagao — naam preserve karo     │
   │ *args, **kwargs      │ Wrapper mein hamesha — koi bhi args    │
   ├──────────────────────┼────────────────────────────────────────┤
   │ Decorator + Args     │ 3 level nesting — outer, decorator,    │
   │                      │ wrapper                                │
   │ Chaining             │ Neeche wala pehle apply hota hai       │
   ├──────────────────────┼────────────────────────────────────────┤
   │ Class Decorator      │ __init__ + __call__ → state maintain   │
   │ Singleton            │ Class decorator se — ek hi object      │
   ├──────────────────────┼────────────────────────────────────────┤
   │ @staticmethod        │ self/cls nahi — utility kaam           │
   │ @classmethod         │ cls — factory method, alternative      │
   │                      │ constructor                            │
   ├──────────────────────┼────────────────────────────────────────┤
   │ @dataclass           │ __init__ __repr__ __eq__ auto generate │
   │ field()              │ Mutable defaults ke liye — list, dict  │
   │ frozen=True          │ Immutable dataclass                    │
   │ order=True           │ <, > operators auto                    │
   ├──────────────────────┼────────────────────────────────────────┤
   │ __slots__            │ Memory save — __dict__ nahi banta      │
   │                      │ Lakhon objects ke liye use karo        │
   ├──────────────────────┼────────────────────────────────────────┤
   │ __repr__             │ HAMESHA likho — developer ke liye      │
   │ __str__              │ Optional — user ke liye                │
   ├──────────────────────┼────────────────────────────────────────┤
   │ MRO                  │ C3 Linearization — Child→Left→Right    │
   │ super()              │ MRO mein next class call karta hai     │
   │ Cooperative MI       │ super() + MRO = sab levels call hote  │
   └──────────────────────┴────────────────────────────────────────┘
'''