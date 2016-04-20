# creation of linkedlist and adding data to the linkedlist
# creating class Node and linkedlist
class Node:
    def __init__(self, data):
        self.data = data;
        self.next = None;
        
class linkedlist:
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

list1 = linkedlist();
list1.add('sample1');
list1.add('sample2');
list1.add('sample3');
list1.add('sample4');
list1.showdata();