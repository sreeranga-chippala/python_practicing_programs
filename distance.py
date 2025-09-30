#The distance program#


x1=float(input("enter the co-ordinate x1:"))
x2=float(input("enter the co-ordinate x2:"))
y1=float(input("enter the co-ordinate y1:"))
y2=float(input("enter the co-ordinate y2:"))
distance=((x2-x1)**2 + (y2-y1)**2)**(1/2)
print(f"distance is {distance}")


#The Ascii value code#


char=input("enter the character:")
print(f"The ASCII value of the \"{char}\" :",ord(char))