from node import Node

class OrderedList:
    def __init__(self):
        self.head = None
            
    def __str__(self):
        current = self.head
        selflist = []
        while current != None:
            selflist.append(current.getData())
            current = current.getNext()
        return str(selflist)
        
    def isEmpty(self):
        return self.head == []
    
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count
    
    def add(self,item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)
            
    def remove(self,item):
        current = self.head
        previous = None 
        found = False
        while not found and current != None:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
                
            if previous == None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())
    
    def pop(self):
        current = self.head
        previous = None
        count = 0
        while current.getNext() != None:
            previous = current
            current = current.getNext()
        
        if current == self.head:
            self.head = None
        else:
            data = current.getData()
            previous.setNext(None)
        return data
            
    #def pop(self,pos):
    #   pass
    
    def search(self,item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData()>item:
                    stop = True
                else:
                    current = current.getNext()
        return found
        
mylist = OrderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist)
print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))
print ('removi', mylist.pop())
print ('removi', mylist.pop())
print(mylist)
