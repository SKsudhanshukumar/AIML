#Create a program that takes a user's age as input and prints whether they are eligible to vote or not.
name=input("enter your name:")
f_name=input("enter your father name:")
age=int(input("enter your age:"))
if (age<18):
    print(name,"care of",f_name,"is not eligible for vote his age is",age)
else:
    print(name,"care of",f_name,"is eligible for vote his age is",age)