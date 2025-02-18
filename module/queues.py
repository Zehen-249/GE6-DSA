class Queue:
    def __init__(self,*args,**kargs):
        if(len(args) > 0):
            self.qu = list(args)
            self.len = len(args)
        else:
            self.qu = []
            self.len = 0
        if("capacity" in kargs):
            self.capacity = kargs["capacity"]
        else:
            self.capacity =None 

    def enqueue(self,*args):
        for i in args:
            if(self.capacity and ( self.len == self.capacity)):
                print(f"ERROE: FULL QUEUE capacity {self.capacity}")
            self.qu.append(i)
            self.len +=1
    
    def dequeue(self,ele):
        if(self.capacity and (self.len == 0)):
            print(f"ERROE: EMPTY QUEUE")
        self.qu.pop(0)
        self.len -= 1

    def isEmpty(self):
        return self.len == 0

    def __len__(self):
        return(self.len)
    
    def __str__(self):
        return f"<--OUT {self.qu} <--IN"

que = Queue(1,3,5,6,4,capacity = 6)
que.enqueue(3,3,5)
print(que)
print(len(que))