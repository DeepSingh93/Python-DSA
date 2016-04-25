# add necessary directories to import (change your import directory)
import sys;
# IMPORTANT : Change your import directory else this will not work
sys.path.append('/home/ubuntu/workspace/linkedlist/Node');

#import node class
from Node_Core import Node

class insert_after_an_element_class():
    def __init__(self):
        print("#Creating a linked list with empty head and tail")
        self.head = None;
        self.tail = None;
    
    def add(self, data):
        print("#create node object")
        nodeObject = Node(data);
        print("#check head and tail")
        if self.head == None:
            print("#Head is none, adding first element")
            self.head = self.tail = nodeObject
        else:
            print("#Head is not null, appending an element")
            self.tail.next = nodeObject;
            self.tail = nodeObject;
        print("#--- Element added : " + data)
    
    def addElementAfterAnElement(self, afterElement, element):
        dataFound = False;
        getHead = self.head
        print("#Finding element")
        while(self.head != None):
            if self.head.data == afterElement:
                dataFound = True
                print("#Element FOUND !")
                print("#Creating node object")
                nodeObject = Node(element);
                print("#Adding Element")
                tempSelfHeadNext = self.head.next
                self.head.next = nodeObject
                nodeObject.next = tempSelfHeadNext
                print("#--- ELEMENT ADDED ---")
            self.head = self.head.next
        if dataFound == False:
            print("element not found")
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
        
        