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
        print("~~~~~~~ BEGIN OF REMOVING AN ELEMENT FROM LINKEDLIST ~~~~~~~")
        print("#Initially setting elementFound as False")
        elementFound = False
        print("#Setting temp head value")
        tempHead = self.head
        print("#Checking whether it's the first element or not")
        if self.head.data == element:
            elementFound = True
            print("#Yes it's the first element")
            print("#Now checking whether there exists an element after first element")
            if self.head.next == None:
                print("#No element after first element, so removing this element, by setting self.head == None")
                self.head = None
                print("#---ELEMENT REMOVED---")
                print("#Updating the temp value of self.head")
                tempHead = self.head
            else:
                print("#Yes it contains more elements after first element")
                print("#Removing the first element from the list")
                self.head = self.head.next
                print("#Updating the temp value of self.head")
                tempHead = self.head
                print("#---ELEMENT REMOVED---")
        elif self.tail.data == element:
            print("#It's the last element !")
            while(self.head.next != None):
                if self.head.next.data == element:
                    elementFound = True
                    print("#Element found at the last position")
                    self.tail = self.head
                    self.head.next = None
                else:
                    self.head = self.head.next
        else:
            print("#No it's not the first element neither the last element, searching for element ! Traversing the linkedlist")
            while(self.head != None):
                if self.head.data == element:
                    elementFound = True
                    print("#This is not the last element ! Updating the element position")
                    self.head.data = self.head.next.data
                    self.head.next = self.head.next.next
                    print("#---ELEMENT REMOVED---")
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