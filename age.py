current_year=int(input("enter the currnt year"))
birth_year=int(input("enter the birth year"))
age=current_year-birth_year
if birth_year-current_year:
    print(age,"is your age")
else:
    print("it is not your age")
