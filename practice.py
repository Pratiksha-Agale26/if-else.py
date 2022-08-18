# alpha,dighit,special chr.......

# a=(input("enter the anything"))
# if a>="a" and a<="z" or a>="A" and "z":
#     print(a,"is a alphabet")
# elif a>="0" and a<="9":
#     print(a,"it is a number")
# else:
#     print(a,"is a special charecter")

# n=(input("enter the alphbet"))
# if n>="a" and n<="z":
#     print(n,"it is alphabet")
# else:
#     print(n,"it is not alphabet")

# a=(input("enter the alphabet"))
# if a=="a" or a=="e" or a=="i" or a=="o" or a=="u":
#     print("vowel")
# else:
#     print("consonent")

# a=int(input("enter the number"))
# b=int(input("enter the number"))
# c=int(input("enter the number"))
# total=a+b+c
# if total==180:
#     print("in this valid triangle")
# else:
#     print("in this is not not triangale")

# a=int(input("enter the number"))
# b=int(input("enter the number"))
# c=int(input("enter the number"))
# d=(a+b+c)/3
# if a+b+c:
#     print(d,"average")
# else:
#     print("false")

# num=int(input("enter the number"))
# if num%2==0:
#     print("divisible by 2")
# else:
#     print("not")

# a=int(input("enter the number"))
# if a%2==0:
#     print(a,"even")
# else:
#     print(a,"odd")

# a=int(input("enter the number"))
# if a%2==0 and a>10:
#     print("number is even and greater than 10")
# elif a%2==0 and a<10:
#     print("number is even and smaller than 10")
# else:
#     print("number is odd")

# a=int(input("enter the number"))
# if a>=1320:
#     print("greater than or equal")
# else:
#     print("lesser")

# a=int(input("enter the actual word"))
# b=int(input("enter the guess word"))
# if a==b:
#     print(len(a)*2)
# else:
#     print("0")

# a=int(input("enter the number"))
# b=int(input("enter the number"))
# c=int(input("enter the number"))
# if a>b and a>c:
#     print("max num",a)
# elif b>c and b>a:
#     print("max num",b)
# elif c>a and c>b:
#     print("max num",c)
# else:
#     print("not max num")

# num=int(input("enter the number"))
# if num%10:
#     print(num%10)
# else:
#     print("error")

# year=int(input("enter the number"))
# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             print(year,"is a leap year")
#         else:
#             print(year,"is not leap year")
#     else:
#         print(year,"is not leap year")
# else:
#     print(year,"is not leap year")

# a=int(input("enter the number"))
# b=int(input("enter the number"))
# if a>b:
#     print("max number",a)
# else:
#     print("max number",b)

# date=int(input("enter the day"))
# month=int(input("enter the month"))
# year=int(input("enter the year"))
# if date!=31 and date!=29:
#     print(date+1,"/",month,"/",year)
# elif date==29 and month==2:
#     print("1","/","1","/",year+1)
# elif date==31 and month==12:
#     print("1","/","1","/",year+1)
# else:
#     print("invalid")

# a=int(input("enter the number"))
# i=1
# while i<=10:
#     print(a*i,"=",a*i)
#     i+=1

# a=int(input("enter the number"))
# if a<=10:
#     print(a*1)
#     print(a*2)
#     print(a*3)
#     print(a*4)
#     print(a*5)
#     print(a*6)
#     print(a*7)
#     print(a*8)
#     print(a*9)
#     print(a*10)

# a="pratiksha"
# b=12
# c="14.5"
# d=1+2j



# a="divya"
# b="12.5"
# c=21
# d="shivani"
# e=float(b)
# f=int(e)
# h=f+c
# g=str(h)
# print(a+d+g)




# a="pratiksha"
# b=12
# c="14.5"
# d=1+2j
# f=float(c)
# g=int(f)
# h=complex(d)
# # i=(int(h))
# j=g+h+b
# k=str(j)
# print(a+k)

# a="3+5j"
# b="21.4"
# c="sejal"
# # d="14.5" 
# e=float(b)
# f=int(e)
# g=e+b
# print(g)

# a=8//4//(3//2)%9
# print(a)

# a=(8/4/2,8/(4/2))
# print(a)

# a=(24//6%3,24//4//2)
# print(a)

# a=(2**(3**2),(2**3)**2,2**3**3)
# print(a)


# if True:
#     if True:
#         print("kranti")
#     if not(10==5):
#         print("good")
#     else:
#         print("no")
# if True:
#     print("have anice day")
#     if False:
#         print("good morning")
#     if 10 is 5:
#         print("happy")
#     elif not(10<20) and not (10>30):
#         print("priti")
#     else:
#         print("sunday")
# else:
#     if True:
#         print("world")
#     else:
#         print("nice")


# d1={"a":23,"b":45}
# d2={"c":54,"d":67}
# s={}
# for i in d1:
#     for i in d2:
#         s.update(d1)
#         s.update(d2)
# print(s)

# for i in range(11,1):
#     while i>=100:
#         print(i,end=" ")
#         i=i-1
#     print()

# a=[1,2,3,4,5,6]
# i=1
# b=[]
# while i<len(a):
#     b.append(a[i])
#     b.append(a[i-1])
#     i+=2
# print(b)

a="my name is pratiksha"
i=0
b=[]
c=""   
while i<len(a):
    if a[i]==" ":
        b.append(c)
        c=""
    else:
        c=c+a[i]
    i+=1
b.append(c)
print(b)
