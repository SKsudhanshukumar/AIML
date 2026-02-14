#Calculate the sum of the first 10 even numbers.
n=int(input("enter the number"))
sum=0
for i in range(1,2*(n+1)):
    if (i%2==0):
        sum=sum+i
        print(sum)
print(sum)