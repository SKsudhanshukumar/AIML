# # Print the sub string from string 

# name= "Sudhanshu"
# nameshort=name[4:9]
# print(nameshort)
# print(name[-4:-1])
# print(name[:4])
# print(name[2:])
# print(name[1:7])

# # Print the sub string with a skip of value

# print(name[1:6:2])
# print(name[1::2])
# print(len(name))
# print(name.endswith("shu"))
# print(name.startswith("Su"))
# print(name.capitalize())
# print(name.count("u"))
# print(name.find("s"))

# # PRACTICE SET

# # 1. Write a python program to display a user entered name followed by Good Afternoon using input function.
# a= input("Enter name: ")
# print(f"Good Afternoon {a}")

# # 2. Write a program to fill in a letter template given below with name and date.
# letter='''
#         Dear <|Name|>,
#         You are selected!
#         <|Date|>'''
# print(letter.replace("<|Name|>","Sudhanshu").replace("<|Date|>","24 December 2025"))

# # 3.  Write a program to detect double space in a string.
# name="I am a  good  boy"
# print(name.find("  "))
# print(name)

# # 4. Replace the double space from problem 3 with single spaces.
# name="I am a  good  boy"
# print(name.replace("  "," ")) # it will create new string original string won't change

# # 5. Write a program to format the following letter using escape sequence characters.
# Letter ="Dear Sudhanshu,\n \tThis python course is nice.\nThanks!"
# print(Letter)