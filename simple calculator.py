num1 = eval(input("Please enter your first number:"))
num2 = eval(input("Please enter your second number:"))
oper = input("Please enter the operation:")
if oper =='+':
    print(num1+num2)
elif oper =='-':
    print(num1-num2)
elif oper =='*':
    print(num1*num2)
elif oper =='/':
    print(num1/num2)
else:
    print("Invalid operation:")

