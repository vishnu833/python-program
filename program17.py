n=int(input("Enter a number"))
for i in range(1,n,1):
    if(n%i!=0 and n%n==0 and n%1==0):
              print("prime number",n)
    else:
        print("composite number",n)
              

