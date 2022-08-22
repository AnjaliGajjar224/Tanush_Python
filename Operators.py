"""
Assignment Operators:

= (Assignment)
+= (Add and assign) # a += 10 ----> a = a + 10
-= (Subtract and assign) # a -= 10 ----> a = a - 10
*= (Multiply and assign) # a *= 10 ----> a = a * 10
/= (Divide and assign) # a /= 10 ----> a = a / 10
%= (Modulus and assign) # a %= 10 ----> a = a % 10
//= (Floor division and assign) # a //= 10 ----> a = a // 10
**= (Exponent and assign) # a **= 10 ----> a = a ** 10

"""

# a = 10
# print(a)            # 10

# a += 10             # a = a + 10 ---> a = 10 + 10 = 20
# print(a)            # 20

# a -= 5              # a = a - 5 ---> a = 20 - 5 = 15
# print(a)            # 15

# a **= 2            # a = a ** 2 ---> a = 15 ** 2 = 225
# print(a)           # 225

"""
Bitwise Operators:

1. & (AND)
2. | (OR)
3. ^ (XOR)
4. >> (Right shift)
5. << (Left shift)
---------------------------------

Decimal to Binary Conversion:

43 = 101011

2 | 43
2 | 21 ---> 1
2 | 10 ---> 1
2 | 5 ---> 0
2 | 2 ---> 1
2 | 1 ---> 0

----> Botom up approach

Binary to Decimal Conversion:

43 - 1   0   1   0   1    1

     1 | 2 | 4 | 8 | 16 | 32 | 64 | 128

1 + 4 + 16 + 32 = 43

45 - 101101

--------------------------------

1. &(AND)

Truth Table:
----------------
a | b | a & b
----------------
0 | 0 | 0
0 | 1 | 0
1 | 0 | 0
1 | 1 | 1

43  -  1   0   1   0   1    1
&      &   &   &   &   &    &
45  -  1   0   1   1   0    1
------------------------------
       1   0   1   0   0    1  (41)
"""
# print(43&45)
# print(16&32)
# print(89&45)
# print(78&45)
# print(78&89)
# print(56&16)

"""
2. | (OR)

Truth Table:
----------------
a | b | a | b
----------------
0 | 0 |  0
0 | 1 |  1
1 | 0 |  1
1 | 1 |  1

43  -  1   0   1   0   1    1
|      |   |   |   |   |    |
45  -  1   0   1   1   0    1
------------------------------
       1   0   1   1   1    1   (47)
"""

# print(43|45)

"""
3. ^ (XOR)

Truth Table:
----------------
a | b | a ^ b
----------------
0 | 0 |  0
0 | 1 |  1
1 | 0 |  1
1 | 1 |  0

43  -  1   0   1   0   1    1
^      ^   ^   ^   ^   ^    ^
45  -  1   0   1   1   0    1
------------------------------
       0   0   0   1   1    0   (6)
"""
# print(43^45)

"""
4. Shift Operaters:

>> (Right shift)
<< (Left shift)


>>(Right Shift)

43 >> 2

43 - 1   0   1   0   1    1
     1 | 2 | 4 | 8 | 16 | 32 | 64 | 128

43 >> 2 

------------------------------
1010 - (10)
"""

# print(43>>2)

"""
<<(Left Shift)

15 << 3
"""

# print(15<<3)

"""
Logical Operators:

1. and (AND)

     True and True = True
     True and False = False
     False and True = False
     False and False = False

2. or (OR)
     True or True = True
     True or False = True
     False or True = True
     False or False = False

3. not (NOT)
     not True = False
     not False = True

It always returns a boolean value.
"""
# Find the largest number among the three numbers

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))


# Without Logic Operators

# if num1 > num2:
#      if num1 > num3:
#           print(num1,"is the largest number")
#      else:
#           print(num3,"is the largest number")
# elif num2 > num3:
#      print(num2,"is the largest number")
# else:
#      print(num3,"is the largest number")

# With Logic Operators

# if num1 > num2 and num1 > num3:
#      print(num1,"is the largest number")
# elif num2 > num3 and num2 > num1:
#      print(num2,"is the largest number")
# else:
# #      print(num3,"is the largest number")

# print(15 > 12 and 12 > 10)                      # True and True = True
# print(15 > 12 and 12 < 10)                      # True and False = False
# print(15 > 12 or 12 > 10)                       # True or True = True
# print(15 > 12 or 12 < 10)                       # True or False = True
# print(not(15 > 12))                             # not True = False

"""
Take a number from the user and check whether the number is divisible by 3 and 5 both or not.
"""

"""
Membership Operators:

1. in
2. not in

It always returns a boolean value.
"""

# print('a' in 'Hello')                            # False
# print('b' in 'banana')                           # True

# print("Python" in "python is a fun Python")             # True

# print('a' not in 'banana')                   # False
# print('k' not in 'banana')                   # True

"""
Identity Operators:

1. is (is operator)
2. is not (is not operator)
"""

# a = 15
# b = 10
# c = 15


# print(id(a))
# print(id(b))
# print(id(c))


# print(a is b)      # False
# print(a is c)      # True

# print(a is not b)  # True
# print(a is not c)  # False


# name = input("Enter your name: ")

# print(name)

"""
Take two strings from the user and check whether the first strong is availabe in second strong or not.

e.g. Python is a programming language.

ch = is

Ouput: Exist

ch = in

Output: Not exist
"""

# my_str = input("Enter your string: ")

# ch = input("Enter string you want to check :")

# if ch in my_str:
#      print(ch, "is present in a Original String")
# else:
#      print(ch,"is not present in original string")