#Create a program to calculate the factorial of a given number
n=int(input("enter the number:"))
fact=1
if n==1:
    print("factorial of 1 is 1")
elif (n<0):
    print("factorial of n cannot be negative")
elif (n==0):
    print("factorial of 0 is 1")
else:
    for i in range(1,n+1):
        fact*=i
        print(i)
    print("the factorial of",i,"is",fact)
