'''
nums = input("Enter the array of numbers: ").split()
nums = [int(num) for num in nums]

tol_e=0
tol_o=0
char=input("Enter the valid character to perform operations:")
if char=='-1':
    for num in nums:
        if num%2==0:
            tol_e=tol_e+num
        else:
            tol_o=tol_o+num
    print(len(nums),"is the count")
    print(tol_e,"is the even numbers sum")
    print(tol_o,"is the odd numbers sum")
else:
    print("enter the valid character(-1)")'''

'''rows=9
cols=5
i=0
j=0
for i in range(rows+1):  
        stars=cols-abs(cols-i)
        for j in range(stars):
            print("*",end=" ")
        print()
'''
'''n=int(input("enter the no.of rows:"))
for i in range(1,n+1):
    for j in range(1,2*i):
        print(1+abs(i-j),end=" ")
    print()'''
'''n=input("enter the number:")
length=len(n)
for i in range (length):
    row = n[i:]
    print(row.center(length))'''
'''n = int(input("enter the rows:"))  # or n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
'''
