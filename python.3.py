n=int(input("Enter a number"))
a=0
b=1
for i in range(3,n+1):
    c=a+b
    a=b
    b=c

print(c)
