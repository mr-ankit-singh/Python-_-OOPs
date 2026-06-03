'''
╔══════════════════════════════════════════════════════════════════╗
║                  Polymorphism in Python                          ║
╚══════════════════════════════════════════════════════════════════╝

   Definition:
   Polymorphism = "poly" (many) + "morphism" (forms)
   One thing, many forms.

   In programming:
   The ability of a single function, method, or operator to work
   differently based on the object or data it is applied to.

   Real life example:
   A person behaves differently in different roles —
   same person, different behavior:
     → As a Son    : respects parents
     → As a Teacher: teaches students
     → As a Friend : jokes around

   In Python:
   The same method name works differently for different classes.
   Python decides at runtime which version to call — based on
   the object type. This is called Runtime Polymorphism.

   Types of Polymorphism in Python:
   ┌─────────────────────────────────────────────────────────────┐
   │  a) Duck Typing              ( Python ka apna style )       │
   │  b) Method Overriding        ( Inheritance ke saath )       │
   │  c) Operator Overloading     ( Dunder methods se )          │
   │  d) Method Overloading       ( Python mein kaise hota hai ) │
   └─────────────────────────────────────────────────────────────┘
'''


# ══════════════════════════════════════════════════════════════════
#  a) DUCK TYPING
# ══════════════════════════════════════════════════════════════════
'''
Duck Typing
   "If it walks like a duck and quacks like a duck,
    it is a duck."

   Python mein:
   Hum object ki class nahi dekhte — sirf yeh dekhte hain
   ki uske paas woh method hai ya nahi.
   Agar method hai → chalao, chahe object kisi bhi class ka ho.

   No inheritance required — just same method name.

   Key Points:
   ┌─────────────────────────────────────────────────────────────┐
   │  ✦ Class se koi matlab nahi — method hona chahiye          │
   │  ✦ Inheritance zaroori nahi                                │
   │  ✦ Python dynamically decide karta hai runtime pe          │
   │  ✦ Code flexible aur reusable banta hai                    │
   └─────────────────────────────────────────────────────────────┘
'''

class Dog:
    def sound(self):
        print("Dog  : Woof Woof! 🐕")

    def info(self):
        print("I am a Dog.")


class Cat:
    def sound(self):
        print("Cat  : Meow Meow! 🐈")

    def info(self):
        print("I am a Cat.")


class Cow:
    def sound(self):
        print("Cow  : Moo Moo! 🐄")

    def info(self):
        print("I am a Cow.")


# Ek common function — kisi bhi object ke saath kaam karta hai
def make_sound(animal):
    animal.sound()          # bas method chahiye — class se matlab nahi
    animal.info()


# Alag-alag objects — same function, alag-alag behavior
d = Dog()
c = Cat()
w = Cow()

make_sound(d)
print()
make_sound(c)
print()
make_sound(w)

# Loop mein bhi — yahi Duck Typing ki power hai
print()
animals = [Dog(), Cat(), Cow(), Dog()]
for animal in animals:
    animal.sound()


# ── Duck Typing — Real Example (File Readers) ────────────────────

class PDFReader:
    def read(self):
        print("PDF file pad raha hai...")

    def close(self):
        print("PDF band kar diya.")


class WordReader:
    def read(self):
        print("Word document pad raha hai...")

    def close(self):
        print("Word document band kar diya.")


class ExcelReader:
    def read(self):
        print("Excel sheet pad raha hai...")

    def close(self):
        print("Excel sheet band kar diya.")


def process_file(reader):       # reader koi bhi ho — bas read() chahiye
    reader.read()
    reader.close()


process_file(PDFReader())
process_file(WordReader())
process_file(ExcelReader())


# ══════════════════════════════════════════════════════════════════
#  b) METHOD OVERRIDING
# ══════════════════════════════════════════════════════════════════
'''
Method Overriding
   - Child class mein Parent ka same naam ka method dobara
     define karna — override karna.
   - Jab child object se method call hoga, child ka chalega.
   - Inheritance ke saath aata hai — yahi "Runtime Polymorphism"
     hai.
   - Parent ka bhi chahiye toh super().method() karo.

   Key Points:
   ┌─────────────────────────────────────────────────────────────┐
   │  ✦ Same method naam — Parent aur Child dono mein           │
   │  ✦ Child ka method override karta hai Parent ka            │
   │  ✦ Runtime pe decide hota hai kaun sa chalega              │
   │  ✦ super().method() se Parent wala bhi call kar sakte hain │
   └─────────────────────────────────────────────────────────────┘
'''

class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        print("Shape ka area — override karo!")

    def describe(self):
        print(f"Color : {self.color}")
        self.area()             # runtime pe sahi child ka chalega


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):             # Override ✅
        result = 3.14 * self.radius ** 2
        print(f"Circle ka area  : {result:.2f}")


class Rectangle(Shape):
    def __init__(self, color, length, breadth):
        super().__init__(color)
        self.length  = length
        self.breadth = breadth

    def area(self):             # Override ✅
        print(f"Rectangle ka area : {self.length * self.breadth}")


class Triangle(Shape):
    def __init__(self, color, base, height):
        super().__init__(color)
        self.base   = base
        self.height = height

    def area(self):             # Override ✅
        print(f"Triangle ka area  : {0.5 * self.base * self.height}")


shapes = [
    Circle("Red", 7),
    Rectangle("Blue", 5, 10),
    Triangle("Green", 8, 6)
]

for shape in shapes:
    shape.describe()            # describe() same — area() alag alag ✅
    print()


# ── Method Overriding — Payment System ───────────────────────────

class Payment:
    def __init__(self, amount):
        self.amount = amount

    def pay(self):
        print(f"₹{self.amount} ka payment ho raha hai...")

    def receipt(self):
        print(f"Receipt generate ho rahi hai — ₹{self.amount}")
        self.pay()              # runtime pe sahi pay() chalega


class CashPayment(Payment):
    def pay(self):              # Override ✅
        print(f"₹{self.amount} cash mein diya.")


class UPIPayment(Payment):
    def __init__(self, amount, upi_id):
        super().__init__(amount)
        self.upi_id = upi_id

    def pay(self):              # Override ✅
        print(f"₹{self.amount} UPI se diya — ID: {self.upi_id}")


class CardPayment(Payment):
    def __init__(self, amount, card_no):
        super().__init__(amount)
        self.card_no = card_no

    def pay(self):              # Override ✅
        print(f"₹{self.amount} card se diya — Card: xxxx{self.card_no[-4:]}")


payments = [
    CashPayment(500),
    UPIPayment(1200, "ankit@upi"),
    CardPayment(3000, "1234567890123456")
]

for p in payments:
    p.receipt()
    print()


# ══════════════════════════════════════════════════════════════════
#  c) OPERATOR OVERLOADING
# ══════════════════════════════════════════════════════════════════
'''
Operator Overloading
   - Same operator (+, -, *, ==, >) ko apni class ke objects
     pe custom behavior dena.
   - Dunder methods se hota hai — __add__, __sub__, __eq__ etc.
   - Python internally operator ko dunder method pe map karta hai.

   Operator     →   Dunder Method
   ┌────────────┬──────────────────────────────────────────────┐
   │  +         │  __add__(self, other)                        │
   │  -         │  __sub__(self, other)                        │
   │  *         │  __mul__(self, other)                        │
   │  /         │  __truediv__(self, other)                    │
   │  ==        │  __eq__(self, other)                         │
   │  !=        │  __ne__(self, other)                         │
   │  <         │  __lt__(self, other)                         │
   │  >         │  __gt__(self, other)                         │
   │  str(obj)  │  __str__(self)                               │
   │  len(obj)  │  __len__(self)                               │
   └────────────┴──────────────────────────────────────────────┘
'''

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):           # + operator overload
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):           # - operator overload
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):          # * operator overload
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):            # == operator overload
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):            # < operator overload
        mag_self  = (self.x**2  + self.y**2)  ** 0.5
        mag_other = (other.x**2 + other.y**2) ** 0.5
        return mag_self < mag_other


v1 = Vector(3, 4)
v2 = Vector(1, 2)
v3 = Vector(3, 4)

print(v1 + v2)          # __add__  →  Vector(4, 6)
print(v1 - v2)          # __sub__  →  Vector(2, 2)
print(v1 * 3)           # __mul__  →  Vector(9, 12)
print(v1 == v3)         # __eq__   →  True
print(v1 == v2)         # __eq__   →  False
print(v2 < v1)          # __lt__   →  True


# ── Operator Overloading — Student Marks ─────────────────────────

class Student:
    def __init__(self, name, marks):
        self.name  = name
        self.marks = marks

    def __str__(self):
        return f"{self.name}({self.marks})"

    def __add__(self, other):           # Do students ki marks jodo
        total = self.marks + other.marks
        return f"Combined Marks: {total}"

    def __gt__(self, other):            # Kaun zyada marks wala?
        return self.marks > other.marks

    def __eq__(self, other):            # Same marks?
        return self.marks == other.marks

    def __lt__(self, other):
        return self.marks < other.marks


s1 = Student("Ankit",  85)
s2 = Student("Sophia", 92)
s3 = Student("Rahul",  85)

print(s1 + s2)          # __add__ →  Combined Marks: 177
print(s1 > s2)          # __gt__  →  False
print(s1 == s3)         # __eq__  →  True

# sort() bhi __lt__ use karta hai
students = [s2, s1, s3]
students.sort()
print([str(s) for s in students])      # Marks ke hisaab se sort


# ══════════════════════════════════════════════════════════════════
#  d) METHOD OVERLOADING
# ══════════════════════════════════════════════════════════════════
'''
Method Overloading
   - Same method naam — alag alag arguments ke saath.
   - Java / C++ mein directly support hota hai.
   - Python mein directly nahi hota — last definition win karti.
   - Python mein alternatives:
       1. Default arguments
       2. *args
       3. **kwargs

   Key Points:
   ┌─────────────────────────────────────────────────────────────┐
   │  ✦ Python mein same naam ka sirf last method rahega        │
   │  ✦ Default arguments se simulate kar sakte hain            │
   │  ✦ *args se variable arguments handle kar sakte hain       │
   │  ✦ **kwargs se named arguments handle kar sakte hain       │
   └─────────────────────────────────────────────────────────────┘
'''

# Python mein overloading directly nahi hoti — last definition jeetti hai
class Demo:
    def greet(self):
        print("Hello!")

    def greet(self, name):          # Ye wala rahega — pehla overwrite
        print(f"Hello, {name}!")

d = Demo()
# d.greet()           # ❌ Error — pehla wala gone
d.greet("Ankit")      # ✅ sirf yahi kaam karta hai


# ── Method 1: Default Arguments ──────────────────────────────────

class Calculator:
    def add(self, a, b, c=0, d=0):          # default arguments
        result = a + b + c + d
        print(f"Sum : {result}")


calc = Calculator()
calc.add(10, 20)            # c=0, d=0 by default
calc.add(10, 20, 30)        # d=0 by default
calc.add(10, 20, 30, 40)    # sab arguments


# ── Method 2: *args — Variable Arguments ─────────────────────────

class Calculator:
    def add(self, *args):                   # kitne bhi numbers do
        result = sum(args)
        print(f"Sum of {args} = {result}")


calc = Calculator()
calc.add(10, 20)
calc.add(10, 20, 30)
calc.add(1, 2, 3, 4, 5, 6, 7)


# ── Method 3: **kwargs — Keyword Arguments ───────────────────────

class Student:
    def setInfo(self, **kwargs):
        for key, value in kwargs.items():
            print(f"{key} : {value}")


s = Student()
s.setInfo(name="Ankit", age=20)
print()
s.setInfo(name="Sophia", age=22, course="BTech", marks=88)


# ══════════════════════════════════════════════════════════════════
#  POLYMORPHISM WITH FUNCTIONS — len() print() type()
# ══════════════════════════════════════════════════════════════════
'''
Built-in Functions aur Polymorphism
   - Python ke built-in functions khud polymorphic hain.
   - len() — string pe bhi, list pe bhi, tuple pe bhi kaam karta.
   - print() — int, float, string, object — sab print ho jaata.
   - type() — kisi bhi object ka type bata deta.
   - Ye sab Duck Typing pe hi kaam karte hain.
'''

print(len("Hello"))             # string  — 5
print(len([1, 2, 3, 4]))        # list    — 4
print(len((10, 20, 30)))        # tuple   — 3
print(len({"a": 1, "b": 2}))   # dict    — 2

print()
print(10)                       # int
print(3.14)                     # float
print("Ankit")                  # string
print([1, 2, 3])                # list

print()
print(type(10))                 # <class 'int'>
print(type("Hi"))               # <class 'str'>
print(type([1, 2]))             # <class 'list'>


# ══════════════════════════════════════════════════════════════════
#  COMPLETE REAL WORLD EXAMPLE — NOTIFICATION SYSTEM
# ══════════════════════════════════════════════════════════════════

class Notification:
    def __init__(self, message):
        self.message = message

    def send(self):
        print(f"Sending: {self.message}")

    def log(self):
        print(f"[LOG] Notification triggered.")
        self.send()             # runtime pe sahi send() chalega


class EmailNotification(Notification):
    def __init__(self, message, email):
        super().__init__(message)
        self.email = email

    def send(self):             # Override ✅
        print(f"📧 Email sent to {self.email} : {self.message}")


class SMSNotification(Notification):
    def __init__(self, message, phone):
        super().__init__(message)
        self.phone = phone

    def send(self):             # Override ✅
        print(f"📱 SMS sent to {self.phone} : {self.message}")


class WhatsAppNotification(Notification):
    def __init__(self, message, number):
        super().__init__(message)
        self.number = number

    def send(self):             # Override ✅
        print(f"💬 WhatsApp sent to {self.number} : {self.message}")


class PushNotification(Notification):
    def __init__(self, message, device_id):
        super().__init__(message)
        self.device_id = device_id

    def send(self):             # Override ✅
        print(f"🔔 Push sent to device {self.device_id} : {self.message}")


# Ek function — sab types handle karta hai (Duck Typing)
def notify_all(notifications):
    for n in notifications:
        n.log()
        print()


notifications = [
    EmailNotification("Your order is placed!", "ankit@gmail.com"),
    SMSNotification("OTP: 4821", "9876543210"),
    WhatsAppNotification("Meeting at 5 PM", "9123456789"),
    PushNotification("New message received!", "DEVICE-XK291")
]

notify_all(notifications)


# ══════════════════════════════════════════════════════════════════
#  FLOW
# ══════════════════════════════════════════════════════════════════
'''
Flow
   Polymorphism = One name, Many behaviors
         ↓
   Duck Typing
   → Inheritance nahi chahiye
   → Bas method hona chahiye object mein
   → make_sound(animal) — koi bhi animal chale
         ↓
   Method Overriding
   → Inheritance ke saath
   → Child ka method Parent ka override karta hai
   → Runtime pe decide hota hai — Runtime Polymorphism
   → super().method() se Parent ka bhi call kar sakte hain
         ↓
   Operator Overloading
   → Dunder methods se — __add__, __eq__, __lt__ etc.
   → Custom objects pe +, ==, < operators kaam karte hain
         ↓
   Method Overloading (Python style)
   → Direct nahi hoti — last definition rahti hai
   → Default arguments / *args / **kwargs se simulate karo
         ↓
   Built-in functions — len(), print(), type() — khud polymorphic
'''


# ══════════════════════════════════════════════════════════════════
#  QUICK REVISION
# ══════════════════════════════════════════════════════════════════
'''
Quick Revision
   ┌──────────────────────┬────────────────────────────────────────┐
   │ Type                 │ Key Point                              │
   ├──────────────────────┼────────────────────────────────────────┤
   │ Duck Typing          │ Class se matlab nahi — method chahiye  │
   │                      │ Inheritance zaroori nahi               │
   ├──────────────────────┼────────────────────────────────────────┤
   │ Method Overriding    │ Child ka method Parent ka override kare│
   │                      │ Runtime Polymorphism — runtime pe      │
   │                      │ decide hota hai kaun sa chalega        │
   │                      │ super().method() → Parent ka bhi chalao│
   ├──────────────────────┼────────────────────────────────────────┤
   │ Operator Overloading │ Dunder methods se — __add__, __eq__    │
   │                      │ Custom objects pe operators kaam kare  │
   ├──────────────────────┼────────────────────────────────────────┤
   │ Method Overloading   │ Python mein direct nahi hoti           │
   │                      │ Default args/ *args / **kwargs use karo│
   ├──────────────────────┼────────────────────────────────────────┤
   │ Built-in Polymorphism│ len(), print(), type() — already poly  │
   └──────────────────────┴────────────────────────────────────────┘
'''