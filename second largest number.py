a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
c=int(input("enter 3rd number"))
if a>b and a>c:
    print(a,"is second largest number")
    if b>c:
        print(b,"is largest number ")
    else:
        print(c,"is largest number")
elif b>a and b<c:
    print(b,"is second larget number")
    if c>a:
        print(c,"is largest number")
    else:
        print(a,"is largest number")
elif c>a and c<b:
    print(c,"is second largest number")
    if a>b:
        print(b,"is largest number")
    else:
        print(a,"is larget number")
else:
    print("error")