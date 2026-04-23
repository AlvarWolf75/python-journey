import string
import math
def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit. Formula: (celsius × 9/5) + 32"""
    return (celsius * 9/5) + 32

def is_palindrome(word: str) -> bool:
    """Check if a word is a palindrome (reads the same backward as forward)."""
    cleaned = word.lower().replace(" ", "")
    return cleaned == cleaned[::-1]
def factorial(n: int) -> int:
   ''' result = 1
    for i in range(1, n + 1):
        result *= i
    return result'''
   if n == 0:
       return 1
   return n * factorial(n - 1)

def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
# Way 1 — slicing (1 line)
def reverse_string(s: str) -> str:
    return s[::-1]     # ← this IS slicing!

# Way 2 — loop (manual, no slicing)
def reverse_string(s: str) -> str:
    result = ""
    for i in range(len(s)-1, -1, -1):
        result += s[i]
    return result

def count_vowels(s):
    count = 0 
    s = s.lower()
    vowel = "aeiou"

    for i in s:
        if i in vowel:
            count += 1
    return count 
def flatten(nested_list: list) -> list:
    """Turn a nested list into a flat list."""
    result = []
    for sublist in nested_list:
        for item in sublist:
            # add item to result here
             result.append(item)
    return result
def average(numbers:list)-> float:
    if numbers == []:
        return 0
    return  sum(numbers) / len(numbers)




if __name__ == "__main__":
    print(celsius_to_fahrenheit(0))      # should print 32.0
    print(celsius_to_fahrenheit(100))    # should print 212.0
    print(celsius_to_fahrenheit(37))     # should print 98.6
    print(is_palindrome("racecar"))      # should print True
    print(is_palindrome("hello"))        # should print False
    print(is_palindrome("Racecar"))      # capital R — True or False?
    print(is_palindrome("race car"))     # space — True or False?
    print(is_palindrome(""))              # empty string — True or False?
    print(factorial(5))    # 120
    print(factorial(3))    # 6
    print(factorial(0))    # 1
    print(is_prime(2))     # True
    print(is_prime(7))     # True
    print(is_prime(10))    # False
    print(is_prime(1))     # False
    print(is_prime(13))    # True
    print(reverse_string("hello"))      # olleh
    print(reverse_string("Python"))     # nohtyP
    print(reverse_string("racecar"))    # racecar
    print(reverse_string("12345"))      # 54321
    print(reverse_string("a"))
    print(count_vowels("hello"))    # 2
    print(count_vowels("Alvar"))    # 2
    print(count_vowels("Python"))   # 1
    print(count_vowels("rhythm"))   # 0 
    print(flatten([[1,2], [3,4], [5,6]]))    # [1, 2, 3, 4, 5, 6]
    print(flatten([[1], [2,3,4], [5]]))      # [1, 2, 3, 4, 5]
    print(flatten([[1,2], [], [3]]))         # [1, 2, 3]
    print(average([1, 2, 3, 4, 5]))    # 3.0
    print(average([10, 20, 30]))       # 20.0
    print(average([95, 87, 92]))       # 91.333...
    print(average([]))   