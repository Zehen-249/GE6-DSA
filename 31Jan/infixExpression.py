#EVALUATE   INFIX EXPRESSIONS

from module.stacks import Stack

def solveInfix(exp):
    opStack = Stack()
    valStack = Stack()

    operators = '(+-*/'
    num = ''
    for i in range(len(exp)):
        if(exp[i] in operators):
            opStack.push(exp[i])
        elif(exp[i].isdigit()):
            num+=exp[i]
            if(exp[i+1].isdigit()):
                continue
            else:
                valStack.push(int(num))
                num = ''
        elif(exp[i] == ')'):
            operation = opStack.pop()
            b = valStack.pop()
            a = valStack.pop()
            if(operation == '+'):
                valStack.push(int(a) + int(b))
            elif(operation == '-'):
                valStack.push(int(a) - int(b))
            elif(operation == '*'):
                valStack.push(int(a) * int(b))
            elif(operation == '/'):
                valStack.push(int(a) / int(b))
            opStack.pop()
            
    if(opStack.len !=0):
        operation = opStack.pop()
        b = valStack.pop()
        a = valStack.pop()
        if(operation == '+'):
            valStack.push(int(a) + int(b))
        elif(operation == '-'):
            valStack.push(int(a) - int(b))
        elif(operation == '*'):
            valStack.push(int(a) * int(b))
        elif(operation == '/'):
            valStack.push(int(a) / int(b))
    return valStack.pop()

print(solveInfix(exp = input("Enter Expression: ").strip()))