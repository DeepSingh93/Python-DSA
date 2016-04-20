# creation of linkedlist and adding data to the linkedlist
# creating class Node and linkedlist
from Node.Node_Class import Node
class linkedlist_insert_in_end:
    def __init__(self):
        self.head = None;
        self.tail = None;
    
    def add(self, data):
        newnode = Node(data);
        if self.head == None:
            self.head = self.tail = newnode;
        else:
            self.tail.next = newnode;
            self.tail = self.tail.next;
    
    def showdata(self):
        getHead = self.head;
        while(getHead != None):
            print(getHead.data);
            getHead = getHead.next;

