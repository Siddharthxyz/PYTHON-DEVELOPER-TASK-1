

'''Leap Year Check
 Objective: Determine whether a year is a leap year.
 Input: An integer year (e.g., 2024).
 Output: True if leap year, otherwise False.
 Hint: A year is a leap year if divisible by 4 but not by 100 unless divisible by 400.'''

def leap_uear_check(n):
    if (n % 4 == 0 and n % 100 != 0 ) or (n % 400 == 0):
        return True
    else:
        return False

n = int(input("Enter a year :- "))
print(leap_uear_check(n))