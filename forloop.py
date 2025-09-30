a=int(input("enter the number:"))

for i in range(1,11):
    the=a*i
    print(f"{a}*{i}={the}\n")

# The factorial reccursion #

b=int(input("enter the number:"))
print(f"The factorial of the number {b}:")
fact=1
for i in range(b):
    i+=1
    fact=fact*i
print(fact)