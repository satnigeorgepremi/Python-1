a=int(input("enter the no"))
if(a<1000):
    for i in range(2,a+1):
        if(a%i==0):
            if(i%2==0):
                print(i)