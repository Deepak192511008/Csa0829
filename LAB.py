#Write a Python program to find the union of two sets.
l={1,2,3,4}
ln={4,5,6}
ul=l.union(ln)
print(ul)

#Write a Python program to sort a list in descending order
l=[3,5,7,1,4,2]
print(sorted(l,reverse=True))

#Write a Python program to remove all occurrences of a specified element from a list.
lst = [1, 2, 3, 2, 4, 2, 5,3]
value = 2
result = []
for i in lst:
    if i != value:
        result.append(i)
print("Original list:", lst)
print("After removing", value, ":", result)

#27. Write a Python program to find the intersection of two sets.
l={1,2,3,4}
ln={4,5,6}
ul=l.intersection(ln)
print(ul)

# Write a Python program to print the multiplication table of a given number.
n=5
for i in range (1,11):
  print(i,"*",n,"=",i*n)

#19. Write a Python program to find the factorial of a number using a loop.
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial of", num, "is", fact)

#Write a Python program to find the sum of digits in a number
n = int(input("Enter a number: "))
s = 0
while n > 0:
    d = n % 10      
    s += d
    n //= 10            

print("Sum of digits:", s)


n = int(input("Enter a number: "))
s=str(n)
su=0
for i in s:
  d=int(i)
  su+=d
print(su)

# Write a Python program to check if a number is a palindrome or not.
n=121
s=str(n)
sr=s[::-1]
if s==sr:
  print("pal")
else:
  print("not pal")

#Write a Python program to find the sum of the first N natural numbers.
n=int(input("enter number "))
s=0
for i in range (0,n+1):
  s+=i
print(s)

#Write a Python program to find the LCM of two numbers
a = int(input("Enter first number: "))
ac=a
b = int(input("Enter second number: "))
bc=b
while b != 0:
    a, b = b, a % b
g=a
l=(ac*bc)/g
print("lcm= ",l)

#Write a Python program to find the second largest element in a list.
l=[15,4,2,20,23]
l2=[]
m=max(l)
for i in l:
  if i not in l2:
    if i!=m:
      l2.append(i)
sm=max(l2)
print("second max= ",sm)

#Write a Python program to find the greatest common divisor (GCD) of two numbers.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
while b != 0:
    a, b = b, a % b
print("GCD is:", a)


#Write a Python function to remove duplicate elements from a list.
l=[1,1,2,3,3,6,7,1]
nl=[]
for i in l:
  if i not in nl:
    nl.append(i)
print(nl)

#Write a Python program to find the maximum of two numbers using the ternary operator.
n1 = int(input("Enter the number: \n"))
n2 = int(input("Enter the number: \n"))
m = n1 if n1 > n2 else n2
print("The maximum is:",m)

#Write a Python program to find the greatest common divisor (GCD) of three numbers.
import math
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
gcd_ab = math.gcd(a, b)
gcd_abc = math.gcd(gcd_ab, c)
print("GCD of the three numbers is:", gcd_abc)

#GCD 3number
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
gcd=min(a,b,c)
while gcd>0:
  if a%gcd==0 and b%gcd==0 and c%gcd==0:
    break
  gcd-=1
print(gcd)

#gcd of 2 number
a=4
b=6
x,y=a,b
while b:
  a,b=b,a%b
g=a
print("gcd",g)

#LCM of 3 number 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
lcm=max(a,b,c)
while(lcm%a!=0 or lcm%b!=0 or lcm%c!=0 ):
  lcm+=1
print("LCM=",lcm)

#Write a Python program to find the LCM of two numbers using a while loop.
a=4
b=6
x,y=a,b
while b:
  a,b=b,a%b
g=a
print("lcm",x*y/g)
#with math
import math
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
lcm = math.lcm(num1, num2)
print("LCM of", num1, "and", num2, "is:", lcm)


#Write a Python program to check if a given number is a perfect square or not.
import math
n = int(input("Enter a number: "))
r=int(math.sqrt(n))
if r*r==n:
  print("Perfect square")
else:
  print("Not a perfect square")

#Write a Python program to find the largest prime number less than a given number.
n = int(input("Enter a number: "))
for num in range(n-1, 1, -1):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Largest prime less than", n, "is:", num)
        break
else:
    print("No prime number found")

#Write a Python program to find the first n Fibonacci numbers using a for loop.
#with function
def fib(n):
  if n==0 or n==1:
    return n
  else:
    return fib(n-1)+fib(n-2)
n=int(input("enter n\n"))
for i in range(n):
  print(fib(i))
 
print("\n")
#without function
n=int(input("enter number \n"))
a=0
b=1
for i in range(n):
  print(a)
  c=a+b
  a=b
  b=c

#Write a Python program to find the factorial of a number using a while loop.
n=int(input("enter "))
fact=1
while n>0:
  fact=n*fact
  n=n-1
print(fact)


#Write a Python program to find the sum of two numbers using a recursive function.
def sum(a, b):
    if b == 0:
        return a
    return sum(a + 1, b - 1)
num1 = 5
num2 = 3
result = sum(num1, num2)
print("Sum is:", result)

#Write a Python program to check if a given number is a perfect number using a user-defined function.
def is_perfect(num):
    if num <= 0:
        return False
    total = 0
    for i in range(1, num):
        if num % i == 0:
            total += i
    return total == num
number = int(input("Enter a number: "))
if is_perfect(number):
    print(number, "is a Perfect Number")
else:
    print(number, "is not a Perfect Number")

#Write a Python program to find the frequency of all characters in a given string.
s = input("Enter a string: ")
f = {}
for c in s:
    if c in f:
        f[c] += 1
    else:
        f[c] = 1
for c, n in f.items():
    print(f"{c}: {n}")


#Write a Python program to find the largest palindrome substring in a given string.
s = input("Enter a string: \n")
sl=s.split()
l=0
for i in sl:
  if i==i[::-1]:
    if len(i)>l:
      l=len(i)
for i in sl:
  if i==i[::-1] and len(i)==l:
    print(i)

#Write a Python program to find the second most frequent character in a given string.
s = "examplestring"
freq = {}
for c in s:
    freq[c] = freq.get(c, 0) + 1
sorted_chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)
print("Second most frequent character:", sorted_chars[1][0])

#Write a Python program to check if a given string is an anagram of another string.
str1=input("enter 0\n")
str2=input("enter 1\n")

st=sorted(str1)
st2=sorted(str2)
if st==st2:
  print("Ana")
else:
  print("no")

#Write a Python program to find the most frequent word in a given sentence.
s = input("Enter a sentence: ")
w = s.lower().split()
c = {}
for i in w:
    c[i] = c.get(i, 0) + 1
m = max(c, key=c.get)
print(m, "appears", c[m], "times")

#Write a Python program to find the largest subsequence sum in a given list of integers.
l=[[1,3],[8,9,7],[1]]
le=0
for i in range(len(l)):
  if len(l[i])>le:
    le=len(l[i])
for i in range (len(l)):
  if len(l[i])==le:
    print(sum(l[i]))

#Write a Python program to remove duplicates from a given list.
l = [1, 2, 2, 3, 4, 4, 5,4,4]
for i in l:
  if l.count(i)>1:
    for j in range(l.count(i)-1):
      l.remove(i)
print(l)
