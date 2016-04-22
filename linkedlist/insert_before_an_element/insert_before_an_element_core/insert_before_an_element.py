# add necessary directories to import (change your import directory)
import sys;
# IMPORTANT : Change your import directory else this will not work
sys.path.append('/home/ubuntu/workspace/linkedlist/insert_at_end');

from Node.Node_Core import Node

class insert_before_an_element_class:
    def __init__(self):
        self.head = None;
        self.tail = None;
    
    def add(self, data):
        print("#Begin addition of element")
        print("#Creating node object")
        nodeObject = Node(data)
        print("#Check whether head is null or not")
        if(self.head == None):
            print("#Head is null, adding first element")
            self.head = self.tail = nodeObject
        else:
            print("#Head is not null, appending element")
            self.tail.next = nodeObject
            self.tail = nodeObject
        print("#Finish addition of element")
    
    def addBefore(self, elementBefore, element):
        print("#Initially keeping elementFound = False")
        elementFound = False
        print("Save the head position")
        tempHead = self.head
        while(self.head.next != None):
            if self.head.next.data == elementBefore :
                
                elementFound = True
                print("#Getting current element position")
                getCurrElement = self.head
                print("#Getting next head position")
                getnextElement = self.head.next
                print("#Creating node object")
                nodeObject = Node(element)
                
                self.head.next = nodeObject
                nodeObject.next = getnextElement
                
                self.head = nodeObject.next
                
            self.head = self.head.next
        if elementFound == False:
            print("Element Not Found")
        self.head = tempHead
    
    def printLinkedList(self):
        print("#---- Start of printing of linkedlist ----")
        print("#Getting head position")
        getHead = self.head;
        if(self.head == None):
            print("#List is empty")
        else:
            while(getHead != None):
                print(getHead.data)
                getHead = getHead.next
        print("#---- End of printing of linkedlist ----")
        