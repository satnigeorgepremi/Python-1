b=1
c=1
g=0

a=int(input("a"))
c=a
while(a>0):
    b=a%10
    a=a//10
    g+=(b**3)

if(c==g):
    print('yes')
else:
    print('no')
print(a)
