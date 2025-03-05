def arithmetic_operations(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operator"
    
'''
num1=int(input())
num2=int(input())
operator=input()
print(arithmetic_operations(num1,num2,operator))
'''