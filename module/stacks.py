class Stack:
    def __init__(self, *args,size=False):
        self.st = []
        self.len = len(args)
        self.size = size

        if((bool(self.size) & (self.size >= self.len)) or  not bool(self.size)):
            for i in args:
                self.st.append(i)
        else:
            for i in range(self.size):
                self.st.append(args[i])

    def push(self, element):
        if((self.size and self.len < self.size) or not self.size):
            self.st.append(element)
            self.len+=1
        else:
            print("ERROR: Stack Overflow")


    def pop(self):
        if(self.len>0):
            self.len-=1
            return self.st.pop()
        else:
            print("ERROR: Stack Underflow")
            return None

    def peek(self):
        if(self.len>0):
            return self.st[-1]
        else:
            print("EMPTY ")
            return None
    
    def show(self):
        if(self.len>0):
            print("[ ",end="")
            for i in self.st:
                print(i,end=" ")
            print("] <-- Top")
        else:
            print("EMPTY <-- Top")
    def __str__(self):
        return f"{self.st} <-- TOP"
        
    def __len__(self):
        return self.len

st = Stack(3,5,7,9,4,3,size=5)
st2 = Stack(5,7,9,0)
print(st)
st.show()