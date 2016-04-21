# add necessary directories to import (change your import directory)
import sys;
# IMPORTANT : Change your import directory else this will not work
sys.path.append('/home/ubuntu/workspace/linkedlist/insert_at_end');

#import node class
from Node.Node_Core import Node

class insert_at_end:
    def __init__(self):
        print("#created empty linked list")
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
    
    def printLinkedList(self):
        print("#Get head position and save it in local variable");
        getHead = self.head;
        print("#--- START OF PRINTING OF LINKEDLIST ---")
        while(getHead != None):
            print(getHead.data)
            getHead = getHead.next;
        print("#--- END OF PRINTING OF LINKEDLIST ---")
        
