from itertools import permutations
a=int(input("a"))
b=int(input("b"))
c=int(input("c"))
perm = permutations([a, b, c])
for i in list(perm):
    print(i)