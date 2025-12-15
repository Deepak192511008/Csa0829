n = 6

# 1) Pyramid pattern
for i in range(1, n+1):
    print(" " * (n-i) + "*" * (2*i-1))
print()

# Sample Output:
#      *
#     ***
#    *****
#   *******
#  *********
# ***********


# 2) Increasing left triangle
for i in range(1, n+1):
    print("*" * i)
print()

# Sample Output:
# *
# **
# ***
# ****
# *****
# ******


# 3) Right-aligned increasing triangle
for i in range(1, n+1):
    print(" " * (n-i) + "*" * i)
print()

# Sample Output:
#      *
#     **
#    ***
#   ****
#  *****
# ******


# 4) Decreasing left triangle
for i in range(n, 0, -1):
    print("*" * i)
print()

# Sample Output:
# ******
# *****
# ****
# ***
# **
# *


# 5) Right-aligned decreasing triangle
for i in range(n, 0, -1):
    print(" " * (n-i) + "*" * i)
print()

# Sample Output:
# ******
#  *****
#   ****
#    ***
#     **
#      *


# 6) Pascal’s Triangle
for i in range(n):
    nu = 1
    print(" " * (n-i), end=" ")
    for j in range(i+1):
        print(nu, end=" ")
        nu = nu * (i-j) // (j+1)
    print()
print()

# Sample Output:
#       1
#      1 1
#     1 2 1
#    1 3 3 1
#   1 4 6 4 1
#  1 5 10 10 5 1


# 7) Hollow square pattern
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n-1 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Sample Output:
# * * * * * *
# *         *
# *         *
# *         *
# *         *
# * * * * * *

