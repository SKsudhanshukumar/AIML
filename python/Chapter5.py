# # DICTIONARY
# a={"key":"value",
#    "Marks":100,
#    "Name":"Sudhanshu",
#    "list":[1,2,4]}
# print(a)
# print(type(a))
# print(a["Name"])

# # METHODS
# marks={
#     "Sudhanshu":100,
#     "Ayush":85,
#     "Rohan":89,
# }

# print(marks.items())
# print(marks.keys())
# marks.update({"Ayush":81})
# print(marks)
# print(marks.get("Ayush")) # returns none
# # print(marks.get["Ayush"]) # gives error



# # SETS
# s={1,3,45,65,6,4,5,6,6}
# print(len(s)) # 7
# s.remove(3) 
# print(s) # {65, 1, 4, 5, 6, 45}
# print(s.pop()) # 65
# print(s.union({2,7,8})) # {1, 2, 4, 5, 6, 7, 8, 45}
# print(s.intersection({4,45,678})) # {4, 45}
# print(s.clear()) #none
# s.add(3)
# print(s)


# # PRACTICE SET
# # 1. Write a program to create a dictionary of hindi words with values as the english translation. Provide user with an option to look it up!
# words={
#     "kutta":"Dog",
#     "billi":"cat",
#     "bandar":"monkey"
#        }
# word=input("enter the word you want meaning of: ")
# print(words[word])

# # 2. Write a program to input eight numbers from the user and display all the unique numbers(once).
# a=set()
# for i in range(1,9):
#     n=int(input(f'''Enter number {i}: '''))
#     a.add(n)
# print(a)


# # 3. Can we have a set with 18 (int) and '18' (str) as a value in it?
# s=set()
# s.add(18)
# s.add("18")
# print(s)

# # 4. What will be the length of folling set s:
# s=set()
# s.add(20)
# s.add(20.0)
# s.add('20')
# print(len(s)) #python consider the float and integer as same value (1==1.0 will true)

# # 5. s={} what is the type of 's'?
# s={}
# print(type(s)) #Dictionary

# # 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.
# dict={}
# for i in range(0,4):
#     name=input("enter name: ")
#     lang=input("enter language: ")
#     dict.update({name:lang})
# print(dict)

# # 7. If the name of 2 friends are same; What will happen to program in problem 6?
# # The key value will be updated and it will be consider as a same variable
# dict={}
# for i in range(0,4):
#     name=input("enter name: ")
#     lang=input("enter language: ")
#     dict.update({name:lang})
# print(dict)

# # 8. If the language of 2 friends are same; What will happen to program in problem 6?
# # No effect to the keys
# dict={}
# for i in range(0,4):
#     name=input("enter name: ")
#     lang=input("enter language: ")
#     dict.update({name:lang})
# print(dict)

# # 9. Can you change the values inside a list which is contained in set S?
# s={8, 7, 12, "Harry", [1,2]}
# Cannot change value inside a list contained inside a set
# We can not have list inside a set because sets in python require all their element to be immutable and hashable. Lists are mutable and not hashable, so they cannot be add to a set
# Traceback (most recent call last):
#     s={8, 7, 12, "Harry", [1,2]}
#       ^^^^^^^^^^^^^^^^^^^^^^^^^^
# TypeError: unhashable type: 'list'