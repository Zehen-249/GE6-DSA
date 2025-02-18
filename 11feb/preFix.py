#evaluation of prefix expressions

from module.stacks import Stack

def solvePrefix(exp:str)->int:
    valStack = Stack()
    for i in range(len(exp)-1,-1,-1):
        if(exp[i] in "+-/*%^"): 
            op1 = int(valStack.pop())
            op2 = int(valStack.pop())

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
exp = "-+23+45"
print(solvePrefix(exp))