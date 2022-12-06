# Implementing classes in Python
**Resources:**
- [Understanding 'super()' in Python classes](https://realpython.com/python-super/)
- [Official documentation on 'super()'](https://docs.python.org/3/library/functions.html#super)
- [Inheritance and composition in Python classes](https://realpython.com/inheritance-composition-python/)

---

## Inheritance in classes
Inheritance models what is called a "is a" relationship - where **derived classes** are more specific extensions of **base classes** (e.g., a square **is a** rectangle. a rectangle **is a** 2D_polygon).

**Some nomenclature:**
- classes that *inherit* are called **derived classes, subclasses, or subtypes**
- classes from which other classes are *derived* are called **base classes or super classes**
- a **derived class** is said to **"inherit" or "extend"** a **base class**

---

## Composition in classes
Composition models a "has a" relationship - creating complex types by **combining objects of other types**.
(e.g., a cube **has a** square; a dog **has a** tail)

---

## Abstract classes
Abstract classes are base classes which are only intended to be inherited, but never to be instantiated. For example, if we mad a "Tail" class which is supposed to be inherited by "Dog", we would probably never instantiate "Tail" on its own.

To explicitly show that classes are abstract, we can derive them from the abstract base class (ABC)
```
from abc import ABC, abstractclassmethod

class Tail(ABC):
    def __init__(self,length,tufted):
        self.length = length
        self.tufted = tufted

    @abstractclassmethod
    def flick_tail(self):
        pass
```

By explicitly defining abstract classes, other developers will know that (a) they should not instantiate this class directly and (b) if they make a derived class from the abstract class, they must override the abstract class method.

---

## 'super()' in Python classes
In Python, every class by default derives from the **object** class as its base. However, for some specialized use cases (like defining error classes), you might need to use another base class (e.g., "Exception" base class)
```
class MyError(Exception):
    pass

raise MyError()
```
