# Escape Sequence and Raw String

# s = 'Welcome to Python's code' 
# print(s)
# Output: Invalid Syntax

s = 'Welcome to Python\'s code'
print(s)
# Output: Welcome to Python's code

s1 = "Hi,\nWelcome"
print(s1)
# Output:
# Hi,
# Welcome

s2 = "A simple \ example"
print(s2)
# Output: A simple \ example

s3 = "Backslash at the end \\"
print(s3)
# Output: Backslash at the end \

s4 = "\\n"
print(s4)
# Output: \n

s5 = "\\t"
print(s5)
# Output: \t

s6 = "C:\project\name.py"
print(s6)
# Output: 
# C:\project
# ame.py

s7 = "C:\project\\name.py"
print(s7)
# Output: C:\project\name.py

# Raw String - using r or R at the begining of string literal.
s8 = r"C:\project\name.py"
print(s8)
# Output: C:\project\name.py