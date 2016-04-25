# add necessary directories to import (change your import directory)
import sys;
# IMPORTANT : Change your import directory else this will not work
sys.path.append('/home/ubuntu/workspace/linkedlist/Node');

from Node_Core import Node

class delete_element_begining_class:
    def __init__(self):
        self.head = None;
        self.tail = None;
    
    def add(self, data):
        print("creating node object")
        nodeObject = Node(data)
        print("#Checking head");
        if self.head == None:
            print("#Head is none, adding first element");
            self.head = self.tail = nodeObject;
        else:
            print("#Head is not none, adding an element to the end of list")
            self.tail.next = nodeObject;
            self.tail = nodeObject;
        print("#----- ELEMENT SUCCESSFULLY ADDED ELEMENT : "+data+" -----")
    
    def delete(self):
        print("#DELETION OF ELEMENT FROM BEGINING")
        print("#Check whether the head is empty or not")
        if self.head == None:
            print("#List is empty, cannot delete elemnet")
        elif self.head.next == None:
            print("#Only one element in the list, deleting that one element")
            self.head = self.tail = None
            print("----- SUCCESSFULLY DELETED ELEMENT-----")
        else:
            print("#List is not empty, deleting element")
            print("#Setting head position to the next element in the list [from begining]")
            self.head = self.head.next
            print("----- SUCCESSFULLY DELETED ELEMENT-----")
            
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
        