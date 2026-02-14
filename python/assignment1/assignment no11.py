# Write a program that checks if a given number is positive, negative, or zero.
n=int(input("enter the number:"))
if (n>=0):
    if(n==0):
        print("the number is equal to zero")
    else:
        print("the number is positive")
else:
    print("the number is negative")