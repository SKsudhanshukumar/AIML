# # FUNCTIONS

# def avg():
#     a=int(input("Enter the number: "))
#     b=int(input("Enter the number: "))
#     c=int(input("Enter the number: "))
#     avg=(a+b+c)/3
#     print(avg)
# # FUNCTION CALL
# avg()
# avg()

# def goodDay():
#     print("Good Day")

# goodDay()


# # FUNCTION WITH ARGUMENTS
# def greet(name):
#     gr="Hello "+name
#     return gr

# a=greet("Sudhanshu")
# print(a)

# def goodDay(name,ending):
#     print("Good Day, "+ name)
#     print(ending)
#     return "ok"

# a=goodDay("Sudhanshu","Thank you")
# print(a)


# # DEFAULT PARAMETER VALUE
# def greet(name="stranger"):
#     print("Hello "+name)
# greet()


# # RECURSION
# def factorial(n):
#     if(n==1 or n==0):
#         return 1
#     return n*factorial(n-1)

# n=int(input("Enter your number: "))
# print(f"The factorial of this number is: {factorial(n)}")


# # PRACTICE SET
# # 1. Write a program using function to find greatest of three numbers.
# def greatestNumber(a,b,c):
#     if(a>b and a>c):
#         print(f"the greatest number is: {a}")
#     elif(b>a and b>c):
#         print(f"the greatest number is: {b}")
#     else:
#         print(f"the greatest number is: {c}")
# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# c=int(input("Enter thrid number: "))
# greatestNumber(a,b,c)


# # 2. Write a python program using function to convert celsius to fahrenheit.
# def tempConverter(f):
#     c=5*(f-32)/9
#     return c
# f=int(input("Enter temperature in F: "))
# print(f"{round(tempConverter(f),2)}")


# # 3. How do you prevent a python print function to print a new line at the end.
# print("a")
# print("b")
# print("c ", end="")
# print("d", end="")


# # 4. Write a recursive function to calculate the sum of first n natural numbers.
# def n_natural_sum(n):
#     if(n==1):
#         return 1
#     return (n+n_natural_sum(n-1))
# n=int(input("Enter your number: "))
# print(n_natural_sum(n))

# # 5. Write a python function to print first n lines of the following pattern:
# # ***
# # **
# # *
# def pattern(n):
#     if(n==0):
#         return
#     print("*"*n)
#     return pattern(n-1) 
# n=int(input("Enter your number: "))
# pattern(n)


# # 6. Write a python function which convert inches to centimeters.
# def inch_to_cm(inch):
#     return inch*2.54
# n=int(input("Enter value in inches: "))
# print(f"The corresponding value in cms is: {inch_to_cm(n)}")


# # 7. Write a python function to remove a given word from a list and strip it at the same time.
# def rem(l,word):
#     n=[]
#     for item in l:
#         if not(item==word):
#             n.append(item.strip(word))
#     return n
# l=["Sudhanshu", "Ayush", "Shubham", "anshu"]
# print(rem(l,"hu"))


# # 8. Write a python function to print multiplication table of a given number.
# def table(n):
#     for i in range(1,11):
#         print(f"{n} X {i} = {n*i}")
# n=int(input("Enter your number: "))
# table(n)