year=int(input("enter the number"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(year,"is a leap year")
        else:
            print(year,"not leap year")
    else:
        print(year,"not leap year")
else:
    print("not leap year")