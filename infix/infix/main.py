operators = ['+', '-', '*', '/']

def checking_expression(str1) -> list:
    global operators
    lst = str1.split() 
    countInt, countOp = 0, 0
    for i in range(len(lst)):
        if lst[i].isdigit():
            countInt += 1
        elif lst[i] in operators:
            countOp += 1
    if (countOp + countInt != len(lst)):
        raise TypeError("Unknown character. Use only binary operators and unsigned numbers.")
    elif (countOp >= countInt) or (countOp < countInt-1):
        raise ValueError("Not enough values to translate.")
    return lst

def to_infix(str1):
    global operators
    lst = checking_expression(str1) 
    expression = []
    for i in reversed(lst):
        if i.isdigit():
            expression.append(i)
        elif i in operators:
            if len(expression) < 2:
                raise ValueError("Not enough numbers to translate.")
            num1 = expression.pop()
            num2 = expression.pop()
            expression.append(f'({num1} {i} {num2})')
    return expression[0]

def start():
    print("This program translates expressions from prefix form to infix form.\nOnly binary operators are allowed: +, -, *, /. Unsigned numbers are used as operands.")
    try:
        str1 = input("Enter the expression in prefix form using a space as a separator: \n")
        str1 = to_infix(str1)
        return f"Infix expression: {str1}"
    except Exception as e:
        return f"Exception: {e}"

print(start())





