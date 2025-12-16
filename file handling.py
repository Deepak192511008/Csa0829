#Write a Python program to write a list of strings to a file.
l = [
    "Hello, world!",
    "This is a sample file.",
    "Each string will be on a new line."
]
f = open("192511008.txt", "w")
for i in l:
    f.write(i + "\n")
f.close()
print("Data written")

#Write a Python program to copy the contents of one file to another.
file = open("192511008.txt", "w")
file.write("Hello\nThis is a sample file\nFile copy program")
file.close()
print("Source file created")

s = open("192511008.txt", "r")
d = open("192511008.txt", "a")  
for l in s:
    d.write(l)
s.close()
d.close()
print("File copied successfully")

f = open("192511008.txt", "r")
for l in f:
    print(l, end="")
f.close()

#Write a Python program to count the number of characters in a file.
f = open("192511008.txt", "w")
f.write("Hello World\nThis is a file\nPrinting file contents")
f.close()

f = open("192511008.txt", "r")
c = 0
for l in f:
    c += len(l)  
f.close()
print("Number of characters in the file:", c)

#Write a Python program to count the number of lines in a file.
f = open("192511008.txt", "w")
f.write("Hello World\nThis is a file\nPrinting file contents\n")  # <-- add \n
f.close()

f = open("192511008.txt", "r")
c = 0
for l in f:
    c += 1
f.close()
print("Number of lines in the file:", c)

#Write a Python program to count the number of words in a file.
f = open("192511008.txt", "w")
f.write("Hello World\nThis is a file\nPrinting file contents\n")  # <-- add \n
f.close()

f = open("192511008.txt", "r")
c= 0
for l in f:
    w = l.split()
    c += len(w)
f.close()
print("Number of words in the file:",c)

#Write a Python program to read a file and display its contents on the screen.
file = open("192511008.txt", "w")
file.write("Hello\nThis is a sample file\nFile copy program")
file.close()

f = open("192511008.txt", "r")
for l in f:
    print(l, end="")
f.close()
