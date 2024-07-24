

num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))
print(type(num1))
print(type(num2))


def sum(num1, num2):
    print("Sum of {num1} and {num2} is : ", num1+num2)


def difference(num1, num2):
    print("Difference of {num1} and {num2} is : ", (num1-num2))


def division(num1, num2):
    print("Division of {num1} and {num2} is : ", num1/num2)


def multiplication(num1, num2):
    print("Multiplication of {num1} and {num2} is : ", num1*num2)


user_operation = input(
    "Enter what you want to do with 2 numbers (add/sub/div/multiply) : ")

if user_operation == "add":
    sum(num1, num2)
elif user_operation == "sub":
    difference(num1, num2)
elif user_operation == "div":
    division(num1, num2)
elif user_operation == "multiply":
    multiplication(num1, num2)
else:
    print("Enter valid operation...!")
