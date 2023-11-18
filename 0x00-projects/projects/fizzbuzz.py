"""
FizzBuzz is a very popular programming interview question asked.
Let's try to implement it with python.

The function takes an input

@params number

If the number is divisible by 3, it returns Fizz,
If the number is divisible by 5, it returns Buzz,
If the number is divisible by 5 and 3, it returns FizzBuzz,
Else it returns the number.
"""

def fizzBuzz(number):
    # check is the number is divisible by 3
    if(number % 5 == 0 and number % 3 == 0):
        print("FizzBuzz")
    elif(number % 3 == 0):
        print("Fizz")
    elif(number % 5 == 0):
        print("Buzz")
    else:
        print(number)


fizzBuzz(5)