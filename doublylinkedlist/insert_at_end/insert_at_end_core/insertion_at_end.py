# add necessary directories to import (change your import directory)
import sys;
# IMPORTANT : Change your import directory else this will not work
sys.path.append('/home/ubuntu/workspace/doublylinkedlist/Node');

from Node_Core import Node

class insert_at_end_doublylinkedlist_class:
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
            
    def printLinkedList(self):
        print("#Getting temp value of head")
        tempHead = self.head
        print("#--- BEGIN PRINTING OF ELEMENTS ---")
        while(self.head != None):
            print(self.head.data)
            self.head = self.head.next
        print("#--- END OF PRINTING OF ELEMENTS ---")
        
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