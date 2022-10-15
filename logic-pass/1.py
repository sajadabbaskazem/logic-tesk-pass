from os import remove


x=input('enter the required word :')
x=list(x)
y=input('enter the charecter you want to remove :')
i=0
while(i<len(x)):
    if (y==x[i]):
        x[i]=''
    i+=1
print(str(x))