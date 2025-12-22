#Write a Python program to write a list of strings to a file.
lines = [
    "Hello, world!",
    "This is a sample file.",
    "Each string will be on a new line."
]

file = open("192511008.txt", "w")

for line in lines:
    file.write(line + "\n")

file.close()

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
print(f.read())
f.close()

#Write a Python program to count the number of characters in a file.
# Create and write to file
f = open("192511008.txt", "w")
f.write("Hello World\nThis is a file\nPrinting file contents")
f.close()
f = open("192511008.txt", "r")
content = f.read()
f.close()
c = len(content)
print("Number of characters in the file:", c)

#Write a Python program to count the number of lines in a file.
f = open("192511008.txt", "w")
f.write("Hello World\nThis is a file\nPrinting file contents\n")
f.close()


f = open("192511008.txt", "r")
lines = f.readlines()
f.close()


c = len(lines)

print("Number of lines in the file:", c)

#Write a Python program to count the number of words in a file.
f = open("192511008.txt", "w")
f.write("Hello World\nThis is a file\nPrinting file contents\n")
f.close()

f = open("192511008.txt", "r")
content = f.read()
f.close()


words = content.split()
c = len(words)

print("Number of words in the file:", c)

#Write a Python program to read a file and display its contents on the screen.
file = open("192511008.txt", "w")
file.write("Hello\nThis is a sample file\nFile copy program")
file.close()

f = open("192511008.txt", "r")
print(f.read(), end="")
f.close()
