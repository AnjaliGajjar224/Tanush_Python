"""
Arithmetic Operators

+ , - , * , / , %(Remainder), //(floor division), ** (Exponent)

Comparison Operators:
1. == (Equal to)
2. != (Not Equal to)
3. > (Greater than)
4. < (Less than)
5. >= (Greater than or equal to)
6. <= (Less than or equal to)

---> It always returns Boolean value (True, False)
"""

# print(15 == 15)              # True
# print(15 != 15)              # False     
# print( 15 > 12)              # True
# print( 15 < 12)              # False
# print( 15 >= 15)             # True
# print( 15 <= 15)             # True

"""
1) if
2) if..else
3) if..elif..else
4) if ladder (Nested if)

-------------------------

Syntax:

1 ) if condition:
         statements
         statements

2) if condition:
        statements
    else:
        statements

3) if condition1:
        statements
    elif condition2:
        statements
    else:
        statements

"""
# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))
# if num1 > num2:
#     print(num1,"is greater than",num2)
# else:
#     print(num1,"is less than",num2)

"""
1. Check Whether the given number is even or odd.
2. Check Whether the given number is positive or negative.
3. Check Whether the given number is divisible by 3.
4. A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
    # Ask user for quantity
    # Assume each unit's cost is 100.
    # Judge and print total cost for user. 
"""
# Task 4

# quantity = int(input("Enter quantity: "))
# cost = quantity * 100

# if cost > 1000:
#     print("You will get 10% discount")
#     total = cost - (cost * 0.1)
#     print("Total cost: ",total)

# else:
#     print("Total cost: ",cost)


"""
5. A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount.

6. A school has following rules for grading system:
    # a. Below 25 - F
    # b. 25 to 45 - E
    # c. 45 to 50 - D
    # d. 50 to 60 - C
    # e. 60 to 80 - B
    # f. Above 80 - A
    # Ask user to enter marks and print the corresponding grade.

7. A student will not be allowed to sit in exam if his/her attendance is less than 75%.
    # Take following input from user:
    # Number of classes held
    # Number of classes attended.
    # And print:
    # percentage of class attended
    # Is student is allowed to sit in exam or not.
"""
held_classes = int(input("Enter number of classes held: "))
attended_classes = int(input("Enter number of classes attended: "))

percentage = (attended_classes / held_classes) * 100

if percentage < 75:
    print("You are not allowed to sit in exam")
else:
    print("You are allowed to sit in exam")
"""
8. Take a three numbers from the user and find maximum.
"""