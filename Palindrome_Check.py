a = input("enter a string:- ")
a= a.lower().replace(" ", "")  # replace is use to remove whitespace
palindrome = (a == a[::-1])
print(palindrome) # it will return true if given string is palindrome
