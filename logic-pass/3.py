x=input('entar your string :')
y=len(x)
z=[]
i=0
while(i<y):
    z.append(x[i])
    count=x.count(x[i])
    print(count,z)
    z=[]     
    i+=1
