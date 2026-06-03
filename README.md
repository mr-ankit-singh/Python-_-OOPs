<div align="center">

# 🐍 Python OOPs — Object Oriented Programming

[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![OOP](https://img.shields.io/badge/Paradigm-Object--Oriented-green?style=for-the-badge)](https://docs.python.org/3/tutorial/classes.html)
[![GitHub](https://img.shields.io/badge/GitHub-mr--ankit--singh-black?style=for-the-badge&logo=github)](https://github.com/mr-ankit-singh)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)]()

<br/>

> 📚 **Python Object-Oriented Programming ke concepts ko simply aur clearly samjhane ki koshish — beginners ke liye perfect!**

</div>

---

## 👨‍💻 About This Repository

Yeh repository mere Python OOPs learning journey ka ek hissa hai. Isme sabhi important OOP concepts ko simple code examples ke saath cover kiya gaya hai — taaki koi bhi aasani se samajh sake.

Agar tum Python seekh rahe ho aur OOP concepts ko practically samajhna chahte ho, toh yeh repo tumhare liye hi bana hai! 🚀

---

## 📂 Topics Covered

| # | Topic | Description |
|---|-------|-------------|
| 01 | 🏗️ **Classes & Objects** | Python mein class banana aur object create karna |
| 02 | 🔧 **Constructor (`__init__`)** | Object initialization aur default values |
| 03 | 🔒 **Encapsulation** | Data hiding — public, protected, private attributes |
| 04 | 🧬 **Inheritance** | Single, Multiple, Multilevel, Hierarchical |
| 05 | 🎭 **Polymorphism** | Method Overriding aur Duck Typing |
| 06 | 🎨 **Abstraction** | Abstract classes aur `ABC` module ka use |
| 07 | ✨ **Magic / Dunder Methods** | `__str__`, `__repr__`, `__len__`, `__add__` etc. |
| 08 | 📌 **Class & Static Methods** | `@classmethod` aur `@staticmethod` decorators |
| 09 | 🏷️ **Properties** | `@property`, getter & setter methods |
| 10 | 🔗 **Method Resolution Order (MRO)** | Multiple inheritance mein method lookup order |

---

## 🧠 Concepts at a Glance

### 🏗️ Class & Object
```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi! Main {self.name} hoon aur meri age {self.age} hai.")

s1 = Student("Ankit", 21)
s1.introduce()
```

---

### 🧬 Inheritance
```python
class Animal:
    def speak(self):
        print("Main kuch boltha hoon...")

class Dog(Animal):
    def speak(self):
        print("Woof! Woof! 🐶")

d = Dog()
d.speak()
```

---

### 🎭 Polymorphism
```python
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        return 3.14 * 5 * 5

class Square(Shape):
    def area(self):
        return 4 * 4

for shape in [Circle(), Square()]:
    print(f"Area: {shape.area()}")
```

---

### 🔒 Encapsulation
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # Private variable

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount
```

---

### 🎨 Abstraction
```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car start ho gayi! 🚗")
```

---

## 🚀 How to Run

**Step 1 — Repository Clone Karo**
```bash
git clone https://github.com/mr-ankit-singh/Python-_-OOPs.git
```

**Step 2 — Folder mein Jao**
```bash
cd Python-_-OOPs
```

**Step 3 — File Run Karo**
```bash
python filename.py
```

> ✅ Koi extra library install karne ki zarurat nahi — sirf Python 3.x chahiye!

---

## 🛠️ Requirements

```
Python >= 3.6
```

Python install nahi hai? Download karo 👉 [python.org](https://www.python.org/downloads/)

---

## 📁 Folder Structure

```
Python-_-OOPs/
│
├── 01_classes_objects/
│   └── basics.py
├── 02_constructor/
│   └── init_method.py
├── 03_encapsulation/
│   └── encapsulation.py
├── 04_inheritance/
│   ├── single.py
│   ├── multiple.py
│   └── multilevel.py
├── 05_polymorphism/
│   └── polymorphism.py
├── 06_abstraction/
│   └── abstraction.py
├── 07_magic_methods/
│   └── dunder.py
├── 08_class_static_methods/
│   └── methods.py
└── README.md
```

---

## 📖 Learning Resources

Agar aur seekhna chahte ho toh yeh resources helpful rahenge:

- 🔗 [Python Official Docs — Classes](https://docs.python.org/3/tutorial/classes.html)
- 🔗 [Real Python — OOP in Python](https://realpython.com/python3-object-oriented-programming/)
- 🔗 [W3Schools — Python OOP](https://www.w3schools.com/python/python_classes.asp)

---

## 🤝 Contributing

Agar tumhe koi bug mile ya koi concept add karna ho:

1. Fork karo 🍴
2. Apni branch banao (`git checkout -b feature/new-concept`)
3. Changes karo aur commit karo (`git commit -m "Add new concept"`)
4. Push karo (`git push origin feature/new-concept`)
5. Pull Request submit karo ✅

---

## 📬 Connect With Me

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-mr--ankit--singh-black?style=flat-square&logo=github)](https://github.com/mr-ankit-singh)

</div>

---

<div align="center">

### ⭐ Agar yeh repo helpful laga toh ek Star zaroor do!

*Happy Coding! 💻🔥*

**Made with ❤️ by Ankit Singh**

</div>