# add necessary directories to import (change your import directory)
import sys;
# IMPORTANT : Change your import directory else this will not work
sys.path.append('/home/ubuntu/workspace/linkedlist/Node');

from Node.Node_Core import Node

class delete_element_middle_class:
    def __init__(self):
        self.head = None
        self.tail = None
    
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
    
    def remove(self, element):
        print("#Initially setting elementFound as False")
        elementFound = False
        print("#Setting temp head value")
        tempHead = self.head
        while(self.head.next != None):
            if self.head.next.data == element and self.head.next.next == None:
                elementFound = True
                print("#Reached at the last element, just set the tail as current self.head")
                self.tail = self.head
                print("#--- ELEMENT REMOVED ----")
            elif self.head.data == element and self.head.next != None:
                elementFound = True
                print("#Element Found at the starting of the list")
                self.head = self.head.next
                print("#Since element is removed from begining, so setting temphead to updated self.head")
                tempHead = self.head
                print("#--- ELEMENT REMOVED ----")
            elif self.head.data == element and self.head.next == None:
                elementFound = True
                print("#Element found at the starting and no more elements in the list");
                self.head = None
                print("#--- ELEMENT REMOVED ----")
            elif self.head.next.data == element and self.head.next.next != None:
                elementFound = True
                print("#Reached at the middle of the list, element found in the middle of the list")
                self.head.next = self.head.next.next;
                print("#--- ELEMENT REMOVED ----")
            self.head = self.head.next
        if elementFound != True:
            print("#Element Not found !")
        
        print("#Resetting the head element back to original position")
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