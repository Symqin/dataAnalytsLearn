# belajar oop 

class Mahasiswa:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def perkenalan(self):
        print(f"Halo, nama saya {self.nama} dan saya berumur {self.umur} tahun.")

mhs1 = Mahasiswa("Alice", 20)
mhs1.perkenalan()  # Output: Halo, nama saya Alice dan saya berumur 20 tahun.

# inheritance
class Animal:
    def speak(self):
        print("Animal speaks")
    
class Dog(Animal):
    def bark(self):
        print("Woof!")

dog = Dog()
dog.speak()  # Output: Animal speaks
dog.bark()   # Output: Woof!

# polimorphism

# func polimorphism

print(len("Hello"))  # Output: 5
print(len([1, 2, 3, 4]))  # Output: 4

# method overriding
class Bird(Animal):
    def speak(self):
        print("Bird chirps")

bird = Bird()
bird.speak()  # Output: Bird chirps

# duck typing

class Cat:
    def bersuara(self):
        print("Meow!")

class Dog:
    def bersuara(self):
        print("Woof!")

class Duck:
    def bersuara(self):
        print("Quack!")

def buat_bersuara(hewan):
    hewan.bersuara()

kucing = Cat()
anjing = Dog()
bebek = Duck()

buat_bersuara(kucing)  # Output: Meow!
buat_bersuara(anjing)  # Output: Woof!
buat_bersuara(bebek)   # Output: Quack!

# encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Atribut privat
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500

# abstraction
from abc import ABC, abstractmethod 

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
circle = Circle(5)
print("Area of circle:", circle.area())  # Output: Area of circle: 78.5


