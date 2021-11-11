# Here some magic methods are included. For a full guide on them, check
# Python's Data Model: https://docs.python.org/3/reference/datamodel.html

from __future__ import annotations
from typing import List


class Person:
    def __init__(self, name: str, age: int, parents: List[Person]):
        # Initializes the instance
        self.name = name
        self.age = age
        self.parents = parents

    def __repr__(self) -> str:
        # Official string representation of an object, should look
        # like a valid Python expression
        return f"Person({self.name}, {self.age})"

    def __str__(self) -> str:
        # Informal or nicely printable string presentation
        return f"Name: {self.name} - Age: {self.age} "

    def __lt__(self, other: Person) -> bool:
        # 'Lower than' comparison between ages
        return self.age < other.age

    def __le__(self, other: Person) -> bool:
        # 'Lower or Equals to' comparison between ages
        return self.age <= other.age

    # ... similar for the remaining rich comparison methods
    # (see: https://docs.python.org/3/reference/datamodel.html#object.__lt__)

    def __call__(self):
        # Executed when the instance is 'called'
        print(f"Hi! My name is {self.name} and I'm {self.age} years old!")

    def __len__(self) -> int:
        # The length of the object, in this case the 'age' for example
        return self.age

    def __add__(self, other: Person) -> int:
        # Add operation, in this case we will add the ages
        return self.age + other.age

    # ... similar for the remaining operation methods
    # (see: https://docs.python.org/3/reference/datamodel.html#object.__add__)

    def __getitem__(self, item: int) -> Person:
        # To return an item by index or key
        return self.parents[item]

    def __setitem__(self, item: int, other: Person):
        # To set an item by index or key
        self.parents.insert(item, other)

    def __contains__(self, item: Person) -> bool:
        # To check if an item is contained
        return item in self.parents
    
    def __iter__(self):
        # Provides a generator
        for item in self.parents:
            yield item


if __name__ == "__main__":

    p = Person("Christine", 60, [])  # calls __init__
    p2 = Person("Mary", 30, [p])

    print(repr(p))  # calls __repr__
    print(str(p))  # calls _str__

    print(p < p2)  # calls __lt__
    print(p <= p2)  # calls __le__
    # ... and so on

    p()  # calls __call__
    p2()

    print(len(p))  # calls __len__

    print(p + p2)  # calls __add__

    print(p2[0])  # calls __getitem__

    p3 = Person("John", 96, [])
    p[0] = p3  # calls __setitem__
    print(p[0])

    print(p in p2)  # calls __contains__

    iter_p = iter(p2)
    print(next(iter_p))  # calls __iter__
    