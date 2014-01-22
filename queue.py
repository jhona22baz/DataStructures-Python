
class Queue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    def saw(self):
        print (self.items)
        
    def dequeue(self):
        return self.items.pop()
    
    def enqueue(self,item):
        self.items.insert(0,item)
        