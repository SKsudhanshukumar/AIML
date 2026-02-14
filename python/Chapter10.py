# class Employee:
#     language="python"
#     salary=1200000

# sudhanshu=Employee()
# sudhanshu.name="Sudhanshu"
# print(sudhanshu.name, sudhanshu.language, sudhanshu.salary)

# ayush=Employee()
# ayush.name="Ayush"
# Employee.salary=1300000 # Changing the attributes
# print(ayush.name, ayush.language, ayush.salary)


# # Self parameter
# class Employee:
#     language="python"
#     salary=1200000
    
#     def getInfo1(self): # Without self we cannot use this method function
#         print(f"The language is {self.language}. The salary is {self.salary}")

#     def getInfo2(self): # Without self we cannot use this method function
#         print(f"The language is {self.language}. The salary is {self.salary}")

#"Sudhanshu=Employee()
#"Sudhanshu.getInfo1() # this one is defined as Employee.getInfo1"Sudhanshu)
# Employee.getInfo1"Sudhanshu)

# #  Static Method
# class Employee:
#     @staticmethod
#     def greet():
#         print("Good morning")

# sudhanshu=Employee()
# sudhanshu.greet()


# # __init__ constructor
# class Employee:
#     language="Python"
#     salary=1200000

#     def __init__(self, name, salary, language): # dunder method which is automatically called
#         self.name=name
#         self.salary=salary
#         self.language=language

# sudhanshu=Employee("Sudhanshu",1300000,"Java")
# print(sudhanshu.name, sudhanshu.salary, sudhanshu.language)


# # PRACTICE SET
# # 1. Create a Class "Programmer" for storing information of few programmers working at Microsoft.
# class Programmer:
#     company="Microsoft"
#     def __init__(self,name,salary,pin):
#         self.name=name
#         self.salary=salary
#         self.pin=pin

# p=Programmer("Sudhanshu", 1200000,245532)
# a=Programmer("Ayush", 1200000,245532)

# print(p.name, p.salary, p.pin, p.company)
# print(a.name, a.salary, a.pin, a.company)


# # 2. Write a class "calculator" capable of finding square, cube and square root of a number.
# class Calculator:
#     def __init__(self,number):
#         self.number=number
    
#     def square(self):
#         print(f"square of a number is: {self.number**2}")
    
#     def cube(self):
#         print(f"the cube of a number: {self.number**3}")

#     def sq_root(self):
#         print(f"the cube of a number: {self.number**(1/2)}")


# n=Calculator(25)
# n.square()
# n.cube()
# n.sq_root()


# # 3. Create a class with a class attribute a; create an object from it and set 'a' directly using object.a = o. Does this change the class attribute?
# class Demo:
#     a=4

# o=Demo()
# print(o.a) # print the class attribute because instance attribute is not present
# o.a=0 # Instance attribute is set
# print(o.a) # print the instance attribute because instance attribute is not present
# print(Demo.a) # print class attribute


# # 4. Add a static method in problem 2, to greet the user with hello.
# class Calculator:
#     def __init__(self,number):
#         self.number=number
    
#     def square(self):
#         print(f"square of a number is: {self.number**2}")
    
#     def cube(self):
#         print(f"the cube of a number: {self.number**3}")

#     def sq_root(self):
#         print(f"the cube of a number: {self.number**(1/2)}")
    
#     @staticmethod
#     def greet():
#         print("Hello")


# n=Calculator(25)
# n.greet()
# n.square()
# n.cube()
# n.sq_root()


# # 5. Write a class Train which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.
# from random import randint
# class Train:
#     def __init__(self, trainNo):
#         self.trainNo=trainNo

#     def book(self, fro, to):
#         print(f"Ticket is booked in train no.: {self.trainNo} from {fro} to {to}")
    
#     def status(self):
#         print(f"Train no: {self.trainNo} is running on time")

#     def fare(self, fro, to):
#         print(f"Ticket is booked in train no.: {self.trainNo} from {fro} to {to} is {randint(22, 555)}")

# t=Train(12392)
# t.book("Rampur", "Delhi")
# t.status()
# t.fare("Rampur", "Delhi")


# 6. Can you change the self-parameter inside a class to something else (say "Sudhanshu"). Try changing self to "slf" or "Sudhanshu" and see the effects.
class Demo:
    def __init__(slf,name):
        slf.name=name
    def greet(sudhanshu):
        print(f"Hello {sudhanshu.name}")
p=Demo("Ayush")
p.greet()