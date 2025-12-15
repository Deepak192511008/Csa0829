n=int(input("Enter a Year:"))
if (n%4==0 and n%100!=0) or n%400==0:
    print("The given year is a leap year")
else:
    print("The given year is not a leap year")
