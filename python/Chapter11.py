# # Inheritance
# class Employee:
#     company="ITC"
#     language="Python"
#     name="Sudhanshu"
#     salary=125422
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

# # class Programmer:
# #     company="ITC Infotech"
# #     name="Ayush"
# #     salary=121732
# #     def show(self):
# #         print(f"The name is {self.name} and the salary is {self.salary}")
    
# #     def showLanguage(self):
# #         print(f"The name is {self.name} and he is good with {self.language} language")
    
# class Programmer(Employee):
#     company="ITC Infotech"
#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.language} language")
    
# a= Employee()
# b=Programmer()
# b.show()
# b.showLanguage()



# # Multiple Inheritance

# class Employee: # Parent 1
#     company="ITC"
#     name="Sudhanshu"
#     salary=1200000
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

# class coder: # Parent 2
#     language="python"
#     def printLanguages(self):
#         print(f"Out of all the language here is your language: {self.language}")

# class Programmer(Employee,coder): # Child
#     company="ITC Infotech"
#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.language} language")
    
# a= Employee()
# b=Programmer()
# b.show()
# b.printLanguages()
# b.showLanguage()


# # Multilevel Inheritance
# class Employee:
#     a=2

# class Programmer(Employee):
#     b=3

# class Manager(Programmer):
#     c=4

# o=Employee()
# print(o.a)

# o=Programmer()
# print(o.a,o.b)

# o=Manager()
# print(o.a,o.b,o.c)


# # Super() Method
# class Employee:
#     def __init__(self):
#         print("Constructor of Employee")
#     a=2

# class Programmer(Employee):
#     def __init__(self):
#         # super().__init__()
#         print("Constructor of Programmer")
#     b=3

# class Manager(Programmer):
#     def __init__(self):
#         print("Constructor of Manager")
#         super().__init__()
#     c=4

# # o=Employee()
# # print(o.a)

# # o=Programmer()
# # print(o.a,o.b)

# o=Manager()
# print(o.a,o.b,o.c)


# # Class method
# class Employee:
#     a=2
#     @classmethod
#     def show(cls):
#         print(f"The class value of a is {cls.a}")
# e=Employee()
# e.a=45
# e.show()


# # Property Method
# class Employee:
#     @property
#     def name(self):
#         return f"{self.fname} {self.lname}"
    
#     @name.setter
#     def name(self,value):
#         self.fname=value.split(" ")[0]
#         self.lname=value.split(" ")[1]

# e=Employee()
# e.name="Sudhanshu Kumar"
# print(e.fname,e.lname)
# print(e.fname)
# print(e.lname)
# print(e.name)


# # Operator overloading in python
# class Number:
#     def __init__(self,n):
#         self.n=n

#     def __add__(self,num):
#         return self.n+num.n
    
# n=Number(1)
# m=Number(2)
# print(n+m)


# # PRACTICE SET
# # 1. Create a class (2-D vector) and use it to create another class representing a 3-D vector.
# class TwoDVector():
#     def __init__(self,i,j):
#         self.i=i
#         self.j=j
    
#     def show(self):
#         print(f"The vector is {self.i}i {self.j}j")

# class ThreeDVector(TwoDVector):
#     def __init__(self,i,j,k):
#         super().__init__(i,j)
#         self.k=k

#     def show(self):
#         print(f"The vector is {self.i}i {self.j}j {self.k}k")

# a=TwoDVector(1,2)
# a.show()
# b=ThreeDVector(1,2,3)
# b.show()


# # 2. Create a class 'Pets' from a class 'Animals' and further create a class 'Dog' from 'Pets'. Add a method 'bark' to class 'Dog'.
# class Animal:
#         pass

# class Pets(Animal):
#         pass

# class Dog(Pets):
#     @staticmethod
#     def bark():
#         print("Bow Bow!")

# d=Dog()
# d.bark()


# # 3. a) Create a class 'Employee' and add salary and increment properties to it.
# class Employee:
#     salary=240000
#     increment=20

# e=Employee()


# # 3. b) Write a method 'salaryAfterIncrement' method with a @property decorator with a setter which changes the value of increment based on the salary.
# class Employee:
#     salary=150
#     increment=20
#     @property
#     def salaryAfterIncrement(self):
#         return (self.salary + self.salary * (self.increment/100))
#     @salaryAfterIncrement.setter
#     def salaryAfterIncrement(self, salary):
#         self.increment=((salary/self.salary)-1)*100
        
# e=Employee()
# e.salaryAfterIncrement=200
# print(e.increment)



# # 4. Write a class 'Complex' to represent complex numbers, along with overloaded operators '+' and '*' which adds and multiplies them.
# class Complex:
#     def __init__(self,r,i):
#         self.r=r
#         self.i=i
#     def __add__(self,c2):
#         return Complex(self.r+c2.r, self.i+c2.i)
    
#     def __mul__(self,c2):
#         real_part=self.r * c2.r - self.i * c2.i
#         img_part=self.r * c2.r + self.i * c2.r
#         return Complex(real_part,img_part)
    
#     def __str__(self):
#         return f"{self.r} + {self.i}i"
# c1=Complex(1,2)
# c2=Complex(3,4)
# print(c1+c2)
# print(c1*c2)


# # 5. Write a class vector representing a vector of n dimensions. Overload the + and * operator which calculates the sum and the dot(.) product of them.
# class Vector:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#     def __add__(self, other):
#         result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
#         return result
#     def __mul__(self, other):
#         result = self.x * other.x + self.y * other.y + self.z * other.z
#         return result
#     def __str__(self):
#         return f"Vector({self.x}, {self.y}, {self.z})"
# # Test the implementation
# v1 = Vector(1, 2, 3)
# v2 = Vector(4, 5, 6)
# v3 = Vector(7, 8, 9) # Same dimension vector
# print(v1 + v2) # Output: Vector (5, 7, 9)
# print(v1 * v2) # Output: 32
# print(v1 + v3) # Output: Vector(8, 10, 12)
# print(v1 * v3) # Output: 50


# # 6. Write_str_() method to print the vector as follows: 7i + 8j + 10k
# class Vector:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#     def __add__(self, other):
#         result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
#         return result
#     def __mul__(self, other):
#         result = self.x * other.x + self.y * other.y + self.z * other.z
#         return result
#     def __str__(self):
#         return f"{self.x}i {self.y}j {self.z}k"
    
# # Test the implementation
# v1 = Vector(1, 2, 3)
# v2 = Vector(4, 5, 6)
# v3 = Vector(7, 8, 9) # Same dimension vector
# print(v1 + v2) # Output: 5i 7j 9k
# print(v1 * v2) # Output: 32
# print(v1 + v3) # Output: 8i 10j 12k
# print(v1 * v3) # Output: 50


# # 7. Override the __len__() method on vector of problem 5 to display the dimension of the vector.
# class Vector:
#     def __init__(self, l):
#         self.l= l

#     def __len__(self):
#         return len(self.l)

# # Test the implementation
# v1 = Vector([1, 2, 3])
# print(len(v1))

