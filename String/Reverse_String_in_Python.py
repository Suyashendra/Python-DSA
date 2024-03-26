# Reverse String in Python

# String in Python are immutable.
# eg- 
# s = "Hello"
# s[0] = "P"
# print(s)
# Output: TypeError: 'str' object does not support item assignment

# Reverse String in Python
# Method 1:

s = input("Enter your string to reverse: ")
reverse_str = ""
for i in s:
    reverse_str = i + reverse_str
print(reverse_str)

# Method 2:

s1 = input("Enter your string to reverse: ")
reverse_str = s1[::-1]
print(reverse_str)