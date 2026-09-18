import time
list1  = [5, 10, 15, 20, 25, 30]

print(list1[-3:])
print(list1[::2])
print(list1[::-1])
print(list1[2:5])

list2 = [1,2,3,4,5,6,7,8,9,10]
list3 = [] 
for i in list2:
    if i == 5:
        continue
    if i == 8 :
        break
    print(i)
def summarize(*args,**kwargs):
    for i in args:
        print(i)
    for j,k in kwargs.items():
        print(f"{j} : {k}")

summarize("hello", "world", author="Alvar", year=2026)

def power(base,exp):
    if exp == 0:
         return 1
    else:
        return base * power(base,exp-1)
print(power(2, 3))    # 8
print(power(3, 4))    # 81
print(power(5, 0))    # 1

class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self,amount):
        self.__balance = amount+ self.__balance

    def withdraw(self,amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Insuffiecient Funds")

    def get_balance(self):
        return self.__balance
    def __str__(self):
        return(f"Account: {self.owner} | Balance: $ {self.__balance}")


class Animal():
    def __init__(self,name,sound):
       self.name = name
       self.sound = sound

    def speak(self):
        print(f"{self.name} says {self.sound}")

class Dog(Animal):
    def __init__(self,name,sound,breed):
        super().__init__(name,sound)
        self.breed = breed
    def speak(self):
        print(f"{self.name} barks: WOOF!") 
    def fetch (self):
        print(f"{self.name} fetches the ball!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows: purr")
    
    def purr(self):
        print(f"{self.name} purrs...")

from abc import ABC, abstractmethod
class Shape():
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        return (self.width*self.height)
    def perimeter(self):
        return (2*(self.width+self.height))
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return (3.14* self.radius**2)
    def perimeter(self):
        return(2 * 3.14 * self.radius)

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        print("Function starting...")
        func()
        print("Function done!")
    return wrapper

@logger_decorator
def calculate():
    print("2 + 2 = 4")

def countdown(n):
    while n > 0:
        yield n 
        n-=1

def safe_divide(a, b):
    try:
        result = a/b
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except TypeError:
        print("Please use numbers!")
    else:
        print(result)
    finally:
        print("Done!")
def timer_decorator(func):
    def wrapper(*args,**kwargs):
        start = time.time() 
        func()
        end = time.time()
        print(end - start)
    return wrapper
@timer_decorator
def slow_function():
    
    print("Done!")
def even_numbers(limit):
    for i in range(0, limit+1):
        if i % 2 == 0:
            yield i


    


if __name__ == "__main__":
    account = BankAccount("Alvar", 1000)
    account.deposit(500)
    account.withdraw(200)
    account.withdraw(5000)
    print(account.get_balance())
    print(account)

    dog = Dog("Rex", "Woof", "Beagle")
    cat = Cat("Whiskers", "Meow")
    
    dog.speak()     # Rex barks: WOOF!
    dog.fetch()     # Rex fetches the ball!
    cat.speak()     # Whiskers meows: purr
    cat.purr()      # Whiskers purrs...+
    r = Rectangle(5, 3)
    c = Circle(4)
    print(r.area())        # 15
    print(r.perimeter())   # 16
    print(c.area())        # 50.24
    print(c.perimeter())   # 25.12
    calculate()
    gen = countdown(3)
    print(next(gen))    # 3
    print(next(gen))    # 2
    print(next(gen))    # 1
    with open ("scores.txt","w") as f:
        f.write("Alvar: 95\nBob: 87")
    with open ("scores.txt","r") as f:
        print(f.read())
    with open("scores.txt","a") as f:
        f.write("\nDiana: 92")
    with open ("scores.txt","r") as f:
        print(f.read())

    
    safe_divide(10, 2)    # should print 5.0 then Done!
    print("---")
    safe_divide(10, 0)
    print("---")
    safe_divide(10, "a")
    slow_function()
    for num in even_numbers(10):
        print(num)
    
    print("---")
    
    gen = even_numbers(10)
    print(next(gen))
    print(next(gen))
    print(next(gen))