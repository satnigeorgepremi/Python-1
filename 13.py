a=int(input("enter the no"))
if a > 1:

    for i in range(2, a):
        if (a % i) == 0:
            print(a, "is not a prime number")
            print(i, "times", a// i, "is", a)
            break
    else:
        print("yes")
else:
    print(a, "is not a prime number")
