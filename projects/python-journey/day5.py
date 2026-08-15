from abc import ABC, abstractmethod
# class Dog:
#     def __init__(self,name,breed,age):
#         self.name = name
#         self.breed = breed
#         self.age = age
    
#     def bark(self):
#         print(f"{self.name} says: Woof")

#     def info(self):
#         print(f"{self.name} is a {self.breed}, age {self.age}")

class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self,amount):
        self.__balance = self.__balance + amount
    def withdraw(self,amount):
            if self.__balance >= amount:    
                self.__balance -= amount
            else:
                print(f"Insuffiecient Funds")
    def get_balance(self):
        return self.__balance 

class Animal:
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound
    def speak(self):
        print(f"{self.name} says {self.sound}")
class Dog(Animal):
    def fetch(self):
        print(f"{self.name} fetches the ball!")
    def speak(self):           # overrides Animal's speak!
        print(f"{self.name} barks: WOOF WOOF!")


class Cat(Animal):
    def purr(self):
        print(f"{self.name} purrs")
    def speak(self):           # overrides Animal's speak!
        print(f"{self.name} meows: purrrr")

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def perimeter(self):
        pass
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2*(self.width + self.height)
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
    



if __name__ == "__main__":
    
    # dog1 = Dog("Rex", "German Shepherd", 3)
    # dog2 = Dog("Buddy", "Beagle", 5)
    
    # dog1.bark()
    # dog1.info()
    # dog2.bark()
    # dog2.info()
    
    account = BankAccount("Alvar", 1000)
    account.deposit(500)
    print(account.get_balance())   # 1500
    account.withdraw(200)
    print(account.get_balance())   # 1300
    account.withdraw(5000)         # Insufficient funds!
    print(account.get_balance())   # 1300

    dog = Dog("Rex", "Woof")
    cat = Cat("Whiskers", "Meow")
    
    dog.speak()     # inherited from Animal
   # dog.fetch()     # Dog's own method
    cat.speak()     # inherited from Animal
    #cat.purr()      # Cat's own method
    r = Rectangle(5, 3)
    c = Circle(4)
    
    print(r.area())        # 15
    print(r.perimeter())   # 16
    print(c.area())        # 50.24
    print(c.perimeter())   # 25.12
    
