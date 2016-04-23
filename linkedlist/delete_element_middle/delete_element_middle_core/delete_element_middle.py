# add necessary directories to import (change your import directory)
import sys;
# IMPORTANT : Change your import directory else this will not work
sys.path.append('/home/ubuntu/workspace/linkedlist/Node');

from Node.Node_Core import Node

class delete_element_middle_core_class:
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
            if self.head.next.data == element:
                