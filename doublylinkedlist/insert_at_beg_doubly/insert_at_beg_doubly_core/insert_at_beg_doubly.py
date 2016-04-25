# add necessary directories to import (change your import directory)
import sys;
# IMPORTANT : Change your import directory else this will not work
sys.path.append('/home/ubuntu/workspace/doublylinkedlist/Node');

from Node_Core import Node

class insert_at_beg_doubly_class:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add(self, element):
        print("#--- Begin insertion at begining")
        print("#Creating node object")
        nodeObject = Node(element)
        print("#Check if first element or not")
        if self.head == None:
            print("#It's the first element")
            self.head = self.tail = nodeObject
            print("#Element Added")
        else:
            print("#It's not the first element, adding the element")
            self.head.previous = nodeObject
            nodeObject.next = self.head
            self.head = nodeObject
    
    def printLinkedList(self):
        print("#Getting temp value of head")
        tempHead = self.head
        print("#--- BEGIN PRINTING OF ELEMENTS ---")
        while(self.head != None):
            print(self.head.data)
            self.head = self.head.next
        print("#--- END OF PRINTING OF ELEMENTS ---")
        self.head = tempHead
    
    def printBothSides(self):
        print("Printing both prev and next values for the current node")
        print("#--- Begin printing of elements of previous and next values ---")
        while(self.head != None):
            previousValue = "Null"
            nextValue = "Null"
            if self.head.previous != None:
                previousValue = self.head.previous.data
            if self.head.next != None:
                nextValue = self.head.next.data
            print("Current node ==> " + self.head.data + " ,Previous Value : " + previousValue + " ,Next value : " + nextValue)
            self.head = self.head.next
        print("#--- END printing of elements of previous and next values ---")