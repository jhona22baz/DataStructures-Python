#!/usr/bin/python
'''
 Program Assignment:  LinkedList.py                                                         
 Name:  Jhonatan Bazaldúa Oliva
 Date:  03 Sep 2013
 Description: It's a simple LinkedList 
'''
'''
Class declarations:                                                                                            
    +Node
    +doublyLinkedList

'''
#BASE 0
import math 
class Node:
    """
    Node have dato and next. have a __init__ and __str__ functions for init the method and acept 
    all data. and recive a varible named dato that will bi add to the list 
    """
    def __init__(self, dato):
        self.dato = dato
        self.next = None                
    def __str__(self):
        return str(self.dato)

class  doublyLinkedList:   
    '''
    doublyLinkedList
    recive: 
    funtions:
        +addToFinish
        +AddToInit
        +Delete
        +printList
    '''
    def __init__(self):
        self.head = None
        self.Tail = None        
    def addToFinish(self,dato):  
        nodo_nuevo = Node(dato)
        if self.head == None: 
            self.head = nodo_nuevo
        if self.Tail != None: 
            self.Tail.next = nodo_nuevo
        self.Tail = nodo_nuevo
    def AddToInit(self, dato):
        nodo_nuevo = Node(dato)
        if self.head == None: 
            self.head = nodo_nuevo        
        if self.Tail != None: 
            nodo_nuevo.next = self.head 
            self.head =  nodo_nuevo 
    def Delete(self,dataToDelete):
        node = self.head
        prev = node
        if self.head.dato == dataToDelete: 
            self.head == self.head.next
        else: 
            while node != None:
                if node.dato == dataToDelete:
                    prev.next = node.next
                prev = node
                node = node.next
    def printList(self):
        node = self.head
        while node != None:
            print node.dato
            node = node.next    
