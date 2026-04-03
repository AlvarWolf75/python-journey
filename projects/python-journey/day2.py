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