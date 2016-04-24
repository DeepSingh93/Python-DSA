# add necessary directories to import (change your import directory)
import sys;
# IMPORTANT : Change your import directory else this will not work
sys.path.append('/home/ubuntu/workspace/doublylinkedlist/Node');

from Node_Core import Node

class reverse_traversal_doublylinkedlist_class:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add(self,element):
        print("#Begin Insertion of element using doubly linkedlist")
        print("#Creating node object")
        nodeObject = Node(element)
        print("#Check whether it's the first element or not")
        if self.head == None:
            print("#It's the first element")
            self.head = self.tail = nodeObject
            print("#ELEMENT ADDED SUCCESSFULLY")
        else:
            print("#Its not the first element")
            print("#Adding element")
            print("#Get the tail and save it in temp var")
            tempTail = self.tail
            print("#Now update the tail element with previous and next")
            nodeObject.previous = self.tail
            self.tail.next = nodeObject
            self.tail = nodeObject
            print("#ELEMENT ADDED SUCCESSFULLY")
    
    def printReverseLinkedList(self):
        print("#Setting temp value to self.tail")
        tempTail = self.tail
        print("#-- Start of printing of reverse linkedlist")
        while(self.tail != None):
            print(self.tail.data)
            self.tail = self.tail.previous
        print("#-- End of printing of linkedlsit")
        print("#Setting tail value back")
        self.tail = tempTail