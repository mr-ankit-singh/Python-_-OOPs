'''
╔══════════════════════════════════════════════════════════════════╗
║                   Inheritance in Python                          ║
╚══════════════════════════════════════════════════════════════════╝

   - Inheritance = Ek class ki properties aur methods doosri
     class ko mil jaati hain — bina dobara likhे.
   - Jis class se lete hain  →  Parent / Base / Super Class
   - Jo class leti hai       →  Child  / Derived / Sub Class
   - Real life example:
       Father ke paas property hai → Son ko inherit hoti hai.
       Son apni extra cheezein bhi rakh sakta hai.

   - Code reuse hota hai — ek baar likho, baar baar use karo.
   - Child class Parent ki sab cheezein le sakti hai aur
     apni nai cheezein bhi add kar sakti hai.

   Types of Inheritance:
   ┌─────────────────────────────────────────────────────────────┐
   │  a) Single       →  Ek Parent, Ek Child                    │
   │  b) Multi-level  →  Chain: A → B → C                       │
   │  c) Multiple     →  Do Parent, Ek Child                    │
   │  d) Hierarchical →  Ek Parent, Kai Children                │
   │  e) Hybrid       →  Mix of above types                     │
   └─────────────────────────────────────────────────────────────┘
'''


# ══════════════════════════════════════════════════════════════════
#  BASIC SYNTAX
# ══════════════════════════════════════════════════════════════════
'''
Basic Syntax
   class ParentClass:
       ...

   class ChildClass(ParentClass):   ← parenthesis mein parent ka naam
       ...

   - Child class automatically Parent ke saare
     public aur protected members le leti hai.
   - Private members (__var) inherit nahi hote — directly.
'''

class Animal:                           # Parent class
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def eat(self):
        print(f"{self.name} kha raha hai.")

    def sleep(self):
        print(f"{self.name} so raha hai.")


class Dog(Animal):                      # Child class — Animal se inherit
    def bark(self):                     # apna naya method
        print(f"{self.name} bhaunk raha hai — Woof! 🐕")


d = Dog("Bruno", 3)
d.eat()             # Parent ka method — ✅ inherit hua
d.sleep()           # Parent ka method — ✅ inherit hua
d.bark()            # Dog ka apna method ✅

print(d.name)       # Parent ka variable — ✅ inherit hua
print(d.age)        # Parent ka variable — ✅ inherit hua


# ══════════════════════════════════════════════════════════════════
#  a) SINGLE INHERITANCE
# ══════════════════════════════════════════════════════════════════
'''
Single Inheritance
   - Sabse simple — ek parent, ek child.
   - Child → Parent ki sab cheezein leta hai.
   - Child apni extra cheezein bhi add kar sakta hai.

   Diagram:
        Animal
          ↓
         Dog
'''

class Animal:
    def __init__(self, name, species):
        self.name    = name
        self.species = species

    def breathe(self):
        print(f"{self.name} saans le raha hai.")

    def display(self):
        print(f"Name    : {self.name}")
        print(f"Species : {self.species}")


class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, "Mammal")   # Parent ka init call kiya
        self.breed = breed                       # apna extra variable

    def bark(self):
        print(f"{self.name} bhaunk raha hai!")

    def display(self):                           # Parent ka method override kiya
        Animal.display(self)                     # Parent wala bhi chalao
        print(f"Breed   : {self.breed}")         # extra cheez add ki


d = Dog("Bruno", "Labrador")
d.display()
d.breathe()         # Parent ka method — inherited ✅
d.bark()            # Dog ka method ✅


# ══════════════════════════════════════════════════════════════════
#  super() — PARENT KO CALL KARNE KA SAHI TARIKA
# ══════════════════════════════════════════════════════════════════
'''
super()
   - Parent class ke methods ya __init__ ko call karne ke
     liye super() use karte hain.
   - ParentClass.__init__(self, ...) ki jagah
     super().__init__(...)  likhna better aur clean hai.
   - Multiple inheritance mein super() ka fayda zyada hota hai.
   - MRO (Method Resolution Order) follow karta hai.

   Key Points:
   ┌─────────────────────────────────────────────────────────────┐
   │  ✦ super().__init__()  →  Parent ka constructor call karo   │
   │  ✦ super().method()    →  Parent ka koi bhi method call karo│
   │  ✦ Parent ka naam nahi likhna padta — auto detect karta hai │
   │  ✦ Multiple inheritance mein bhi sahi kaam karta hai        │
   └─────────────────────────────────────────────────────────────┘
'''

class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
        print(f"Vehicle created: {self.brand}")

    def info(self):
        print(f"Brand : {self.brand}")
        print(f"Speed : {self.speed} km/h")


class Car(Vehicle):
    def __init__(self, brand, speed, fuel_type):
        super().__init__(brand, speed)      # super() se parent ka __init__
        self.fuel_type = fuel_type
        print(f"Car created: {self.brand}")

    def info(self):
        super().info()                      # super() se parent ka method
        print(f"Fuel  : {self.fuel_type}")


class ElectricCar(Car):
    def __init__(self, brand, speed, battery):
        super().__init__(brand, speed, "Electric")  # Car ka __init__
        self.battery = battery
        print(f"ElectricCar created: {self.brand}")

    def info(self):
        super().info()                      # Car ka info chalega
        print(f"Battery : {self.battery} kWh")


ec = ElectricCar("Tesla", 250, 100)
print()
ec.info()


# ══════════════════════════════════════════════════════════════════
#  b) MULTI-LEVEL INHERITANCE
# ══════════════════════════════════════════════════════════════════
'''
Multi-level Inheritance
   - Chain ki tarah — A → B → C
   - B, A se inherit karta hai.
   - C, B se inherit karta hai — aur automatically A ki bhi
     sab cheezein mil jaati hain.

   Diagram:
      GrandParent (Animal)
           ↓
        Parent (Dog)
           ↓
         Child (GuideDog)
'''

class Animal:
    def __init__(self, name):
        self.name = name

    def breathe(self):
        print(f"{self.name} saans le raha hai.")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def bark(self):
        print(f"{self.name} bhaunk raha hai!")


class GuideDog(Dog):                    # Dog se inherit — aur Animal bhi aata hai
    def __init__(self, name, breed, owner):
        super().__init__(name, breed)
        self.owner = owner

    def guide(self):
        print(f"{self.name} apne owner {self.owner} ko raasta dikha raha hai.")


gd = GuideDog("Max", "Labrador", "Ankit")
gd.breathe()        # Animal ka — level 1 ✅
gd.bark()           # Dog ka   — level 2 ✅
gd.guide()          # GuideDog ka — apna ✅
print(gd.name)      # Animal ka variable ✅
print(gd.breed)     # Dog ka variable ✅
print(gd.owner)     # GuideDog ka variable ✅


# ══════════════════════════════════════════════════════════════════
#  c) MULTIPLE INHERITANCE
# ══════════════════════════════════════════════════════════════════
'''
Multiple Inheritance
   - Ek child class ke DO ya zyada parent classes hote hain.
   - Dono parents ki sab cheezein child ko mil jaati hain.
   - Python mein supported hai — Java mein nahi hota.
   - Dhyan rakho: agar dono parents mein same method ho toh
     MRO decide karta hai kaun sa chalega.

   Diagram:
      Father     Mother
         ↘      ↙
           Child
'''

class Father:
    def __init__(self, father_name):
        self.father_name = father_name

    def property(self):
        print(f"{self.father_name} ki property inherit hui.")

    def cooking(self):
        print("Father ki cooking style.")


class Mother:
    def __init__(self, mother_name):
        self.mother_name = mother_name

    def care(self):
        print(f"{self.mother_name} ki caring inherit hui.")

    def cooking(self):
        print("Mother ki cooking style.")


class Child(Father, Mother):            # Dono parents
    def __init__(self, name, father_name, mother_name):
        Father.__init__(self, father_name)
        Mother.__init__(self, mother_name)
        self.name = name

    def introduce(self):
        print(f"Mera naam {self.name} hai.")
        print(f"Father : {self.father_name}")
        print(f"Mother : {self.mother_name}")


c = Child("Arjun", "Ramesh", "Sunita")
c.introduce()
c.property()        # Father ka method ✅
c.care()            # Mother ka method ✅
c.cooking()         # Father ka chalega — MRO: Father pehle hai ✅


# ── MRO Check karo ────────────────────────────────────────────────
# Method Resolution Order — kaunsa method pehle dhundha jaayega
print(Child.__mro__)
# (Child, Father, Mother, object)


# ══════════════════════════════════════════════════════════════════
#  d) HIERARCHICAL INHERITANCE
# ══════════════════════════════════════════════════════════════════
'''
Hierarchical Inheritance
   - Ek parent class se kai alag-alag child classes.
   - Sabko same parent ki cheezein milti hain.
   - Har child apni alag extra cheezein add kar sakti hai.

   Diagram:
          Vehicle
        ↙    ↓    ↘
      Car   Bike  Truck
'''

class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def start(self):
        print(f"{self.brand} start ho gaya!")

    def stop(self):
        print(f"{self.brand} ruk gaya.")


class Car(Vehicle):
    def __init__(self, brand, speed, doors):
        super().__init__(brand, speed)
        self.doors = doors

    def info(self):
        print(f"Car   : {self.brand} | Speed: {self.speed} | Doors: {self.doors}")


class Bike(Vehicle):
    def __init__(self, brand, speed, bike_type):
        super().__init__(brand, speed)
        self.bike_type = bike_type

    def info(self):
        print(f"Bike  : {self.brand} | Speed: {self.speed} | Type: {self.bike_type}")


class Truck(Vehicle):
    def __init__(self, brand, speed, payload):
        super().__init__(brand, speed)
        self.payload = payload

    def info(self):
        print(f"Truck : {self.brand} | Speed: {self.speed} | Payload: {self.payload}t")


car   = Car("Toyota", 180, 4)
bike  = Bike("Royal Enfield", 140, "Cruiser")
truck = Truck("Tata", 100, 20)

car.start()         # Vehicle ka method — inherited ✅
car.info()

bike.start()        # Vehicle ka method — inherited ✅
bike.info()

truck.stop()        # Vehicle ka method — inherited ✅
truck.info()


# ══════════════════════════════════════════════════════════════════
#  e) HYBRID INHERITANCE
# ══════════════════════════════════════════════════════════════════
'''
Hybrid Inheritance
   - Upar wale types ka combination hota hai.
   - Real projects mein yahi zyada milta hai.
   - Python ka MRO (C3 Linearization) sahi order handle karta hai.

   Diagram:
         Animal
        ↙      ↘
      Pet      Wild
        ↘      ↙
         Tiger            ← Multiple + Hierarchical = Hybrid
'''

class Animal:
    def __init__(self, name):
        self.name = name

    def breathe(self):
        print(f"{self.name} saans le raha hai.")


class Pet(Animal):
    def __init__(self, name, owner):
        super().__init__(name)
        self.owner = owner

    def cuddle(self):
        print(f"{self.name} apne owner {self.owner} se pyaar kar raha hai.")


class Wild(Animal):
    def __init__(self, name, habitat):
        super().__init__(name)
        self.habitat = habitat

    def hunt(self):
        print(f"{self.name} {self.habitat} mein shikar kar raha hai.")


class Tiger(Pet, Wild):                 # Hybrid — Pet aur Wild dono se
    def __init__(self, name, owner, habitat):
        Pet.__init__(self, name, owner)
        Wild.__init__(self, name, habitat)

    def roar(self):
        print(f"{self.name} dahaad raha hai — ROAR! 🐯")


t = Tiger("Shera", "Zoo Keeper", "Jungle")
t.breathe()         # Animal ka ✅
t.cuddle()          # Pet ka   ✅
t.hunt()            # Wild ka  ✅
t.roar()            # Tiger ka ✅

print(Tiger.__mro__)    # MRO order dekho


# ══════════════════════════════════════════════════════════════════
#  METHOD OVERRIDING
# ══════════════════════════════════════════════════════════════════
'''
Method Overriding
   - Child class mein Parent ka same naam ka method dobara
     likhna — override karna.
   - Child ka method run hoga — Parent wala nahi.
   - Parent wala bhi chahiye toh super().method() karo.
   - Yahi Polymorphism ki neev hai.

   Key Points:
   ┌─────────────────────────────────────────────────────────────┐
   │  ✦ Same method naam — Parent aur Child dono mein           │
   │  ✦ Child ka method automatically chalega                   │
   │  ✦ Parent ka bhi chahiye → super().method() karo           │
   │  ✦ Polymorphism ka base yahi hai                           │
   └─────────────────────────────────────────────────────────────┘
'''

class Shape:
    def area(self):
        print("Shape ka area — override karo!")

    def describe(self):
        print("Main ek Shape hoon.")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):                         # Override — apna formula
        result = 3.14 * self.radius ** 2
        print(f"Circle ka area : {result:.2f}")


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length  = length
        self.breadth = breadth

    def area(self):                         # Override — apna formula
        result = self.length * self.breadth
        print(f"Rectangle ka area : {result}")

    def describe(self):
        super().describe()                  # Parent ka bhi chalao
        print(f"Main {self.length}x{self.breadth} ka Rectangle hoon.")


c = Circle(7)
r = Rectangle(5, 10)

c.area()            # Circle ka override method ✅
r.area()            # Rectangle ka override method ✅
c.describe()        # Parent ka — override nahi kiya ✅
r.describe()        # super() + apna ✅


# ══════════════════════════════════════════════════════════════════
#  isinstance() aur issubclass()
# ══════════════════════════════════════════════════════════════════
'''
isinstance() aur issubclass()
   - isinstance(obj, Class)    →  Check karo obj us class ka hai?
   - issubclass(Child, Parent) →  Check karo Child us Parent se hai?
   - Inheritance chain mein bhi True return karta hai.
'''

class Animal:
    pass

class Dog(Animal):
    pass

class GuideDog(Dog):
    pass


gd = GuideDog()

# isinstance — object check
print(isinstance(gd, GuideDog))     # True  — directly
print(isinstance(gd, Dog))          # True  — inherit hua
print(isinstance(gd, Animal))       # True  — chain se inherit hua
print(isinstance(gd, str))          # False — bilkul alag

# issubclass — class check
print(issubclass(GuideDog, Dog))    # True
print(issubclass(GuideDog, Animal)) # True  — chain mein hai
print(issubclass(Dog, GuideDog))    # False — ulta nahi hota


# ══════════════════════════════════════════════════════════════════
#  PROTECTED VARIABLES IN INHERITANCE
# ══════════════════════════════════════════════════════════════════
'''
Protected Variables aur Inheritance
   - _var (protected) child class mein freely access hoti hai.
   - __var (private) directly child class mein access nahi hoti.
   - Isliye shared data ke liye protected use karo.
'''

class Employee:
    def __init__(self, name, salary):
        self.name     = name            # public
        self._salary  = salary          # protected — child access kar sakta hai
        self.__empId  = "EMP001"        # private — child seedha nahi dekh sakta

    def showId(self):
        print(f"ID : {self.__empId}")   # class ke andar access ✅


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display(self):
        print(f"Name       : {self.name}")
        print(f"Salary     : {self._salary}")    # protected — access ✅
        print(f"Department : {self.department}")
        # print(self.__empId)             # ❌ Error — private, seedha nahi
        self.showId()                     # parent method se access ✅


m = Manager("Sophia", 120000, "Engineering")
m.display()


# ══════════════════════════════════════════════════════════════════
#  MRO — METHOD RESOLUTION ORDER
# ══════════════════════════════════════════════════════════════════
'''
MRO — Method Resolution Order
   - Jab same method kai jagah ho, Python kaunsa choose karega?
   - Python C3 Linearization algorithm use karta hai.
   - ClassName.__mro__ se order dekh sakte hain.
   - Order: Child → Left Parent → Right Parent → object

   Rule — Left se Right, Depth se pehle:
   class D(B, C) aur B(A) aur C(A) ho toh:
   D → B → C → A → object
'''

class A:
    def hello(self):
        print("Hello from A")

class B(A):
    def hello(self):
        print("Hello from B")

class C(A):
    def hello(self):
        print("Hello from C")

class D(B, C):                          # Multiple inheritance
    pass


d = D()
d.hello()                   # B ka chalega — MRO: D→B→C→A
print(D.__mro__)            # (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)


# ══════════════════════════════════════════════════════════════════
#  COMPLETE REAL WORLD EXAMPLE — SCHOOL SYSTEM
# ══════════════════════════════════════════════════════════════════

class Person:
    def __init__(self, name, age, phone):
        self.name  = name
        self.age   = age
        self._phone = phone             # protected

    def display(self):
        print(f"Name  : {self.name}")
        print(f"Age   : {self.age}")

    def contact(self):
        print(f"Phone : {self._phone}")


class Student(Person):
    def __init__(self, name, age, phone, rollno, marks):
        super().__init__(name, age, phone)
        self.rollno = rollno
        self.__marks = marks            # private

    def getMarks(self):
        return self.__marks

    def grade(self):
        m = self.__marks
        if   m >= 75: return "Distinction ⭐"
        elif m >= 60: return "First Class ✅"
        elif m >= 45: return "Second Class"
        else:         return "Fail ❌"

    def display(self):
        super().display()
        print(f"RollNo : {self.rollno}")
        print(f"Marks  : {self.__marks}")
        print(f"Grade  : {self.grade()}")


class Teacher(Person):
    def __init__(self, name, age, phone, subject, salary):
        super().__init__(name, age, phone)
        self.subject  = subject
        self.__salary = salary          # private

    def getSalary(self):
        return self.__salary

    def display(self):
        super().display()
        print(f"Subject : {self.subject}")
        print(f"Salary  : ₹{self.__salary}")


class HeadTeacher(Teacher):             # Multi-level
    def __init__(self, name, age, phone, subject, salary, school):
        super().__init__(name, age, phone, subject, salary)
        self.school = school

    def display(self):
        super().display()
        print(f"School  : {self.school}")


print("═" * 40)
print("STUDENT")
print("═" * 40)
s = Student("Ankit", 18, "9876543210", "S101", 82)
s.display()
s.contact()

print()
print("═" * 40)
print("TEACHER")
print("═" * 40)
t = Teacher("Mrs. Sharma", 40, "9123456789", "Mathematics", 75000)
t.display()
t.contact()

print()
print("═" * 40)
print("HEAD TEACHER")
print("═" * 40)
ht = HeadTeacher("Mr. Verma", 55, "9999988888", "Science", 120000, "ABC School")
ht.display()
ht.contact()

# isinstance checks
print()
print(isinstance(ht, HeadTeacher))     # True
print(isinstance(ht, Teacher))         # True — inherit hua
print(isinstance(ht, Person))          # True — chain se
print(issubclass(HeadTeacher, Person)) # True


# ══════════════════════════════════════════════════════════════════
#  FLOW
# ══════════════════════════════════════════════════════════════════
'''
Flow
   Parent class banao  →  Common cheezein daalo
         ↓
   Child class(Parent) →  Extra cheezein add karo
         ↓
   super().__init__()  →  Parent ka constructor call karo
   super().method()    →  Parent ka method call karo
         ↓
   Method Override     →  Same naam — Child ka chalega
         ↓
   Types:
   Single      →  A → B
   Multi-level →  A → B → C (chain)
   Multiple    →  A, B → C (do parents)
   Hierarchical→  A → B, C, D (kai children)
   Hybrid      →  Upar walo ka mix
         ↓
   MRO  →  Kaun sa method pehle chalega — left to right
         ↓
   isinstance()  →  Object kis class ka hai?
   issubclass()  →  Ek class doosri se inherit karti hai?
'''


# ══════════════════════════════════════════════════════════════════
#  QUICK REVISION
# ══════════════════════════════════════════════════════════════════
'''
Quick Revision
   ┌────────────────────┬──────────────────────────────────────────┐
   │ Concept            │ Key Point                                │
   ├────────────────────┼──────────────────────────────────────────┤
   │ Inheritance        │ Parent ki cheezein Child ko milti hain   │
   │ Syntax             │ class Child(Parent):                     │
   │ super()            │ Parent ka __init__ / method call karo    │
   ├────────────────────┼──────────────────────────────────────────┤
   │ Single             │ A → B — simplest                         │
   │ Multi-level        │ A → B → C — chain                        │
   │ Multiple           │ A, B → C — do parents                    │
   │ Hierarchical       │ A → B, C, D — kai children               │
   │ Hybrid             │ Above ka mix                             │
   ├────────────────────┼──────────────────────────────────────────┤
   │ Method Override    │ Same naam → Child ka chalega             │
   │ super().method()   │ Parent ka method bhi chalao              │
   ├────────────────────┼──────────────────────────────────────────┤
   │ MRO                │ Left → Right — __mro__ se dekho          │
   │ Protected (_var)   │ Child mein freely access ✅             │
   │ Private (__var)    │ Child mein seedha access ❌             │
   ├────────────────────┼──────────────────────────────────────────┤
   │ isinstance(obj, C) │ obj us class ka hai? — chain mein bhi    │
   │ issubclass(A, B)   │ A, B se inherit karta hai?               │ 
   └────────────────────┴──────────────────────────────────────────┘
'''