#Magic number  
num = input("Enter a number: ")

while len(num) > 1:
    s = 0
    for i in num:
        s += int(i)
    num = str(s)

if num == "1":
    print("Magic Number")
else:
    print("Not a Magic Number")
