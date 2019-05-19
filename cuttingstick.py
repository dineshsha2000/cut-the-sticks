n=int(input())
a=list(map(int,input().split()))
b=[]
r=[]
r.append(len(a))
for i in a:
    b.append(i)


for i in range(n):
    c=0
    if(i==0):
        m=min(a)
     
    for j in range(len(a)):
        a[j]=a[j]-m
        v=[]
    for i in a:
        v.append(i)
    a=[]
    for i in v:
        if(i>0):
            a.append(i)
    if(len(a)!=0):
       m=min(a)
       z=len(a)
       r.append(z)
      

for i in r:
    print(i)




"""for i in a:
            v.append(i)
        a=[]
        for k in v:
            if(k>0):
               a.append(k)
               c=len(a)
               r.append(c)
        
print(r)   
"""         

