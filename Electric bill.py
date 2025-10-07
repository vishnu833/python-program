a=int(input("Enter starting meter reading:"))
b=int(input("Enter ending meter reading:"))
units=b-a
print("no of units consumed=",units)
if(units>=200 and units<500):
    bill=units*3.50
    print("Electric bill=",bill)
elif(units>=100 and units<200):
    bill=units*2.50
    print("Electric bill=",bill)
elif(units<100):
    bill=units*1.50
    print("Electric bill=",bill)    
