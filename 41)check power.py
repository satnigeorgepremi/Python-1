a=int(input("a"))
b=int(input("b"))
for i in  range(2,100000):
    if((b**i)==a):
        print("yes")
        break
    else:
        print("no")
        break