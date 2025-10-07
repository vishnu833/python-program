part1="Data"
part2=" Science alhkfrketghhgiorahfglahroegihflhenuolihadfogul"
c=part1+part2
print(c)
l=len(c)
print(l)
sum=0
m=1
sub=0
while (l!=0):
    x=l%10
    sum=sum+x
    sub=sub-x
    m=m*x
    l=l//10
print(sum)    
print(m)
print(sub)
