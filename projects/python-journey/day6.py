import time
def logger_decorator(func):
    def log():
        print("Function starting...")
        func()
        print("Function done!")
    return log

@logger_decorator
def calculate():
    print("2 + 2 = 4")

def timer_decorator(func):
    def timer(*args,**kwargs):
        start = time.time()
        func(*args,**kwargs)
        end = time.time()
        print(end - start) 
    return timer

@timer_decorator
def slow_function():
    time.sleep(1)
    print("Done sleeping!")

def countdown(n):
    for i in range(n,0,-1):
        yield i
def even_numbers(limit):
    for i in range (0,limit+1):
        if i%2 == 0:
            yield i
calculate()
slow_function()
for num in countdown(5):
    print(num)

for num in even_numbers(10):
    print(num)

gen = even_numbers(10)
print(next(gen))    # 0
print(next(gen))    # 2
print(next(gen))    # 4\

def safe_divide(a,b):
    try:
        result = a/b
        print (result)
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except TypeError:
        print ("Please use numbers only!")

def read_file(filename):
    try:
        with open(filename,"r") as f:
            print(f.read())
       
    except FileNotFoundError:
        print("File not found!")
    


with open ("scores.txt","w") as f:
    f.write("Alvar: 95\nBob: 87\nDiana: 92")

with open("scores.txt","r") as f:
    print(f.read())

with open("scores.txt","a") as f:
    f.write("\nEve: 88")

with open("scores.txt","r") as f:
    print(f.read())

if __name__ == "__main__":
    f = open("scores.txt","w")
    f.write("Alvar: 95\nBob: 87\nDiana: 92")
    f.close()
    f = open("scores.txt","r")
    contents = f.read()
    print(contents)
    f.close()
    f =open("scores.txt","a")
    f.write("\nEve: 88")
    f.close()
    f = open("scores.txt","r")
    contents = f.read()
    print(contents)
    f.close()

    safe_divide(10, 2)
    safe_divide(10, 0)
    safe_divide(10, "a")

    read_file("scores.txt")     # exists — print contents
    read_file("missing.txt")    # doesn't exist — error message





