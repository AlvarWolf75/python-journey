name = "Alvar Kandikatla"
age = 20
print(name)
print(age)
print("My name is", name, "and I am", age, "years old")

your_name = input("What is your name? ")
print(f"Hello {your_name}!")
age = int(input("How old are you? "))

if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a kid.")