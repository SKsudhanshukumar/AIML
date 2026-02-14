# # CONDITIONAL STATEMENT
# a=int(input("Enter your age: "))
# # if elif else ladder
# if(a>18):
#     print("You are above the age of consent")
#     print("Good for you")
# elif(a<0):
#     print("You are entering an invalid age")
# elif(a==0):
#     print("You are entering 0 which is not a valid age")
# else:
#     print("You are below the age of consent")
# print("End of Program")


# # PRACTICE SET
# # 1. Write a program to find the greatest of four numbers entered by the user.
# a=int(input("Enter the number:"))
# b=int(input("Enter the number:"))
# c=int(input("Enter the number:"))
# d=int(input("Enter the number:"))
# if(a>b and a>c and a>d):
#     print("Greatest number is a: ",a)
# elif(b>a and b>c and b>d):
#     print("Greatest number is b: ",b)
# elif(c>a and c>b and c>d):
#     print("Greatest number is c: ",c)
# else:
#     print("Greatest number is d: ",d)


# # 2. Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.
# marks1 = int(input("Enter Marks 1: "))
# marks2 = int(input("Enter Marks 2: "))
# marks3 = int(input("Enter Marks 3: "))
# #Check for total percentage
# total_percentage=(100*(marks1 + marks2 + marks3))/300
# if (total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
#     print("You are passed:", total_percentage)
# else:
#     print("You failed, try again next year:", total_percentage)


# # 3. A spam comment is defined as a text containing following keywords: "Make a lot of money", "buy now", "subscribe this", "click this". Write a program to detect these spams.
# p1="Make a lot of money"
# p2="buy now"
# p3="subscribe this"
# p4="click this"
# message=input("Enter your comment: ")
# if((p1 in message) or (p2 in message )or (p3 in message) or (p4 in message)):
#     print("This comment is a spam")
# else:
#     print("This comment is not a spam")


# # 4. Write a program to find whether a given username contains less than 10 characters or not.
# username=input("Enter username")
# if (len(username)<10):
#     print("Your username contains less than 10 characters")
# else:
#     print("All is well!")


# # 5. Write a program which finds out whether a given name is present in a list or not.
# l= ["Harry", "Rohan", "Shubham", "Divya"]
# name = input("Enter your name: ")
# if(name in 1):
#     print("Your name is in the list")
# else:
#     print("Your name is not in the list")


# # 6. Write a program to calculate the grade of a student from his marks from the following scheme:
# # 90-100 => Ex
# # 80-90 => A 
# # 70-80 => B 
# # 60-70 => C 
# # 50-60 => D 
# # <50 => F
# marks=int(input("Enter your marks: "))
# if(marks<=100 and marks>=90):
#     grade = "Ex"
# elif(marks<90 and marks>=80):
#     grade = "A"
# elif(marks<80 and marks>=70):
#     grade = "B"
# elif(marks<70 and marks>=60):
#     grade = "C"
# elif(marks<60 and marks>=50):
#     grade = "D"
# elif(marks<50):
#     grade = "F"
# print("Your grade is:", grade)


# # 7. Write a program to find out whether a given post is talking about "Harry" or not.
# post=input("Enter the post: ")
# if("Sudhanshu".lower() in post.lower()):
#     print("This post is talking about Sudhanshu")
# else:
#     print("This post is not talking about Sudhanshu")

