#Lcm of three numbers
a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=int(input("Enter third number"))
if (a>b and a>c):
    lcm=a
elif (b>c and b>a):
    lcm=b
else :
    lcm=c
while True:
    if (lcm%a==0 and lcm%b==0 and  lcm%c==0):
        break
   lcm +=1print(lcm)

    
     
