

# The factorial reccursion #

b=int(input("enter the number:"))
print(f"The factorial of the number {b}:")
fact=1
for i in range(b):
    i+=1
    fact=fact*i
print("The factorial of given number : ",fact)