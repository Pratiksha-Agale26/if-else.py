a=int(input("enter the number"))
b=int(input("enter the number"))
if a>b:
    print(a,"is max")
else:
    print(b,"is max")

a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
if a>b and a>c:
    print(a,"a is max")
if b>a and b>c:
    print(b,"b is max")
if c>a and c>b:
    print(c,"c is max")

a=int(input("enter the number"))
if a>0:
    print("positive")
else:
    print("negative")

a=int(input("enter the number"))
if a%5==0 and a%11==0:
    print("divisible")
else:
    print("not divisible")

a=int(input("enter the number"))
if a%2==0:
    print("even")
else:
    print("odd")

a=int(input("enter the number"))
if a%4==0:
    if a%100==0:
        if a%400==0:
            print("leap year")
        else:
            print("leap year")
    else:
        print("leap year")
else:
    print("not leap")

a=int(input("enter the number"))
if a%2==0:
    if a%4==0:
        if a%8==0:
            print("divisible")
        else:
            print("dis")
    else:
        print("dis")
else:
    print("not dis")

a=int(input("enter the number"))
if a%2==0 and a%4==0 and a%8==0:
    print("divisible")
else:
    print("not")

a="Pratiksha123"
i=0
count=0
counter=0
num=0
while i<len(a):
    if a[i] >="A" and a[i]<="Z":
        count+=1
    if a[i]>="a" and a[i]<="z":
        counter+=1
    if a[i]>="0" and a[i]<="9":
        num+=1
    i+=1
print("upper",count)
print("lower",counter)
print("number",num)

a="Pratiksha"
i=0
count=0
while i<len(a):
    if a[i]>="A" and a[i]<="Z" or a[i]>="a" and a[i]<="z":
        count+=1
    i+=1
print("alpha",count)
    
a="@pratiksha$#"
i=0
count=0
while i<len(a):
    if a[i]=="@" or a[i]=="$" or a[i]=="#":
            count+=1
    i+=1
print("spl",count)

i=1
while i<=5:
    b=1
    while b<=i:
        print("*",end="*")
        b+=1
    print()
    i+=1