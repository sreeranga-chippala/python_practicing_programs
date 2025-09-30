a = int(input("enter the first number:"))
b = int(input("enter the second number:"))
option = input("enter the correct option:")

add = a+b
sub=a-b
product=a*b
division=a/b

if option == "add":
   print("result:", add)
elif option == "sub":
    print("result:",sub)
elif option == "product":
    print("result:",product)
elif option == "division":
    if b==0:
        print("division is not possible")
    else:
        print("result:",division)
else:
    print("choose any options like : \n add,sub,product and division")


