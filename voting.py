age=int(input("enter your age :  "))
if age >= 18:
    print("eligible for voting")
elif age < 18 and age > 0:
    print("not eligible")
else:
    print("not eligible or enter correct age value")