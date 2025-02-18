from module.stacks import Stack

def reverse(file):
    stack = Stack()
    with open(file,'r') as f:
        lines = f.readlines()
    for line in lines:
        stack.push(line.rstrip('\n'))
        print(line)
    with open(file,'w') as f:
        while(stack.len > 0):
            line = stack.pop()
            f.writelines(line + '\n')
            print(line)

reverse("31Jan\\file.txt")