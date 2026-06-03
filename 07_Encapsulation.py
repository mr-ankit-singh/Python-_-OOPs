'''
╔══════════════════════════════════════════════════════════════════╗
║                   Encapsulation in Python                        ║
╚══════════════════════════════════════════════════════════════════╝

   - Encapsulation = Data ko chupaana + Usse control karna.
   - Class ke andar data (variables) aur methods ko ek saath
     band kar dena — yahi Encapsulation hai.
   - Bahar se seedha data change na ho sake — iske liye
     access control lagate hain.
   - Real life example:
       ATM machine → andar ka circuit seedha nahi chhute,
       sirf buttons se interact karo.

   Types of Access Modifiers:
   ┌─────────────────────────────────────────────────────────────┐
   │  a) Public    →  var       ( Sab access kar sakte hain )    │
   │  b) Protected →  _var      ( Sirf class + subclass )        │
   │  c) Private   →  __var     ( Sirf usi class ke andar )      │
   └─────────────────────────────────────────────────────────────┘
'''


# ══════════════════════════════════════════════════════════════════
#  a) PUBLIC — var
# ══════════════════════════════════════════════════════════════════
'''
Public Variable / Method
   - Default hota hai — koi special symbol nahi lagta.
   - Class ke andar, bahar, aur subclass — sab jagah access
     ho sakta hai.
   - Koi restriction nahi hoti.

   Key Points:
   ┌─────────────────────────────────────────────────────────────┐
   │  ✦ Koi underscore nahi — normal variable                    │
   │  ✦ Kahin se bhi access karo — class, object, subclass       │
   │  ✦ Python ka default behavior yahi hai                      │
   └─────────────────────────────────────────────────────────────┘
'''

class Student:
    def __init__(self, name, marks):
        self.name  = name       # public variable
        self.marks = marks      # public variable

    def display(self):          # public method
        print(f"Name  : {self.name}")
        print(f"Marks : {self.marks}")


s = Student("Ankit", 85)

# Class ke bahar seedha access — allowed ✅
print(s.name)           # Ankit
print(s.marks)          # 85
s.name = "Rahul"        # modify bhi ho sakta hai — koi rok nahi
s.display()


# ══════════════════════════════════════════════════════════════════
#  b) PROTECTED — _var
# ══════════════════════════════════════════════════════════════════
'''
Protected Variable / Method
   - Naam ke aage ek underscore lagao  →  _var
   - Ye sirf ek convention hai — Python actually rok nahi sakta.
   - Message yeh hai: "Ye internal hai, bahar se use mat karo."
   - Class ke andar aur subclass (child class) mein freely
     access ho sakta hai.
   - Bahar se access technically ho sakta hai par karna nahi
     chahiye — ye programmer ka samjhauta hota hai.

   Key Points:
   ┌─────────────────────────────────────────────────────────────┐
   │  ✦ Ek underscore  →  _var                                   │
   │  ✦ Convention only — Python technically block nahi karta    │
   │  ✦ Class + subclass mein freely use karo                    │
   │  ✦ Bahar se seedha use karna avoid karo                     │
   └─────────────────────────────────────────────────────────────┘
'''

class Employee:
    def __init__(self, name, salary):
        self.name    = name         # public
        self._salary = salary       # protected — convention se

    def display(self):
        # Class ke andar access — perfectly fine ✅
        print(f"Name   : {self.name}")
        print(f"Salary : {self._salary}")


class Manager(Employee):            # subclass
    def showDetails(self):
        # Subclass mein bhi access — allowed ✅
        print(f"Manager : {self.name}")
        print(f"Salary  : {self._salary}")


e = Employee("Ankit", 50000)
e.display()

# Bahar se bhi technically kaam karta hai — par avoid karo ⚠️
print(e._salary)        # 50000 — kaam karta hai par galat practice

m = Manager("Sophia", 90000)
m.showDetails()         # subclass se access — sahi ✅


# ══════════════════════════════════════════════════════════════════
#  c) PRIVATE — __var
# ══════════════════════════════════════════════════════════════════
'''
Private Variable / Method
   - Naam ke aage do underscore lagao  →  __var
   - Python isko Name Mangling se actually hide karta hai.
   - Sirf usi class ke andar access ho sakta hai.
   - Bahar se ya subclass se seedha access nahi hota — Error!
   - Name Mangling:  __var  →  _ClassName__var  (andar se)

   Key Points:
   ┌─────────────────────────────────────────────────────────────┐
   │  ✦ Do underscore  →  __var                                  │
   │  ✦ Sirf class ke andar access                               │
   │  ✦ Bahar se seedha access → AttributeError ❌               │
   │  ✦ Name Mangling hoti hai → _ClassName__var                 │
   │  ✦ Getter/Setter se access dete hain — proper tarika        │
   └─────────────────────────────────────────────────────────────┘
'''

class BankAccount:
    def __init__(self, owner, balance):
        self.owner     = owner          # public
        self.__balance = balance        # private — bahar nahi jaega

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount    # andar se access — ✅
            print(f"✅ ₹{amount} jama kiye — Balance: ₹{self.__balance}")
        else:
            print("❌ Invalid amount")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("❌ Insufficient balance")
        else:
            self.__balance -= amount    # andar se access — ✅
            print(f"✅ ₹{amount} nikale — Balance: ₹{self.__balance}")

    def getBalance(self):               # getter — controlled access
        return self.__balance


acc = BankAccount("Ankit", 10000)
acc.deposit(5000)
acc.withdraw(3000)

# Getter se access — sahi tarika ✅
print(f"Balance : ₹{acc.getBalance()}")

# Seedha access — Error ❌
# print(acc.__balance)    # AttributeError: 'BankAccount' object has
                          # no attribute '__balance'

# Name Mangling se technically access ho sakta hai — par kabhi mat karo ⚠️
print(acc._BankAccount__balance)    # 12000 — ye sirf samjhne ke liye


# ══════════════════════════════════════════════════════════════════
#  NAME MANGLING — Python kaise chupaata hai
# ══════════════════════════════════════════════════════════════════
'''
Name Mangling
   - Jab hum __var likhte hain, Python use rename kar deta hai.
   - New name  →  _ClassName__var
   - Isliye bahar se __var nahi milta — alag naam se store hai.
   - Ye accidental access rokne ke liye hai, deliberately chupaane
     ke liye nahi.
'''

class Demo:
    def __init__(self):
        self.__secret = "Hidden Value"

    def show(self):
        print(self.__secret)            # andar se sahi naam se milta hai


d = Demo()
d.show()                                # Hidden Value ✅

# Name mangling check karo
print(dir(d))                           # '_Demo__secret' dikhega list mein

# print(d.__secret)                     # AttributeError ❌
print(d._Demo__secret)                  # "Hidden Value" — mangled naam se


# ══════════════════════════════════════════════════════════════════
#  PRIVATE + GETTER & SETTER — SAHI TARIKA
# ══════════════════════════════════════════════════════════════════
'''
Private Variables ke saath Getter & Setter
   - Private variable seedha access nahi dete.
   - Getter  →  value return karta hai — padh sako
   - Setter  →  value set karta hai — validation ke saath
   - Yahi Encapsulation ka real fayda hai — data safe + controlled.
'''

class Student:
    def __init__(self, name, age, marks):
        self.name    = name             # public
        self.__age   = age             # private
        self.__marks = marks           # private

    # Getter
    def getAge(self):
        return self.__age

    def getMarks(self):
        return self.__marks

    # Setter — validation ke saath
    def setAge(self, age):
        if age < 5 or age > 100:
            print("❌ Invalid age")
        else:
            self.__age = age
            print(f"✅ Age updated: {self.__age}")

    def setMarks(self, marks):
        if marks < 0 or marks > 100:
            print("❌ Marks 0 se 100 ke beech hone chahiye")
        else:
            self.__marks = marks
            print(f"✅ Marks updated: {self.__marks}")

    def display(self):
        print(f"Name  : {self.name}")
        print(f"Age   : {self.__age}")
        print(f"Marks : {self.__marks}")


s = Student("Ankit", 20, 85)
s.display()

s.setAge(25)            # valid   ✅
s.setAge(200)           # invalid ❌ — validation rok dega

s.setMarks(95)          # valid   ✅
s.setMarks(-10)         # invalid ❌

print(s.getAge())       # getter se access
print(s.getMarks())     # getter se access


# ══════════════════════════════════════════════════════════════════
#  PRIVATE METHOD
# ══════════════════════════════════════════════════════════════════
'''
Private Method
   - Variables ki tarah methods bhi private ho sakte hain.
   - __methodName() — sirf class ke andar call ho sakta hai.
   - Helper/internal kaam ke liye use hota hai.
   - Bahar se call karne pe AttributeError aata hai.
'''

class ATM:
    def __init__(self, pin, balance):
        self.__pin     = pin
        self.__balance = balance

    def __verifyPin(self, entered_pin):     # private method
        return self.__pin == entered_pin

    def __deduct(self, amount):             # private method
        self.__balance -= amount

    # Public method — user yahi call karta hai
    def withdraw(self, entered_pin, amount):
        if not self.__verifyPin(entered_pin):
            print("❌ Wrong PIN")
        elif amount > self.__balance:
            print("❌ Insufficient balance")
        elif amount <= 0:
            print("❌ Invalid amount")
        else:
            self.__deduct(amount)
            print(f"✅ ₹{amount} nikale — Remaining: ₹{self.__balance}")


atm = ATM(1234, 20000)
atm.withdraw(1234, 5000)        # correct pin    ✅
atm.withdraw(9999, 5000)        # wrong pin      ❌
atm.withdraw(1234, 50000)       # low balance    ❌

# Private method bahar se call nahi hoti ❌
# atm.__verifyPin(1234)         # AttributeError


# ══════════════════════════════════════════════════════════════════
#  TEEN TARAH KE ACCESS — EK SAATH DEKHO
# ══════════════════════════════════════════════════════════════════

class Company:
    company_name = "TechCorp"               # public class variable

    def __init__(self, emp_name, salary, account_no):
        self.emp_name   = emp_name          # public
        self._salary    = salary            # protected
        self.__account  = account_no        # private

    def publicInfo(self):
        print(f"Employee : {self.emp_name}")     # public — sab dekh sakte

    def internalInfo(self):
        print(f"Salary : {self._salary}")        # protected — andar use

    def __secretInfo(self):                      # private method
        print(f"Account : {self.__account}")     # sirf yahan

    def showAll(self):
        self.publicInfo()
        self.internalInfo()
        self.__secretInfo()                      # private method andar se call


emp = Company("Ankit", 75000, "ACC-9988")
emp.showAll()

print(emp.emp_name)     # public   — ✅
print(emp._salary)      # protected — technically kaam karta hai ⚠️
# print(emp.__account)  # private  — AttributeError ❌


# ══════════════════════════════════════════════════════════════════
#  FLOW
# ══════════════════════════════════════════════════════════════════
'''
Flow
   Class define karo
         ↓
   Public     →  var      →  Sab jagah access — koi restriction nahi
   Protected  →  _var     →  Convention — class + subclass mein use karo
   Private    →  __var    →  Sirf class ke andar — Name Mangling hoti hai
         ↓
   Private variable bahar kaise dein?
         ↓
   Getter   →  value return karo — padh sake
   Setter   →  value set karo — validation bhi laga sako
         ↓
   Name Mangling
   __var  →  _ClassName__var  (Python andar se rename karta hai)
         ↓
   Private Method bhi ho sakti hai
   __method()  →  sirf class ke andar call hogi
   Bahar se call → AttributeError ❌
'''


# ══════════════════════════════════════════════════════════════════
#  QUICK REVISION
# ══════════════════════════════════════════════════════════════════
'''
Quick Revision
   ┌─────────────────┬──────────┬────────────┬─────────────────────┐
   │                 │ Public   │ Protected  │ Private             │
   ├─────────────────┼──────────┼────────────┼─────────────────────┤
   │ Syntax          │  var     │  _var      │  __var              │
   │ Class andar     │  ✅      │  ✅        │  ✅                │
   │ Subclass        │  ✅      │  ✅        │  ❌                │
   │ Class bahar     │  ✅      │  ⚠️ avoid  │  ❌ (Error)        │
   │ Python kya kare │  Kuch    │  Convention│  Name Mangling      │
   │                 │  nahi    │  only      │  _ClassName__var    │
   ├─────────────────┼──────────┼────────────┼─────────────────────┤
   │ Getter          │  Private var ki value return karna          │
   │ Setter          │  Private var ko set karna + validation      │
   │ Name Mangling   │  __var → _ClassName__var  (Python ka kaam)  │
   │ Private Method  │  __method() → sirf class andar call hogi    │
   └─────────────────┴──────────┴────────────┴─────────────────────┘
'''