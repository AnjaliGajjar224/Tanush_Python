"""
String:
------------
String is a sequence of characters.
String is a ordered.
String is immutable.
"""

# ch = 'a'

# print("Type of ch is: ",type(ch))

# myStr = "Python"

# print(myStr)
# print("Length of string is: ",len(myStr))

"""
    Positive Indexes Negative Index
P         0              -6
y         1              -5
t         2              -4
h         3              -3
o         4              -2
n         5              -1
# """

# print(myStr[0])             # P
# print(myStr[1])             # y
# print(myStr[2])             # t
# print(myStr[3])             # h
# print(myStr[4])             # o
# print(myStr[5])             # n
# print(myStr[6])      # IndexError

# print(myStr[-1])
# print(myStr[-2])
# print(myStr[-3])
# print(myStr[-4])
# print(myStr[-5])
# print(myStr[-6])
# print(myStr[-7])    # IndexError

"""
Take a string from the user and print Length of the string.Take index as well from the user and print character on that index.
"""

"""
Slicing of String

---> substring of mainstring

Syntax:
---------
1 . var_name[start:end:step]
2.  var_name[start:end]
3.  var_name[start:]
4.  var_name[:end]
5.  var_name[:]
"""

# s = "Python is a programming language"

# print("Length of string: ",len(s))

# print(s[0:31])             # slicing start from 0 to 30(31 is not included)
# print(s[5:20])             # slicing start from 5 to 19(20 is not included)
# # print(s[50:90])

# print(s[-30:-15])         # slicing start from -30 to -16(-15 is not included)

# print(s[5:])              # slicing start from 5 to length of the string
# print(s[-25:])            # slicing start from -25 to -1(length of string)

# print(s[:30])             # slicing start from 0 to 30
# print(s[:-15])            # slicing start from -32 to -15

# print(s[:])

# Take a string from the user and print the length of the string. Take starting and ending index for slicing and slice string according to it.

input_str = input("Enter a string: ")

print("Length of string is: ",len(input_str))

print("\nOriginal string is: \n",input_str)

print()
start = int(input("Enter starting index: "))
end = int(input("Enter ending index: "))

print()
print("\nSubstring is:\n")
print(input_str[start:end])

