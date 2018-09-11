c=int(input("k"))
d=int(input("d"))

for i in range(c,d+1):
    order = len(str(i))
    k=i
    g=0
    while(k>0):
        b=k%10
        k=k//10
        g+=(b**order)

    if(i==g):
        print(i)

