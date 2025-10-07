n=int(input("Enter a number"))
i=3
res=0
while (i!=0):
    r=n%2
    res=res+r*(10**i)
    i=i-1
print(res)    
