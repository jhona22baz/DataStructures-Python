from node import Node

class UnorderedList():
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
        return self.head == None
    
    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
            
            
        return count
    
    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData()==item:
                found = True
            else:
                current = current.getNext()
        return found
        
    def remove(self,item):
        current = self.head
        previous = None 
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
                
            if previous == None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())

    def append(self,item):
        current = self.head
        while current.getNext() != None:
            current = current.getNext()
        current.setNext(Node(item))
        
    def insert(self,pos,item):
        current = self.head
        previous = None
        count = 0
        newnode = Node(item)
        while current.getNext() != None and not count == pos:
            previous = current
            current = current.getNext()
            count = count + 1
        
        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)
    
    def index(self,item):
        current = self.head
        found = False
        count = 0
        while current != None and not found:
            if current.getData()==item:
                found = True
            else:
                current = current.getNext()
                count = count + 1
        return count 
mylist = UnorderedList()

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)
mylist.append(11)
mylist.append(14)
mylist.add(56)
mylist.insert(2,555)
print(mylist)
print(mylist.size())
mylist.remove(11)
print(mylist)
print(mylist.size())