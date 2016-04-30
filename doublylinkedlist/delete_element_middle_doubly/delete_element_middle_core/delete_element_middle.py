# add necessary directories to import (change your import directory)
import sys;
# IMPORTANT : Change your import directory else this will not work
sys.path.append('/home/ubuntu/workspace/doublylinkedlist/Node');

from Node_Core import Node

class delete_element_middle_class:
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
        self.head = tempHead
    
    def printBothSides(self):
        print("Printing both prev and next values for the current node")
        print("#--- Begin printing of elements of previous and next values ---")
        getTemp = self.head
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
        self.head = getTemp
    
    def delete_element_middle(self, data):
        print("#--- Start of deleting elements, deleting element : " + str(data))
        getTempHead = self.head 
        elementFound = False
        if self.head.data == data:
            elementFound = True
            print("#This is the first element")
            print("#Checking if there are any more elemnts after this")
            if self.head.next == None:
                print("#There is only one element in the list, so removing that element")
                self.head = None
            else:
                print("#There are more than one elements in the list, so removing only the first element")
                self.head = self.head.next
        else:
            print("#This is not the first element, checking for more elements")
            while(self.head != None):
                if self.head.data == data:
                    elementFound = True
                    print("#Element found, checking if it's last element or not")
                    if self.tail.data == data:
                        print("#This is the last element")
                        getTempTail = self.tail.previous
                        self.tail.previous.next = None
                        self.tail.previous = None
                        self.tail = getTempTail
                        break
                    else:
                        elementFound = True
                        print("#This is the middle element")
                        tempPreviousPointer = self.head.previous
                        tempNextPointer = self.head.next
                        self.head.previous.next = tempNextPointer
                        self.head.next.previous = tempPreviousPointer
                        self.head = self.head.previous
                self.head = self.head.next
            self.head = getTempHead
        print("#--- End of deleting elements")
        if elementFound == False:
            print("#=== ELEMENT NOT FOUND ===")
                