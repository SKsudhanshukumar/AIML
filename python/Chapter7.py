# # LOOPS
# # WHILE LOOP
# i=1
# while (i<5):
#     print("Sudhanshu")
#     i+=1

# # Write a program to print the content of a list using while loops
# list=[1,2,3,"Ayush","Sudhanshu",45]
# i=0
# while (i<len(list)):
#     print(list[i])
#     i+=1

# # FOR LOOP
# for i in range(4):
#     print(i)

# l=[1,2,3,4,5,343,632,2,43]
# for i in l:
#     print(i)

# t=(1,423,22,63,85,3,8)
# for i in t:
#     print(i)

# s="Sudhanshu"
# for i in s:
#     print(i)

# # For Loop with else
# l=[1,7,8]
# for item in l:
#     print(item)
# else:
#     print("Done")

# # Break Statement
# for i in range(0,80):
#     if (i==3):
#         break
#     print(i)

# # Continue Statement
# for i in range(10):
#     if(i==5):
#         continue
#     print(i)

# # Pass Statement
# for i in range(10):
#     pass
# print("pass statement")


# # PRACTICE SET


# # 1. Write a program to print multiplication table of a given number using for loop.
# a= int(input("Enter a number: "))
# for i in range(1,11):
#     table=a*i
#     print(f"{a} X {i} = {table}")


# # 2. Write a program to greet all the person names stored in a list 'l' and which starts with S.
# #    l=["Harry", "Soham", "Sachin", "Rahul"]
# l=["Harry", "Soham", "Sachin", "Rahul"]
# for i in l:
#     if (i.startswith("S")):
#         print(f"Hello {i}")


# # 3. Attempt problem 1 using while loop.
# a= int(input("Enter a number: "))
# i=1
# while (i<=10):
#     table=a*i
#     print(f"{a} X {i} = {table}")
#     i+=1


# # 4. Write a program to find whether a given number is prime or not.
# a= int(input("Enter a number: "))
# for i in range(2,a):
#     if(a%i==0):
#         print(f"Number is not prime {a}")
#         break
# else:
#     print(f"Number is prime {a}")


# # 5. Write a program to find the sum of first n natural numbers using while loop.
# n= int(input("Enter a number: "))
# sum=0
# for i in range(0,n+1):
#     sum=sum+i
# print(sum)


# # 6. Write a program to calculate the factorial of a given number using for loop.
# n= int(input("Enter a number: "))
# fact=1
# if(n==1 or n==0):
#     print(f"Factorial is {n}")
# elif(n==2):
#     print(f"Factorial is {n}")
# else:
#     for i in range(1,n+1):
#         fact=fact*i
# print(fact)


# # 7. Write a program to print the following star pattern.
# #      *
# #     ***
# #    ***** for n = 3
# n= int(input("Enter a number: "))
# for i in range(1,n+1):
#     print(" "*(n-i), end="")
#     print("*"*(2*i-1), end="")
#     print("\n")


# # 8. Write a program to print the following star pattern:
# #    *
# #    **
# #    *** for n = 3
# n= int(input("Enter a number: "))
# for i in range(0,n+1):
#     print("*"*i, end="")
#     print("\n")


# # 9. Write a program to print the following star pattern.
# #    ***
# #    * * 
# #    ***for n = 3
# n= int(input("Enter a number: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if(i==1 or i==n or j==1 or j==n):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print("\n")
# # or you can use
# n = int(input("Enter the number: "))
# for i in range(1,n+1):
#     if(i==1 or i==n):
#         print("*"* n, end="")
#     else:
#         print("*", end="")
#         print(" "* (n-2), end="")
#         print("*", end="")
#     print("")

# # 10. Write a program to print multiplication table of n using for loops in reversed order.
# a= int(input("Enter a number: "))
# for i in range(1,11):
#     table=a*(11-i)
#     print(f"{a} X {11-i} = {table}")