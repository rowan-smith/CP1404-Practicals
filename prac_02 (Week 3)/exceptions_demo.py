"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
>> When another data type is input instead of integer
2. When will a ZeroDivisionError occur?
>> When any number is divided by 0, E.g. the denominator is 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
>> Not a clue, care to share?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
