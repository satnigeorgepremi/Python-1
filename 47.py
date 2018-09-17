a=int(input("enter the no"))
b=[]
if(a<=10000):
    for i in range(0,a):
        c=int(input("enter no"))
        b.append(c)
print(min(b),max(b))
