# add necessary directories to import (change your import directory)
import sys;
# IMPORTANT : Change your import directory else this will not work
sys.path.append('/home/ubuntu/workspace/linkedlist/delete_element_end');

#import node class
from Node.Node_Core import Node

class delete_element_end_class:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add(self, data):
        print("#Adding data")
        print("#Checking whether head is null or not")
        print("Creating node object")
        nodeObject = Node(data)
        if self.head == None:
            print("Head is null, so adding first element")
            self.head = self.tail = nodeObject
        else:
            print("Head is not null, appending element")
            self.tail.next = nodeObject
            self.tail = nodeObject
            
    
    def removeElementEnd(self):
        print("#--REMOVING LAST ELEMENT--")
        if self.head == None :
            print("#List is empty, cannot remove more elements")
        elif self.head.next == None:
            print("#Only one element in the list, removing that element")
            self.head = self.tail = None
        else:
            print("#Removing the last element from the list")
            print("#Saving the head element in local variable")
            getHead = self.head
            print("#Deleting last element")
            while(self.head != None ):
                if(self.head.next.next == None):
                    self.tail = self.head
                    self.tail.next = None
                self.head = self.head.next
            print("#Node deleted")
            print("#Restoring head position")
            self.head = getHead
    
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
        