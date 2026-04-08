"""
name = input("Enter your name: ").capitalize()
age = int(input("What is your age? "))
want = input("what do you want to be?")
print(f"Hello my name is {name} and I am {age} years old and I want to become {want}")
if(age <18):
    print("You're starting young — that's a superpower!")
elif(age <= 25):
    print("Perfect time to go all in!")

else:
    print("Experience is your advantage!")
"""

import random
"""
# Day 2 — Loops
# range(start, stop, step)
for i in range(5):
    print(i)  
# Print 1 to 10
for i in range(1, 11):
    print(i)

# Print only even numbers from 0 to 20
for i in range(0, 21, 2):
    print(i)
# Countdown from 10 to 1
for i in range(10, 0, -1):
    print(i)
print("Blast off! 🚀")

random_number = random.randint(1, 10)
count = 0
num = int(input("Enter a number: "))
while num != random_number:
    if num > random_number:
        print("Too high! Try again.")
        count += 1
    elif num < random_number:
        print("Too low! Try again.")
        count += 1
    num = int(input("Enter a number: "))
print(f"Congratulations! You guessed it in {count} tries!")
"""

"""
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
"""

for i in range(1,13):
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")
    print()
