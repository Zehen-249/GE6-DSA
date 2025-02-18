# infox to postfix and prefix conversion

from module.stacks import Stack

def toPostFix(exp:str)->str:
    postExp = ""
    operators = {"-":1, "+":2, "*":3, "/":4}
    opStack = Stack()
    for i in exp:
        if(i=="("):
            opStack.push(i)
        elif(i in operators.keys()):
            if((opStack.len > 0) and (opStack.peek() != "(")):
                if(operators[opStack.peek()] < operators[i]):
                    peek = opStack.pop()
                    opStack.push(i)
                    i = peek
            opStack.push(i)
        elif(i == ")"):
            peek = opStack.pop()
            while(peek != "("):
                postExp += peek
                peek = opStack.pop()
        else:
            postExp += i
        
    return postExp

def toPreFix(exp:str)->str:
    def reverse(exp):
        reversedExp = ""
        for i in range(len(exp)-1,-1,-1):
            if(exp[i] == ")"):
                reversedExp += "("
            elif(exp[i] == "("):
                reversedExp += ")"
            else:
                reversedExp += exp[i]
        
        return reversedExp
    return(reverse(toPostFix(reverse(exp))))

exp = "((A+B)-(D*(C-D)))"
print(toPostFix(exp))
print(toPreFix(exp))
