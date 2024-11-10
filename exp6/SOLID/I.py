# I: Interface Segragation Principle
from abc import ABC, abstractmethod


class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass


class Swimmable(ABC):
    @abstractmethod
    def swim(self):
        pass


class Duck(Flyable, Swimmable):
    def fly(self):
        return "Duck is flying"

    def swim(self):
        return "Duck is swimming"


class Fish(Swimmable):
    def swim(self):
        return "Fish is swimming"


# Usage
duck = Duck()
fish = Fish()

print(duck.fly())
print(duck.swim())
print(fish.swim())
