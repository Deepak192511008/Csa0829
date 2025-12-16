#Write a Python program to convert a dictionary to a list of tuples.
d={1:"rayhaan",2:"emad",3:"vijay"}
t=()
print(list(d.items()))

# Write a Python program to sort a given dictionary by its values.
d = {1: "rayhaan", 3: "emad", 2: "vijay"}
dv = list(d.values())
dv.sort()
print(dv)
sd = {}
for v in dv:
    for k in d:
        if d[k] == v and k not in sd:
            sd[k] = v
            break
print(sd)

#Write a Python program to find the frequency of all elements in a given dictionary.
d = {1: "apple", 2: "banana", 3: "apple", 4: "orange", 5: "banana"}
f = {}
for v in d.values():
    if v in f:
        f[v] += 1
    else:
        f[v] = 1
print(f)

#Write a Python program to find the keys with the maximum and minimum values in a given dictionary.
d = {'a': 5, 'b': 2, 'c': 9, 'd': 3}
max = max(d, key=d.get)
min = min(d, key=d.get)
print("Key with maximum value:", max)
print("Key with minimum value:", min)

#Write a Python program to find the maximum and minimum values in a given dictionary.
d = {'a': 5, 'b': 2, 'c': 9, 'd': 3}
max = max(d.values())
min = min(d.values())
print("maximum value:", max)
print("minimum value:", min)

#Write a Python program to remove a given key from a given dictionary.
d = {'a': 5, 'b': 2, 'c': 9, 'd': 3}
r = 'b'
if r in d:
    del d[r]
print("Updated dictionary:", d)

#Write a Python program to check if a given value exists in a given dictionary.
d = {'a': 5, 'b': 2, 'c': 9, 'd': 3}
value = 9
print(value in d.values())

#Write a Python program to concatenate two dictionaries
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d1.update(d2)
print(d1)

#Write a Python program to check if a given key exists in a given dictionary.
d = {'a': 5, 'b': 2, 'c': 9, 'd': 3}
value = 'b'
print(value in d.keys())

#Write a Python program to sort a given tuple in ascending order.
t = (3, 5, 1, 2, 8, 4)
s = tuple(sorted(t))
print(s)

#Write a Python program to find the sum of all elements in a given tuple.
t = (3, 5, 1, 2, 8, 4)
s=0
for i in t:
  s+=i
print(s)

#Write a Python program to convert a list of tuples to a list of lists.
l=[(1,2),(3,4,5),(6,7,8,9)]
for i in range (len(l)):
  l[i]=list(l[i])
print(l)

#Write a Python program to check if a given element exists in a given tuple.
t = (3, 5, 1, 2, 8, 4)
e=int(input("enter element "))
f=False
for i in t:
  if i==e:
   f=True
if f==True:
  print("yes")
else:
  print("no")

#Write a Python program to find the index of a given element in a given tuple.
t = (10, 20, 30, 40, 50)
e = 30

if e in t:
    i = t.index(e)
    print("Index of", e, "is", i)
else:
    print("Element not found in tuple")



