myFile = open('Example.txt')
print(type(myFile))
print(myFile)

print(myFile.read())
myFile.seek(0)
print(myFile.read())

myFile.seek(0)
print(myFile.readlines())