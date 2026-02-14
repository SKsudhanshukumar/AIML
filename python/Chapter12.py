# # WALRUS OPERATOR
# if (n:=len([1,2,3,4,5]))>3:
#     print(f"List i too  ({n} element, expected <=3)")


# # TYPE DEFINITIONS
# n : int=5
# name:str="Sudhanshu"
# def sum(a:int, b:int)-> int:
#     return a+b
# a=sum(5,6)
# print(a)


# # ADVANCED TYPE HINTS
# from typing import List, Tuple, Dict, Union
# #List of integers
# numbers: List[int] = [1, 2, 3, 4, 5]
# #Tuple of a string and an integer
# person: Tuple [str, int] = ("Alice", 30)
# # Dictionary with string keys and integer values
# scores: Dict [str, int] = {"Alice": 90, "Bob": 85}
# # Union type for variables that can hold multiple types
# identifier: Union [int, str] = "ID123"
# identifier = 12345 # Also valid


# # MATCH CASE
# def http_status (status):
#     match status:
#         case 200:
#             return "OK"
#         case 404:
#             return "Not Found"
#         case 500:
#             return "Internal Server Error"
#         case _:
#             return "Unknown status"
# # Usage
# print(http_status(200)) # Output: OK
# print(http_status (404)) # Output: Not Found
# print(http_status (500)) # Output: Internal Server Error
# print(http_status (403)) # Output: Unknown status


# # DICTIONARY MERGE AND UPDATE OPERATORS
# dict1={"a":1, "b":2}
# dict2={"b":3, "c":4}
# merged=dict1|dict2
# print(merged)


# # EXCEPTION HANDLING
# try:
#     a=int(input("Hey, Enter a number:"))
#     print(a)
# except Exception as e:
#     print(e)


# # RAISING EXCEPTION
# a=int(input("Enter first number"))
# b=int(input("Enter second number"))
# if(b==0):
#     raise ZeroDivisionError("Program is not meant to divide numbers by zero")
# else:
#     print(f"The division a/b is {a/b}")


# # TRY WITH ELSE CLAUSE
# try:
#     a=int(input("Hey, Enter a number:"))
#     print(a)
# except Exception as e:
#     print(e)
# else:
#     print("I am inside else.")


# # TRY WITH FINALLY
# def main():
#     try:
#         a=int(input("Hey, Enter a number:"))
#         print(a)
#         return
#     except Exception as e:
#         print(e)
#         return
#     finally:
#         print("I am inside finally.")

# main()


# # IF __NAME__=='__MAIN__ 
# def myFunc():
#     print("Hello World!")
# if __name__=="__main__":
#     # if this code is directly executed by running the file its present in
#     print("We are directly running this code")
#     myFunc()
#     print(__name__)


# # GLOBAL KEYWORDS
# a=89

# def func():
#     global a 
#     a=3
#     print(a)
# print(a)
# func()


# # ENUMERATE FUNCTION
# list=[1,2,3,4,5,6]
# for  i, item in enumerate(list):
#     print(f"The item number at index {i} is {item}")


# # LIST COMPREHENSIONS
# myList=[1,2,3,4,5,6]
# # squaredList=[]
# # for item in myList:
# #     squaredList.append(item*item)
# #  the alter way to do above operation
# squaredList=[i*i for i in myList]
# print(squaredList)


