'''
╔══════════════════════════════════════════════════════════════════╗
║                   Dunder Methods in Python                       ║
║              ( Magic Methods / Special Methods )                 ║
╚══════════════════════════════════════════════════════════════════╝

   - Dunder = Double UNDERscore  →  __method__
   - Inhe "Magic Methods" ya "Special Methods" bhi kehte hain.
   - Python inhe automatically call karta hai certain situations mein.
   - Hum inhe override karke apni class ka behavior customize kar
     sakte hain.
   - Built-in functions aur operators ke saath kaam karte hain.

   Categories of Dunder Methods:
   ┌─────────────────────────────────────────────────────────────┐
   │  a) Object Initialization & Representation                  │
   │  b) Arithmetic Operators                                    │
   │  c) Comparison Operators                                    │
   │  d) Container / Collection Methods                          │
   │  e) Context Manager Methods                                 │
   └─────────────────────────────────────────────────────────────┘
'''


# ══════════════════════════════════════════════════════════════════
#  a) OBJECT INITIALIZATION & REPRESENTATION
# ══════════════════════════════════════════════════════════════════
'''
__init__, __str__, __repr__, __del__

   __init__  →  Object bante waqt automatically call hota hai.
                Constructor ki tarah kaam karta hai.

   __str__   →  print(obj) karte waqt call hota hai.
                Human-readable string return karta hai.

   __repr__  →  repr(obj) ya shell mein object dekhne pe call hota hai.
                Developer-friendly string return karta hai.

   __del__   →  Object delete hote waqt automatically call hota hai.
                Destructor ki tarah kaam karta hai.

   Key Points:
   ┌─────────────────────────────────────────────────────────────┐
   │  ✦ __init__  →  object creation pe — hamesha call hota hai  │
   │  ✦ __str__   →  print() ke liye — user ko dikhane ke liye   │
   │  ✦ __repr__  →  debugging ke liye — developer ke liye       │
   │  ✦ __del__   →  object destroy hone pe — cleanup kaam       │
   └─────────────────────────────────────────────────────────────┘
'''

class Student:
    def __init__(self, name, marks):
        print("__init__ called — Object ban raha hai!")
        self.name  = name
        self.marks = marks

    def __str__(self):
        # print(obj) karte waqt yahi dikhega
        return f"Student(Name: {self.name}, Marks: {self.marks})"

    def __repr__(self):
        # repr(obj) ya debugging mein yahi dikhega
        return f"Student('{self.name}', {self.marks})"

    def __del__(self):
        print(f"__del__ called — {self.name} ka object delete ho gaya!")


s1 = Student("Ankit", 85)
print(s1)           # __str__  call hoga  → Student(Name: Ankit, Marks: 85)
print(repr(s1))     # __repr__ call hoga  → Student('Ankit', 85)
del s1              # __del__  call hoga


# ══════════════════════════════════════════════════════════════════
#  b) ARITHMETIC OPERATOR DUNDER METHODS
# ══════════════════════════════════════════════════════════════════
'''
Arithmetic Dunder Methods
   - Jab hum apni class ke objects pe +, -, *, / operators use
     karte hain, Python automatically inhe call karta hai.
   - Inhe override karke hum operator ka behavior define kar sakte
     hain apni class ke liye.

   ┌────────────────┬──────────────────────────────────────────┐
   │ Dunder Method  │ Kab call hota hai                        │
   ├────────────────┼──────────────────────────────────────────┤
   │ __add__        │  obj1 + obj2                             │
   │ __sub__        │  obj1 - obj2                             │
   │ __mul__        │  obj1 * obj2                             │
   │ __truediv__    │  obj1 / obj2                             │
   │ __floordiv__   │  obj1 // obj2                            │
   │ __mod__        │  obj1 % obj2                             │
   │ __pow__        │  obj1 ** obj2                            │
   └────────────────┴──────────────────────────────────────────┘
'''

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        # obj1 + obj2 karne pe yahi call hoga
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        # obj1 - obj2 karne pe yahi call hoga
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        # obj * number karne pe yahi call hoga
        return Vector(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        # obj / number karne pe yahi call hoga
        return Vector(self.x / scalar, self.y / scalar)


v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(v1 + v2)      # __add__     →  Vector(4, 6)
print(v1 - v2)      # __sub__     →  Vector(2, 2)
print(v1 * 3)       # __mul__     →  Vector(9, 12)
print(v1 / 2)       # __truediv__ →  Vector(1.5, 2.0)


# ── Arithmetic Example — BankAccount ─────────────────────────────

class BankAccount:
    def __init__(self, owner, balance):
        self.owner   = owner
        self.balance = balance

    def __str__(self):
        return f"{self.owner}: ₹{self.balance}"

    def __add__(self, other):
        # Do accounts merge karo
        merged_balance = self.balance + other.balance
        return BankAccount(f"{self.owner}+{other.owner}", merged_balance)


acc1 = BankAccount("Ankit",  50000)
acc2 = BankAccount("Sophia", 30000)
merged = acc1 + acc2
print(merged)       # Ankit+Sophia: ₹80000


# ══════════════════════════════════════════════════════════════════
#  c) COMPARISON OPERATOR DUNDER METHODS
# ══════════════════════════════════════════════════════════════════
'''
Comparison Dunder Methods
   - Objects ko compare karne ke liye use hote hain.
   - ==, !=, <, >, <=, >= operators ko customize kar sakte hain.
   - sort() bhi inhi pe depend karta hai.

   ┌────────────────┬──────────────────────────────────────────┐
   │ Dunder Method  │ Kab call hota hai                        │
   ├────────────────┼──────────────────────────────────────────┤
   │ __eq__         │  obj1 == obj2                            │
   │ __ne__         │  obj1 != obj2                            │
   │ __lt__         │  obj1 <  obj2                            │
   │ __gt__         │  obj1 >  obj2                            │
   │ __le__         │  obj1 <= obj2                            │
   │ __ge__         │  obj1 >= obj2                            │
   └────────────────┴──────────────────────────────────────────┘
'''

class Student:
    def __init__(self, name, marks):
        self.name  = name
        self.marks = marks

    def __str__(self):
        return f"{self.name}({self.marks})"

    def __eq__(self, other):
        # obj1 == obj2
        return self.marks == other.marks

    def __ne__(self, other):
        # obj1 != obj2
        return self.marks != other.marks

    def __lt__(self, other):
        # obj1 < obj2
        return self.marks < other.marks

    def __gt__(self, other):
        # obj1 > obj2
        return self.marks > other.marks

    def __le__(self, other):
        # obj1 <= obj2
        return self.marks <= other.marks

    def __ge__(self, other):
        # obj1 >= obj2
        return self.marks >= other.marks


s1 = Student("Ankit",  85)
s2 = Student("Sophia", 92)
s3 = Student("Rahul",  85)

print(s1 == s3)     # True   — marks equal hain
print(s1 != s2)     # True   — marks equal nahi
print(s1 <  s2)     # True   — Ankit ke marks kam hain
print(s2 >  s1)     # True   — Sophia ke marks zyada hain

# sort() bhi __lt__ use karta hai
students = [s2, s1, s3]
students.sort()
print([str(s) for s in students])   # Marks ke hisaab se sort hoga


# ══════════════════════════════════════════════════════════════════
#  d) CONTAINER / COLLECTION DUNDER METHODS
# ══════════════════════════════════════════════════════════════════
'''
Container Dunder Methods
   - Apni class ko list/dict ki tarah behave karana.
   - len(), indexing [], in operator, iteration sab support
     kar sakte hain.

   ┌────────────────┬──────────────────────────────────────────┐
   │ Dunder Method  │ Kab call hota hai                        │
   ├────────────────┼──────────────────────────────────────────┤
   │ __len__        │  len(obj)                                │
   │ __getitem__    │  obj[index]                              │
   │ __setitem__    │  obj[index] = value                      │
   │ __delitem__    │  del obj[index]                          │
   │ __contains__   │  item in obj                             │
   │ __iter__       │  for item in obj  (iteration)            │
   │ __next__       │  next() — iterator ke saath              │
   └────────────────┴──────────────────────────────────────────┘
'''

class Classroom:
    def __init__(self):
        self.students = []

    def add(self, name):
        self.students.append(name)

    def __len__(self):
        # len(obj) karne pe
        return len(self.students)

    def __getitem__(self, index):
        # obj[index] karne pe
        return self.students[index]

    def __setitem__(self, index, value):
        # obj[index] = value karne pe
        self.students[index] = value

    def __delitem__(self, index):
        # del obj[index] karne pe
        del self.students[index]

    def __contains__(self, name):
        # name in obj karne pe
        return name in self.students

    def __iter__(self):
        # for loop ke liye
        return iter(self.students)


room = Classroom()
room.add("Ankit")
room.add("Sophia")
room.add("Rahul")

print(len(room))            # __len__      → 3
print(room[0])              # __getitem__  → Ankit
room[1] = "Priya"           # __setitem__
print("Rahul" in room)      # __contains__ → True
del room[2]                 # __delitem__

for student in room:        # __iter__
    print(student)


# ══════════════════════════════════════════════════════════════════
#  e) CONTEXT MANAGER DUNDER METHODS
# ══════════════════════════════════════════════════════════════════
'''
Context Manager — __enter__ & __exit__
   - "with" statement ke saath use hota hai.
   - __enter__  →  with block shuru hone pe call hota hai.
   - __exit__   →  with block khatam hone pe call hota hai.
   - File, database connection, locks ke liye bahut useful hai.
   - Exception aane pe bhi __exit__ call hota hai — cleanup safe
     rahta hai.

   Key Points:
   ┌─────────────────────────────────────────────────────────────┐
   │  ✦ with obj as x  →  __enter__ ka return value x mein aata │
   │  ✦ Block khatam  →  __exit__ automatically call hota hai   │
   │  ✦ Exception pe  →  __exit__ mein exc_type, exc_val milta  │
   │  ✦ Resource management ke liye best practice hai           │
   └─────────────────────────────────────────────────────────────┘
'''

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode     = mode
        self.file     = None

    def __enter__(self):
        # with block shuru hone pe
        print(f"📂 File open ho rahi hai: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file                      # 'as' variable mein aayega

    def __exit__(self, exc_type, exc_val, exc_tb):
        # with block khatam hone pe — exception aaye ya na aaye
        print(f"📁 File band ho rahi hai: {self.filename}")
        if self.file:
            self.file.close()
        if exc_type:
            print(f"⚠️  Exception aaya: {exc_val}")
        return False                          # Exception ko suppress mat karo


# Context manager use karo
with FileManager("test.txt", "w") as f:
    f.write("Hello from Dunder Methods!")
    print("✅ File mein likha gaya")
# with block khatam hote hi __exit__ call hoga


# ── Context Manager — Database Connection Example ─────────────────

class DBConnection:
    def __init__(self, db_name):
        self.db_name    = db_name
        self.connected  = False

    def __enter__(self):
        self.connected = True
        print(f"🟢 Database se connect ho gaye: {self.db_name}")
        return self

    def query(self, sql):
        if self.connected:
            print(f"🔍 Query chal rahi hai: {sql}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connected = False
        print(f"🔴 Database se disconnect ho gaye: {self.db_name}")
        return False


with DBConnection("students_db") as db:
    db.query("SELECT * FROM students")
    db.query("SELECT * FROM marks")
# automatically disconnect


# ══════════════════════════════════════════════════════════════════
#  BONUS — __bool__, __hash__, __call__
# ══════════════════════════════════════════════════════════════════
'''
Kuch Aur Important Dunder Methods

   __bool__  →  bool(obj) ya if obj: check karne pe call hota hai.
   __hash__  →  hash(obj) — dictionary key ya set mein use ke liye.
   __call__  →  obj() — object ko function ki tarah call karne pe.
'''

# __bool__ Example
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def __bool__(self):
        # Account valid hai agar balance > 0 ho
        return self.balance > 0


acc1 = BankAccount(5000)
acc2 = BankAccount(0)

print(bool(acc1))           # True  — balance hai
print(bool(acc2))           # False — balance nahi

if acc1:
    print("✅ Account active hai")
if not acc2:
    print("❌ Account mein balance nahi")


# __call__ Example
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        # Object ko function ki tarah call karo
        return number * self.factor


double = Multiplier(2)
triple = Multiplier(3)

print(double(5))            # __call__ → 10
print(triple(5))            # __call__ → 15
print(double(10))           # __call__ → 20


# ══════════════════════════════════════════════════════════════════
#  SAARE DUNDERS EK SAATH — COMPLETE EXAMPLE
# ══════════════════════════════════════════════════════════════════

class Product:
    def __init__(self, name, price, quantity):
        self.name     = name
        self.price    = price
        self.quantity = quantity

    # Representation
    def __str__(self):
        return f"{self.name} @ ₹{self.price} x {self.quantity}"

    def __repr__(self):
        return f"Product('{self.name}', {self.price}, {self.quantity})"

    # Arithmetic
    def __add__(self, other):
        # Dono products ki total value
        return self.price * self.quantity + other.price * other.quantity

    # Comparison — price se compare
    def __lt__(self, other):
        return self.price < other.price

    def __eq__(self, other):
        return self.price == other.price

    # Container
    def __len__(self):
        return self.quantity

    # Boolean
    def __bool__(self):
        return self.quantity > 0


p1 = Product("Laptop", 55000, 3)
p2 = Product("Phone",  20000, 5)
p3 = Product("Tablet", 15000, 0)

print(p1)                   # __str__
print(repr(p2))             # __repr__
print(p1 + p2)              # __add__  → Total value = 265000
print(p1 > p2)              # __lt__   → True (Laptop costly hai)
print(len(p1))              # __len__  → 3
print(bool(p3))             # __bool__ → False (stock nahi)

products = [p2, p1, p3]
products.sort()             # __lt__ use karega
for p in products:
    print(p)


# ══════════════════════════════════════════════════════════════════
#  FLOW
# ══════════════════════════════════════════════════════════════════
'''
Flow
   Class define karo
         ↓
   __init__    →  Object bante waqt automatically call hota hai
   __str__     →  print(obj) ke liye — human readable
   __repr__    →  repr(obj) ke liye — developer readable
   __del__     →  Object delete hote waqt cleanup
         ↓
   Arithmetic Dunders
   __add__  __sub__  __mul__  __truediv__  →  +  -  *  /  operators
         ↓
   Comparison Dunders
   __eq__  __ne__  __lt__  __gt__  __le__  __ge__  →  ==  !=  <  >  <=  >=
         ↓
   Container Dunders
   __len__  __getitem__  __setitem__  __contains__  __iter__
         ↓
   Context Manager
   __enter__  →  with block shuru
   __exit__   →  with block khatam — exception pe bhi
         ↓
   Special Dunders
   __bool__   →  if obj: check ke liye
   __call__   →  obj() — function ki tarah call
'''


# ══════════════════════════════════════════════════════════════════
#  QUICK REVISION
# ══════════════════════════════════════════════════════════════════
'''
Quick Revision
   ┌──────────────────┬────────────────┬──────────────────────────┐
   │ Category         │ Dunder         │ Trigger                  │
   ├──────────────────┼────────────────┼──────────────────────────┤
   │ Initialization   │ __init__       │ Object() banaate waqt    │
   │ Representation   │ __str__        │ print(obj)               │
   │                  │ __repr__       │ repr(obj) / shell        │
   │ Destructor       │ __del__        │ del obj                  │
   ├──────────────────┼────────────────┼──────────────────────────┤
   │ Arithmetic       │ __add__        │ obj1 + obj2              │
   │                  │ __sub__        │ obj1 - obj2              │
   │                  │ __mul__        │ obj1 * obj2              │
   │                  │ __truediv__    │ obj1 / obj2              │
   ├──────────────────┼────────────────┼──────────────────────────┤
   │ Comparison       │ __eq__         │ obj1 == obj2             │
   │                  │ __lt__         │ obj1 <  obj2             │
   │                  │ __gt__         │ obj1 >  obj2             │
   │                  │ __le__  __ge__ │ <=  >=                   │
   ├──────────────────┼────────────────┼──────────────────────────┤
   │ Container        │ __len__        │ len(obj)                 │
   │                  │ __getitem__    │ obj[i]                   │
   │                  │ __setitem__    │ obj[i] = val             │
   │                  │ __contains__   │ x in obj                 │
   │                  │ __iter__       │ for x in obj             │
   ├──────────────────┼────────────────┼──────────────────────────┤
   │ Context Manager  │ __enter__      │ with obj as x:           │
   │                  │ __exit__       │ with block khatam        │
   ├──────────────────┼────────────────┼──────────────────────────┤
   │ Special          │ __bool__       │ bool(obj) / if obj:      │
   │                  │ __call__       │ obj()                    │
   └──────────────────┴────────────────┴──────────────────────────┘
'''