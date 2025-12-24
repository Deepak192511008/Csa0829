# Count perfect squares between low and high
low = 1
high = 10
i = 1
count = 0
while i * i <= high:
    if i * i >= low:
        count += 1
    i += 1
print(count)
------------------------------------------------------------------------------------------------------------------------------------------------------------------

#You are climbing a staircase with n steps. Each time you can climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Number of ways to climb stairs (Fibonacci)
n = 5
if n <= 2:
    print(n)
else:
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    print(b)
------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Job Assignment – Maximum Profit
#Given arrays difficulty, profit, and worker, return the maximum profit each worker can earn.
# Maximum profit assignment
difficulty = [2, 4, 6, 8, 10]
profit = [10, 20, 30, 40, 50]
worker = [4, 5, 6, 7]
jobs = list(zip(difficulty, profit))
print(jobs)
total_profit = 0
for w in worker:                 # for each worker
    best = 0
    for d, p in jobs:            # check all jobs
        if d <= w:               # worker can do this job
            if p > best:
                best = p
    total_profit += best         # add best profit
print(total_profit)

------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Print one repeated number in a list.
# Find one repeated element
L = [1, 3, 4, 2, 2]
seen = set()
for x in L:
    if x in seen:
        print(x)
        break
    seen.add(x)
------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''Search in a Sorted 2D Matrix
Search a value in an m x n matrix where rows and columns are sorted.'''
# Search in 2D sorted matrix
matrix = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]
target = 5
found=False
for i in matrix:
  if target in i:
    found=True
    break
print(found)
------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Find the frequency of each element and display the element with the highest frequency.
l=[1,2,2,3,2,1,4,3]
d={}
for i in l:
    d[i]=l.count(i)
print(d)
m=(max(d.values()))
for i in d:
    if d[i]==m:
        print("number",i,"has occured maximum =",m)
------------------------------------------------------------------------------------------------------------------------------------------------------------------
     
'''First and Last Position of Target
Given a sorted array, find the starting and ending index of a target value.'''
nums = [5, 7, 7, 8, 8, 10]
target = 8

if target in nums:
    first = nums.index(target)
    last = len(nums) - 1 - nums[::-1].index(target)
else:
    first = last = -1
print([first, last])
------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''Rotated Sorted Array – Find Minimum
An array sorted in ascending order is rotated. Find the minimum element.'''
arr = eval(input("Enter array elements: "))
k = int(input("Enter rotation count: "))
k = k % len(arr)          
rotated = arr[k:] + arr[:k]
print("Rotated array:", rotated)
print("Minimum element:", min(rotated))
------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''Two Sum in Sorted Array (1-Indexed)
Find two numbers such that they add up to a target.'''

numbers = [2, 7, 11, 15]
target = 9
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print([i + 1, j + 1])  # 1-indexed
            break
    else:
        continue
    break
------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Matrix multiplication
import numpy as np
A = np.array([[1, 2],[3, 4]])
B = np.array([[5, 6],[7, 8]])
result =  A @ B
add = A + B
# Subtraction
sub = A - B
print("Addition:\n", add)
print("Subtraction:\n", sub)
print(result)

------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Sort and print middle element
arr = [90, -90, 80, 66, 18, 10]
arr.sort()

mid = len(arr) // 2
print(arr[mid])
------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Intersection of two arrays
nums1 = [1, 2, 2, 1]
nums2 = [2, 2,3]
res = []
for x in nums1:
    if x in nums2:
        res.append(x)
        nums2.remove(x)
print(res)
------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Check anagram
s1 = "listen"
s2 = "silent"

if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")
------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''Luck or Not (Sum = Product of digits)
If sum of digits = product of digits → Lucky number.'''
# Lucky number check
num = 1412

s = 0
p = 1

for d in str(num):
    s += int(d)
    p *= int(d)

if s == p:
    print("Yes")
else:
    print("No")
------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Function to find a peak element
def peak(arr):
    for i in range(1, len(arr)-1):
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            return arr[i]

arr = [1, 3, 20, 4, 1]
print(peak(arr))
------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Rotate array one time to the left.
arr = eval(input("Enter array elements: "))
k = int(input("Enter rotation count: "))
k = k % len(arr)          
rotated = arr[k:] + arr[:k]
print("Rotated array:", rotated)
------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Perfect square check
import math

n = 16
root = int(math.sqrt(n))

if root * root == n:
    print("Perfect Square")
else:
    print("Not a Perfect Square")
------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Frequency of characters using count()
s = "engineering"
a=set(s)
for ch in a:                 # set removes duplicates
    print(ch, "->", s.count(ch))  # count() gives frequency

------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''In daily share trading, a buyer buys shares in the morning and sells them on the same day. 
If the trader is allowed to make the most two transitions in a day, where the second transition
can only start after the first one is completed, gain stock price throughout the day, 
find out the maximum profit the share trader would have had.'''

prices = [10, 22, 5, 75, 65, 80]

buy1 = float('inf')
buy2 = float('inf')
profit1 = 0
profit2 = 0

for i in prices:
    buy1 = min(buy1, i)
    profit1 = max(profit1, i - buy1)
    
    buy2 = min(buy2, i - profit1)
    profit2 = max(profit2, i - buy2)
print("Maximum Profit:", profit2)
------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''Remove K Digits to Form Smallest Number
Given a string number, remove k digits to get the smallest possible number.'''
n = "1432219"
k = 3
l = list(n)
i = 0
while k > 0 and i < len(l) - 1:
    if l[i] > l[i + 1]:
        l.pop(i)
        k -= 1
        i = 0
    else:
        i += 1

while k > 0:
    l.pop()
    k -= 1

print("The smallest number is:")
for d in l:
    print(d, end="")

------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''Least Number of Perfect Squares (Sum = n)
Return the least number of perfect square numbers that sum to n'''
import math

n = int(input("Enter a number: "))

# use n+1 as a "big number" instead of float('inf')
dp = [0] + [n+1] * n

for i in range(1, n+1):
    for j in range(1, int(math.sqrt(i)) + 1):
        square = j * j
        dp[i] = min(dp[i], 1 + dp[i - square])

print("Least number of perfect squares =", dp[n])
------------------------------------------------------------------------------------------------------------------------------------------------------------------
