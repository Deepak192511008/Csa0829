# Additive sequence check
l = [1, 2, 3, 5, 8]
f = True
for i in range(len(l) - 2):
    if l[i] + l[i + 1] != l[i + 2]:
        f = False
        break
if f:
    print("Additive seq")
else:
    print("NA")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Find 3 numbers whose sum is equal to a given number

arr = [1, 2, 3, 4, 5, 6]
n = len(arr)
target = 10
found = False

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if arr[i] + arr[j] + arr[k] == target:
                print("Numbers are:", arr[i], arr[j], arr[k])
                found = True

if not found:
    print("No such numbers found")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#find the difference between the sum of sq of the 1st 200 N no and sq of sum
n = 200
sum_n = n * (n + 1) // 2
square_of_sum = sum_n ** 2
sum_of_squares = n * (n + 1) * (2 * n + 1) // 6
difference = square_of_sum - sum_of_squares
print("Difference =", difference)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#sum of rows , col and diagonal
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

n = len(matrix)

pd = 0
sd = 0

print("Row sum   Column sum")

for i in range(n):
    rs = 0
    cs = 0
    for j in range(n):
        rs += matrix[i][j]
        cs += matrix[j][i]

    pd += matrix[i][i]
    sd += matrix[i][n - i - 1]

    print("Row", i + 1, "=", rs, "   Col", i + 1, "=", cs)

print("\nPrimary diagonal sum =", pd)
print("Secondary diagonal sum =", sd)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#sum of muliple of 3or 5 below 500
s=0
for i in range(1,500):
    if i%3==0 or i%5==0:
        s+=i
print(s)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#sum of digits
n='123'
s=0
for i in n:
    s+=int(i)
print(s)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#GP or not
seq = [2, 6, 18, 54]

r = seq[1] / seq[0]
flag = True

for i in range(len(seq) - 1):
    if seq[i + 1] / seq[i] != r:
        flag = False
        break

if flag:
    print("GP")
else:
    print("Not a GP")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#replaces any negative element in a sorted (ascending) integer array with the average of the array
arr = [-5, -2, 1, 3, 7, 10]  # given ascending array

# Compute average
avg = sum(arr) / len(arr)

# Replace negative elements with average
for i in range(len(arr)):
    if arr[i] < 0:
        arr[i] = avg

print("Updated array:", arr)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''a program to find the maximum total from top to bottom of a number triangle'''
'''a program to find the maximum total from top to bottom of a number triangle'''
triangle = [
    [3],
    [7, 4],
    [2, 4, 6],
    [8, 5, 9, 3]
]

# Start from the second-last row and move upwards
for i in range(len(triangle) - 2, -1, -1):
    for j in range(len(triangle[i])):
        triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])

print("Maximum total from top to bottom:", triangle[0][0])
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#AP or not
seq = [2, 4, 6, 8, 10]  # Example sequence

d = seq[1] - seq[0]  # common difference
is_ap = True

for i in range(len(seq) - 1):
    if seq[i + 1] - seq[i] != d:
        is_ap = False
        break

if is_ap:
    print("AP")
else:
    print("Not an AP")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#matrix in spiral form
matrix = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12],
    [13,14, 15, 16]
]

top, bottom = 0, len(matrix)-1
left, right = 0, len(matrix[0])-1

while top <= bottom and left <= right:
    for i in range(left, right+1): print(matrix[top][i], end=" ")
    top += 1
    for i in range(top, bottom+1): print(matrix[i][right], end=" ")
    right -= 1
    if top <= bottom:
        for i in range(right, left-1, -1): print(matrix[bottom][i], end=" ")
        bottom -= 1
    if left <= right:
        for i in range(bottom, top-1, -1): print(matrix[i][left], end=" ")
        left += 1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def spiral(matrix):
    res = []                      # Stores elements in spiral order

    while matrix:                 # Continue until matrix becomes empty
        res += matrix.pop(0)      # 1️⃣ Remove and add the top row to result

        # 2️⃣ Rotate the remaining matrix 90° counter-clockwise
        # *matrix       → unpacks rows for zip
        # zip(*matrix)  → transposes (rows → columns)
        # list(...)     → converts tuples to list
        # [::-1]        → reverses rows to complete rotation
        matrix = list(zip(*matrix))[::-1]

    return res                    # Final spiral order result


print(spiral([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]))
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def spiral(matrix):
    res = []
    m=[]
    while matrix:
        res += matrix.pop(0)
        matrix = list(zip(*matrix))[::-1]
        #print(res)
        #print(matrix)
    print("in matrix form")
    n = 3
    m = []
    for i in range(0, len(res), n):
        m.append(res[i:i+n])
    
    for row in m:
        print(row)
    print()
    print("in list form")
    return res
    n = 3
    m = []
    for i in range(0, len(res), n):
        m.append(res[i:i+n])

    for row in m:
        print(row)
print(spiral([
    [1,2,3],
    [4,5,6],
    [7,8,9]
    
]))


