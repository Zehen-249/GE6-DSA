class SinglyLinkedListOnlyHead:
    class Node:
        def __init__(self, data, next = None):
            self.data = data
            self.next = next

    def __init__(self):
       self.head = None

    def add(self,data, pos=-1):
        length = len(self)
        if(length+1 == pos):
            pos = -1

        if(length+1 < pos):
            print( f"ERROR: Index {pos-1} out of bound for length {length}")
            return None
   
        if(self.head == None):
            self.head = self.Node(data)
            return
        
        ptr = self.head 
        if(pos == -1):
            while(ptr.next != None):
                ptr = ptr.next
            ptr.next = self.Node(data)
        elif(pos == 0):
            newNode = self.Node(data, self.head)
            self.head = newNode
        else:
            i=1
            while(i + 1 < pos):
                ptr = ptr.next
                i += 1
            newNode = self.Node(data, ptr.next)
            ptr.next = newNode

    def remove(self,pos = -1):
        length = self.__len__()
        if(length==0):
            return None
        if(pos > length):
            return f"ERROR: Index {pos} out of bound for length {length}"
        
        if(pos == 1):
            temp = self.head.data
            self.head = self.head.next
            return temp
        elif(pos == -1):
            pos = length

        ptr = self.head
        i =1 
        while(i+1 < pos):
            ptr = ptr.next
            i+=1
        if(ptr.next == None):
            temp = ptr.data
            self.head = None
            return temp
        temp = ptr.next.data
        ptr.next = ptr.next.next
        return temp

    def __len__(self):
        if(self.head == None):
            return 0
        count = 1
        ptr = self.head
        while(ptr.next!=None):
            count+=1
            ptr = ptr.next
        return count
    
    def __str__(self):
        ptr = self.head
        if(ptr == None):
            return "HEAD -> None"
        ret = "HEAD -> "
        while(ptr.next != None):
            ret += f"[{ptr.data}] -> "
            ptr = ptr.next
        return ret + f"[{ptr.data}]"
    
    def sumElements(self):
        sum = 0
        ptr = self.head
        while(ptr != None):
            sum += ptr.data
            ptr = ptr.next
        return sum
    

class SinglyLinkedListWithTail(SinglyLinkedListOnlyHead):
    def __init__(self):
        super().__init__()
        self.tail = None
    
    def add(self,data, pos=-1):
        length = len(self)
        if(length+1 == pos):
            pos = -1

        if(length+1 < pos):
            print( f"ERROR: Index {pos-1} out of bound for length {length}")
            return None
            
        if(self.head == None):
            newNode = self.Node(data)
            self.head = newNode
            self.tail =  newNode
            return
        if(pos == -1):
            self.tail.next = self.Node(data)
            self.tail = self.tail.next
        elif(pos == 1):
            newNode = self.Node(data, self.head)
            self.head = newNode
        else:
            i=1
            ptr = self.head
            while(i + 1 < pos):
                ptr = ptr.next
                i += 1
            newNode = self.Node(data, ptr.next)
            ptr.next = newNode
    
    def remove(self,pos = -1):
        length = self.__len__()
        if(length==0):
            return None
        if(length==1):
            temp = self.head.data
            self.head,self.tail=None,None
            return temp
        if(pos > length):
            return f"ERROR: Index {pos} out of bound for length {length}"
        
        if(pos == 1):
            temp = self.head.data
            self.head = self.head.next
            return temp
        elif(pos == -1):
            ptr = self.head
            while(ptr.next != self.tail):
                ptr = ptr.next
            temp = self.tail.data
            self.tail = ptr
            ptr.next = None
            return temp
        
        ptr = self.head
        i = 1 
        while(i+1 < pos):
            ptr = ptr.next
            i+=1
        if(ptr.next == None):
            temp = ptr.data
            self.head = None
            self.tail = None
            return temp
        temp = ptr.next.data
        ptr.next = ptr.next.next
        return temp

    def __str__(self):
        ptr = self.head
        if(ptr == None):
            return "HEAD,TAIL -> None"
        ret = "HEAD -> "
        while(ptr.next != None):
            ret += f"[{ptr.data}] -> "
            ptr = ptr.next
        return ret + f"[{ptr.data}] <- TAIL"



# LL = SinglyLinkedListOnlyHead()
# LL.add(2)
# LL.add(3)
# print(LL)
# LL.add(5,4)
# print(LL)
# print(len(LL))

LL = SinglyLinkedListOnlyHead()
LL.add(2)
LL.add(3)
LL.add(5,1)
print(LL)
LL.add(7,2)
print(LL)
# print(LL.tail.data)
# print(LL.sumElements())
print(LL.remove())
print(LL)
# print(LL.tail.data)
print(LL.remove(1))
print(LL)
# print(LL.tail.data)
LL.add(3)
print(LL)
LL.remove()
LL.remove()
print(LL)
print(LL.remove())
print(LL)
print(LL.remove())
print(LL)