#Write a Python program to raise a custom exception.
class MyError(Exception):
  pass

try:
  raise MyError("Custom error occurred")
except MyError as e :
  
    print(e)


#Write a Python program to handle multiple exceptions using a single except block
try:
    a = 1
    b = 0
    r = a / b
    print("Result:", r)
except (ValueError, ZeroDivisionError):
    print("Either a value error or division by zero error has occurred")
  
#Write a Python program to handle a NameError exception.
try:
  print(a)
except NameError:
  print("Name Error has occured")

#Write a Python program to handle a KeyError exception.
try:
  a={1:'one',2:'two'}
  print(a[3])
except KeyError:
  print("Key Error has occured")

#Write a Python program to handle a FileNotFoundError exception.
try:
  a=open("192511008.txt",'r')
except FileNotFoundError:
  print("File Not Found Error has occured")

#Write a Python program to handle a ValueError exception.
try:
  int("abc")
except ValueError:
  print("Value Error has occured")

#Write a Python program to handle a TypeError exception.
try:
    c = 10 + '3'
except TypeError:
    print("Type Error has occurred")
  
#Write a Python program to handle an IndexError exception.
try:
  l=[1,2,3]
  print(l[5])
except IndexError:
    print("Index Error has occurred")

#Write a Python program to handle a ZeroDivisionError exception.
try:
  print(1/0)
except ZeroDivisionError:
    print("Zero Division Error has occurred")
