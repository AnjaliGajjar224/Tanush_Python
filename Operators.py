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
print(43&45)
print(16&32)
print(89&45)
print(78&45)
print(78&89)
print(56&16)