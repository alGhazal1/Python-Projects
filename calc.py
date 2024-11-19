#calculator app

def add (num1, num2):
    return(num1 + num2)

#subtract
def subtract (num1, num2):
    return(num1 - num2)

#divide
def divide (num1, num2):
    return(num1 / num2)

#multiply
def multiply (num1, num2):
    return(num1 * num2)

#select operator
print('Enter operator')
print('1. Addition')
print('2. Subtraction')
print('3. Division')
print('4. Multiplication')

#User input
operator= int(input('Select operation 1,2,3,4:'))

num1 = int(input('Enter first number:'))
num2 = int(input('Enter second number:'))

if operator == 1:
    print("num1", "+", "num2","=", add(num1,num2))

elif operator == 2:
    print("num1", "-", "num2","=", subtract(num1,num2))

elif operator == 3:
    print("num1", "/", "num2","=", divide(num1,num2))

elif operator == 4:
    print("num1", "*", "num2","=", multiply(num1,num2))    