# Print the multiplication table for a given number (up to 10).
n=int(input("enter the number you want to print table:"))
print("table of",n)
for i in range(1,11):
    table=i*n
    print(n,"x",i,"=",table)
