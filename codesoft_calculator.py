print("select an operation to perform")
print("+ ADD")
print("- SUBTRACT")
print("* MULTIPLY")
print("/ DIVIDE")
num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
opr = input("Enter the opr..(+,-,*,/)")
if opr=="+":
    print("the Sum of two number is: ",num1+num2)
elif opr=="-":
    print("the Subtraction of two number is: ",num1-num2)
elif opr=="*":
    print("the Multiplication of two number is: ",num1*num2)
elif opr=="/":
    print("the Division of two number is: ",num1/num2)
else:
    print("Invalid opr..")