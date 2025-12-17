#Return the number of perfect square numbers between low and high (inclusive).
import math
low = 1
high = 10
start = math.ceil(math.sqrt(low))
end = math.floor(math.sqrt(high))
if end >= start:
    count = end - start + 1
else:
    count = 0

print(count)

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

#Job Assignment – Maximum Profit
#Given arrays difficulty, profit, and worker, return the maximum profit each worker can earn.
# Maximum profit assignment
difficulty = [2, 4, 6, 8, 10]
profit = [10, 20, 30, 40, 50]
worker = [4, 5, 6, 7]
jobs = sorted(zip(difficulty, profit))
max_profit = 0
res = 0
j = 0
for w in sorted(worker):
    while j < len(jobs) and jobs[j][0] <= w:
        max_profit = max(max_profit, jobs[j][1])
        j += 1
    res += max_profit
print(res)

#Print one repeated number in a list.
# Find one repeated element
L = [1, 3, 4, 2, 2]
seen = set()
for x in L:
    if x in seen:
        print(x)
        break
    seen.add(x)

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
#from 7


