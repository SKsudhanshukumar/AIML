# # FILE INPUT/OUTPUT

# # Opening a file in read mode
# f=open("file.txt","r")

# # reading its context
# data=f.read()

# # print its contexts
# print(data)

# # close the file
# f.close()


# # Writing in a file
# st= "Hey Sudhanshu you are amazing"
# f=open("myfile.txt", "w")
# f.write(st)
# f.close()


# # Reading a lines in from file
f=open("file.txt")

# # Reads all lines as type lists
# lines=f.readlines()
# print(lines,type(lines))

# # Reads every lines one by one as string
# line1=f.readline()
# print(line1,type(line1))
# line2=f.readline()
# print(line2,type(line2))
# line3=f.readline()
# print(line3,type(line3))
# line4=f.readline()
# print(line4,type(line4))
# f.close()
for i in f:
    line=f.readline()
    if(line != " "):
        print(line)
    else:
        break


# # Write at the end of a file
# st="\nHey this is appended text"
# f=open("myfile.txt","a")
# f.write(st)
# f.close()


# # With statement (automatically close the file)
# with open("myfile.txt","r") as f:
#     text=f.read()
# print(text)


# # 1. Write a program to read the text from a given file 'poems.txt and find out whether it contains the word 'twinkle'.
# with open("file.txt","r") as f:
#     text=f.read()
#     if("Twinkle" in text):
#         print("It contain twinkle")
#     else:
#         print("Not present")


# # 2. The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file 'Hi-score.txt' which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.
# import random
# def game():
#     print("You are playing the game..")
#     score=random.randint(1,62)
#     with open("hiscore.txt","r") as f:
#         hiscore=f.read()
#         if(hiscore!=""):
#             hiscore=int(hiscore)
#         else:
#             hiscore=0
#     print(f"Your score: {score}")
#     if(score>hiscore):
#         with open("hiscore.txt","w") as f:
#             f.write(str(score))
#     return score

# game()


# # 3. Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13 year old.
# def gen_table(n):
#     table=""
#     for i in range(1,11):
#         table+=(f"{n} X {i} = {i*n}\n")
    
#     with open(f"tables/table{n}.txt","w") as f:
#         f.write(table)
        
# for i in range(2,21):
#     gen_table(i)


# # 4. A file contains a word "Donkey" multiple times. You need to write a program which replace this word with ##### by updating the same file.
# def rewrite():
#     with open("file.txt","r") as f:
#         text=f.read()
#     newtext=text.replace("Donkey","#####")

#     with open("file.txt","w") as f:
#         f.write(newtext)
# rewrite()


# # 5. Repeat program 4 for a list of such words to be censored.
# def rewrite():
#     words=["Donkey", "Monkey", "Lion", "Tiger"]
#     with open("file.txt","r") as f:
#         text=f.read()
#     for i in words:
#         text=text.replace(i,"#####")

#     with open("file.txt","w") as f:
#         f.write(text)
# rewrite()


# # 6. Write a program to mine a log file and find out whether it contains 'python'.
# def mine():
#     words="python"
#     with open("log.txt","r") as f:
#         text=f.read()
#         if(words in text):
#             print("Python is in log file")
#         else:
#             print("Not in log file")
# mine()


# # 7. Write a program to find out the line number where python is present from ques 6.

# def mine():
#     words="python"
#     with open("log.txt","r") as f:
#         lines=f.readlines()
#     lineNo=1
#     for line in lines:
#         if(words in line):
#             print(f"Python is in log file. At line No.{lineNo}")
#             break
#         lineNo+=1
#     else:
#         print("Not in log file")

# mine()


# # 8. Write a program to make a copy of a text file "this.txt"
# def fileCopy():
#     with open("myfile.txt","r") as f:
#         content=f.read()
#     with open("Copyed_myfile.txt","w") as f:
#         f.write(content)
# fileCopy()


# # 9. Write a program to find out whether a file is identical & matches the content of another file.
# def fileIdential():
#     with open("myfile.txt","r") as f:
#         context1=f.read()
#     with open("Copyed_myfile.txt","r") as f:
#         context2=f.read()
#     if(context1 == context2):
#         print("File is idential")
#     else:
#         print("File is not idential")
# fileIdential()
    

# # 10. Write a program to wipe out the content of a file using python.
# with open("Copyed_myfile.txt", "w") as f:
#     f.write("")


# # 11. Write a python program to rename a file to "rename_by_python.txt".
# import os

# old_name = "old_file.txt"
# new_name = "rename_by_python.txt"
# os.rename(old_name, new_name)
# print("File renamed successfully")
