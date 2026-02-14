n=int(input("choose how many times you wants to play"))
for i in range(1,n+1):
    a=int(input("enter the number between 1-10"))
    print(a)
    import random
    f=random.randint(1,10)
    print("the actual number is",f)
    if (a==f):
        print("the number is equal and you win")
        break
    elif (a>f):
        print("the number you gusse is greater and you lose")
    else:
        print("the number you gusse is lower and you lose")