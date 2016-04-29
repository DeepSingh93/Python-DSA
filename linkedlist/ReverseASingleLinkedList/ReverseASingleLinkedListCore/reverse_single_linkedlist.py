# add necessary directories to import (change your import directory)
import sys;
# IMPORTANT : Change your import directory else this will not work
sys.path.append('/home/ubuntu/workspace/linkedlist/Node');

from Node_Core import Node

class reverse_linkedlist:
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
    
    def reverse(self):
        print("#--- Begin Reversal Of Linked List ---")
        getTemp  = self.head
        if self.head != None:
            finalList = Node(self.head.data)
            self.head = self.head.next
            while(self.head != None):
                tempListNode = Node(self.head.data)
                tempListNode.next = finalList
                finalList = tempListNode
                self.head = self.head.next
        self.head = finalList
        print("#--- End Reversal Of Linked List ---")
  
    
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