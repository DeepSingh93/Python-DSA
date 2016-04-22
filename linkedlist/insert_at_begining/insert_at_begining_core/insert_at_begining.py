# add necessary directories to import (change your import directory)
import sys;
# IMPORTANT : Change your import directory else this will not work
sys.path.append('/home/ubuntu/workspace/linkedlist/insert_at_end');

from Node.Node_Core import Node

class insert_at_begining_class:
    def __init__(self):
        print("#This program will insert nodes in the begining.")
        self.head = None
        self.tail = None
        
    def add(self, data):
        print("#--BEGIN INSERTING DATA AT BEGINING--")
        
        print("#Creating node object")
        nodeObject = Node(data)
        
        print("#Checking head position")
        tempHead = self.head
        
        if self.head == None:
            print("#Head is null, so adding first element")
            self.head = self.tail = nodeObject
        else:
            print("#Head is not null, adding the nodeobject in the starting")
            nodeObject.next = self.head
            self.head = nodeObject
            
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