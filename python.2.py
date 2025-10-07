n=int(input("Enter a number(in binary form)"))
i=0
res=0
while (n!=0):
    x=n%10
    res=res+x*(2**i)
    i=i+1
    n=n//10

print(res)   
    
