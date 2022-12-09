str1 = " Test Python Program "
print(str1)
print(str1.strip())
print(str1.lstrip())
print(str1.rstrip())

str2 = "\nTest\nPython\nProgram"
print(str2)
print("---")
print(str2.replace("\n", ""))
print("---")
print(str2.replace("\n", "", 1))

print(str1.replace(" ", ""))

print(str1.split())
print(str2.split())
