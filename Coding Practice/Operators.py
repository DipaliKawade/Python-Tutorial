#Operators in python
#***7 Assignment Operators***
# = assignment operator
#right side side value to the left side variable
print("=Assignment Operators")
a = 10  
print("a =", a)

#add and assignment operator
print("+=Add and Assignment Operators")
a=15
a += 5
print("a =", a)

#Subtract and Assignment Operators
print("-=Subtract and Assignment Operators")
a=20
a -= 3
print("a =", a) 

#Multiply and Assignment Operators
print("*=Multiply and Assignment Operators")
a=20
a *= 2
print("a =", a)

#Divide and Assignment Operators
print("/=Divide and Assignment Operators")
a=15
a /= 2
print("a =", a)

#Modulus and Assignment Operators
print("%=Modulus and Assignment Operators")
a=2
a %= 2
print("a =", a)

#Floor Division and Assignment Operators
print("//=Floor Division and Assignment Operators")
num1=10
num2=5
a =num1// num2
print("a =", a)

#Exponent and Assignment Operators
print("**=Exponent and Assignment Operators")
a=2
a **= 2
print("a =", a)

#Arithmetic Operators
print("---------Arithmetic Operators---------")
num1 = 10
num2 = 5
print("num1 =", num1)
print("num2 =", num2)
print("Addition :", num1 + num2)
print("Subtraction :", num1 - num2)
print("Multiplication :", num1 * num2)
print("Division :", num1 / num2)
print("Modulus :", num1 % num2)
print("Floor Division :", num1 // num2)
print("Exponent :", num1 ** num2)

#comparison Operators
print("---------Comparison Operators---------")
print("Equal :", num1 == num2)
print("Not Equal :", num1 != num2)
print("Greater Than :", num1 > num2)
print("Less Than :", num1 < num2)
print("Greater Than or Equal To :", num1 >= num2)
print("Less Than or Equal To :", num1 <= num2)

#logical Operators
print("---------Logical Operators---------")
x = True
y = False
print("x =", x)
print("y =", y)
print("Logical AND :", x and y)
print("Logical OR :", x or y)
print("Logical NOT :", not x)

#bitwise Operators
print("---------Bitwise Operators---------")
a = 10  # 1010 in binary
print("a =", a)
print("Bitwise AND :", a & 5)  # 0101 in binary(both true then true)
print("Bitwise OR :", a | 5)   # 0101 in binary(either true then true)
print("Bitwise XOR :", a ^ 5)  # 0101 in binary(either true then true but not both)
print("Bitwise NOT :", ~a)      # 0101 in binary(negation of a)

#identity Operators
print("---------Identity Operators---------")
x = 5
y = 5
print("x =", 5)
print("y =", 5)
print("id(x) :", id(x))
print("id(y) :", id(y))
print(x is not y)

#membership Operators
print("---------Membership Operators---------")
list1 = [1, 2, 3, 4, 5]
print("list1 =", list1)
print("Is 3 in list1 :", 3 in list1)
print("Is 6 not in list1 :", 6 not in list1)

##operator precedence
print("---------Operator Precedence---------")
print("1. Parentheses")
print("2. Exponentiation")
print("3. Multiplication and Division")
print("4. Addition and Subtraction")

#operator precedence example
print("---------Operator Precedence Example---------")
result = 2 + 3 * 4
print("Result :", result)

#operator precedence example with parentheses
print("---------Operator Precedence Example with Parentheses---------")
result = (2 + 3) * 4
print("Result :", result)

#operator precedence example with multiple operators
print("---------Operator Precedence Example with Multiple Operators---------")
result = 2 + 3 * 4 - 5 / 2
print("Result :", result)

#operator precedence example with multiple operators and parentheses
print("---------Operator Precedence Example with Multiple Operators and Parentheses---------")
result = (2 + 3) * (4 - 5) / 2
print("Result :", result)
