'''Objective: Check if a number equals the sum of its digits raised to the power of the
number of digits.
Input: An integer nnn.
Output: True or False.
Example: 153 is an Armstrong number because 13+53+33=1531^3 + 5^3 + 3^3 =
15313+53+33=153.
Hint: Convert to a string to calculate the length and power.
'''
num = int(input("enter a number"))
str_num = str(num)
num1 = 0
for i in str_num:
    num1=num1+(int(i)**3)
print(num == num1)