n=int(input("Enter a number"))
p=n
s=0
while(n>0):
    x=n%10
    s=s+x**3
    n=n//10
if (s==p):
    print("Entered number is armstrong")
else :
    print("Entered number is not armstrong")
       
