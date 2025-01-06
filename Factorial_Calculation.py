# method 1
num = int(input("Enter a number "))
fact = 1
for i in range (1,num+1):
    fact = fact * i
print("factorial of ",num,"is",fact)

# method 2
import math

num1 = int(input("Enter a number "))

print("factorial of ",num1,"is",math.factorial(num1))


