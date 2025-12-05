marks=int(input("Enter the marks:"))
if 90 <= marks <= 100:
    print("Grade: A")
elif 80 <= marks <= 89:
    print("Grade: B")
elif 70 <= marks <= 79:
    print("Grade: C")
elif 60 <= marks <= 69:
    print("Grade: D")
elif marks <= 60:
    print("Grade: F")
else:
    print("Invalid Marks")
