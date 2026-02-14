#Write a program to find the sum of the first n natural numbers.
n=int(input("enter the number:"))
sum=0
for i in range(1,n+1):
    sum+=i
    print(i)
print(sum)