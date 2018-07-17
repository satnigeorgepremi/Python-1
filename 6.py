a=int(input("year"))
if a%4==0 and a%400==0 and a%100==0:
    print("leap lear")
else:
    print("not leap year")