#evaluation of postfix expressions

from module.stacks import Stack

def solvePostFix(exp:str)->int:
    valStack = Stack()
    for i in range(len(exp)):
        if(exp[i] in "+-/*%^"): 
            op2 = int(valStack.pop())
            op1 = int(valStack.pop())

            if(exp[i] == "+"):
                valStack.push(op1 + op2)
            elif(exp[i] == "-"):
                valStack.push(op1 - op2)
            elif(exp[i] == "*"):
                valStack.push(op1 * op2)
            elif(exp[i] == "/"):
                valStack.push(op1 / op2)
            elif(exp[i] == "%"):
                valStack.push(op1 % op2)
            elif(exp[i] == "^"):
                valStack.push(op1 ** op2)
        else:
            valStack.push(exp[i])

    return valStack.pop()

exp = "45+23+-"
print(solvePostFix(exp))