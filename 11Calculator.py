a = input("Enter first number ")
operator = input("Enter Operator (+,-,*,/,%): ")
b = input("Enter Second number ")

num1 = int(a)
num2 = int(b)

if operator == '+':
    print(num1+num2)
elif operator == '-':
    print(num1-num2)
elif operator == '*':
    print(num1*num2)
elif operator == '/':
    print(num1/num2)
elif operator == '%':
    print(num1%num2)
else:
    print("Enter a valid Operation")                                

