#Write a program that calculates the area of a rectangle given its length and width.
l=float(input("enter the lenght of rectangle:"))
b=float(input("enter the breath of rectangle:"))
print("the area of rectangle is:",l*b)
#write the program to calculate the area of circle
r=float(input("enter the radius of circle:"))
area=22/7*r**2
print("the area of circle is:",area)
#write a program to calculate the simple interest
p=float(input("enter the principle amount:"))
rate=float(input("enter the rate:"))
t=float(input("enter the time in years:"))
si=(p*rate*t)/100
print("the intrest amount is:",si)
print("the total amount including interest is:",si+p) 