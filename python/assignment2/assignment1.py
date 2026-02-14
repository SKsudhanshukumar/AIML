#write a program to print Fibonacci series in python
n=int(input("enter the number:"))
fab1=0
fab2=1
if (n==1):
    print("the fibonacci series",fab1)
elif (n==2):
    print("the fibonacci series",fab2)
else:
    print(fab1)
    print(fab2)
    for i in range(2,n):
        fab=fab1+fab2
        print(fab)
        fab1=fab2
        fab2=fab
