i=0
j=1
next_num=j
n= int(input("enter a number "))

for r in range(n):
    print(next_num,end = " ")
    i , j = j , next_num
    next_num = i + j
print()


