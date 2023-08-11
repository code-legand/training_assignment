byteString = lambda string: b''.join([bytes(ord(i)) for i in list(string)])


file = open("f1.txt", "w")
file.write("hello world")
file.close()

file = open("f1.txt", "r")
content = file.read()
print(content)
file.close()

file = open("f2.bin", "wb")
content = byteString(content)
file.write(content)
file.close()

file = open("f2.bin", "r")
content = file.read()
print(content)
file.close()


