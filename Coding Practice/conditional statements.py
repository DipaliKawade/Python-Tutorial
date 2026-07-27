# if statements
x = 10
if x > 5:
    print("x is greater than 5")
    print("x =", x)

# if-else statements
age = 12
if age >= 18:
    print("Eligible for voating")
else:
    print("Not Eligible for voating") 

# if-elif-else statements
Dipali_marks = 75
if Dipali_marks>=75:
    print("grade A")
elif Dipali_marks>=60:
    print("grade B")
elif Dipali_marks>=35:
    print("grade C")
else:
    print("fail")

#Match Statement or switch case statement
grade = "A"
match grade:
    case"A":
        print("marks is above 75")
    case"B":
        print("marks is above 55")
    case"C":
            print("marks is above 35")
    case _:
            print("fail")

# using uppercase
grade = "a"
temp = grade.upper
match grade:
    case"A":
        print("marks is above 75")
    case"B":
        print("marks is above 55")
    case"C":
            print("marks is above 35")
    case _:
            print("fail")

#nested if else
age=12
nationality="indian"
if age>=18:
        if nationality =="indian":
            print("eligible for voting")
        else:
            print("not eligible for voting")
else:
    print("age is not 18")

# Ternary operator
a = 10
b = 20
result = "a is greater than b" if a > b else "a is less than or equal to b"
print(result)

#looping Staement

# Switch-case statements (using dictionary mapping)
def switch_case(value):
    switcher = {
        1: "One",
        2: "Two",
        3: "Three"
    }
    return switcher.get(value, "Invalid value")

print(switch_case(1))
print(switch_case(2))
print(switch_case(3))
print(switch_case(4))

# For loop
for i in range(5):
    print("Iteration", i)

# print 5th table using for loop
num = 5
for i in range(1, 11):
    print(num, "x", i, "=", num * i) # where x is multiplication sign and * is multiplication operator

# Print 10 table using for loop
print("10 Table:")
for i in range(1, 11):
    print(i*10)

# Nested for loop
for i in range(3):
    for j in range(2):
        print(f"i = {i}, j = {j}")

for i in range(1,4):
    for j in range(1,4):
        print(j) # print on the new line

for i in range(1,4):
    for j in range(1,4):
        print(j, end=" ") # print on the same line

for i in range(1,4):
    for j in range(1,4):
        print(j, end=" ")
        print()  # New line after each inner loop iteration

# print stars pattern using nested for loop
cols = 5
for i in range(1, cols + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()  # New line after each row

#anorher way to print stars pattern using nested for loop
col=3
row=3
for i in range(col):
    for j in range(row):
        print("*", end=" ")
    print()  # New line after each row
    row-=1

col=3
row=3
for i in range(col):
    for j in range(row):
        print("*", end=" ")
    print()  # New line after each row
    row+=1

# While loop
#execute while the condition is true
count = 0
while count < 5:
    print("Count =", count)
    count += 1

# 2nd Example of while loop
i=1
while i<=5:
    print("Hello World")
    i+=1    

# 3rd Example of while loop
num = 1
while num <= 10:
    print(num)
    num += 1    
#break using for loop
for i in range (1, 11):
    if i==5:
        break
    print(i) 

#continue using for loop
for i in range (1, 11):
    if i==5:
        continue
    print(i)

# Break and continue statements
for i in range(10):
    if i == 5:
        print("Breaking the loop at i =", i)
        break
    if i % 2 == 0:
        print("Skipping even number i =", i)
        continue
    print("Current value of i =", i)

# Pass statement
for i in range(5):
    if i == 2:
        pass  # Placeholder for future code
    else:
        print("Current value of i =", i)

# Function definition and calling
def greet(name):
    print("Hello,", name)
    return "Greeting sent to " + name

# Calling the function
greeting_message = greet("Alice")
print(greeting_message)

# Lambda function
square = lambda x: x * x
print("Square of 5 =", square(5))

# List comprehension
squared_numbers = [x * x for x in range(5)]
print("Squared numbers:", squared_numbers)

# Dictionary comprehension
squared_dict = {x: x * x for x in range(5)}
print("Squared dictionary:", squared_dict)

# Set comprehension
squared_set = {x * x for x in range(5)}
print("Squared set:", squared_set)

# Exception handling
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input! Please enter a valid integer.")

    # Finally block
finally:
    print("Execution completed.")   

    # Nested functions
def outer_function():
    print("This is the outer function.")

    def inner_function():
        print("This is the inner function.")

    inner_function()

    # Calling the outer function
outer_function()

# Class definition and object creation
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating an object of the Person class
person1 = Person("Alice", 30)
person1.greet()

# Inheritance
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_student_info(self):
        print(f"Student ID: {self.student_id}")
        self.greet()  # Call the parent class's greet method

        # Creating an object of the Student class
student1 = Student("Bob", 20, "S12345")
student1.display_student_info()

# Polymorphism
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

# Creating objects of the derived classes
dog = Dog()
cat = Cat()

# Calling the sound method (polymorphism)
print(dog.sound())  # Output: Woof!
print(cat.sound())  # Output: Meow!

# Encapsulation
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount.")

    def get_balance(self):
        return self.__balance

    # Creating an object of the BankAccount class
account = BankAccount("123456789", 1000)
account.deposit(500)
account.withdraw(200)
print("Current balance:", account.get_balance())

# Static method
class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b
    

    # Calling static methods
print("Addition:", MathOperations.add(10, 5))
print("Subtraction:", MathOperations.subtract(10, 5))

# Class method

class Circle:
    pi = 3.14159  # Class attribute

    def __init__(self, radius):
        self.radius = radius  # Instance attribute

    @classmethod
    def area(cls, radius):
        return cls.pi * (radius ** 2)

    # Calling class method
print("Area of circle with radius 5:", Circle.area(5))

