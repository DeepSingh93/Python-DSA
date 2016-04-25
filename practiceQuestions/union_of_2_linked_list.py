# Given two Linked Lists, create union lists that contain union
# of the elements present in the given lists. Order of elments
# in output lists doesn’t matter.

# Question given here : http://www.crazyforcode.com/union-intersection-linked-lists/
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add(self, data):
        nodeObject = Node(data)
        if self.head == None:
            self.head = self.tail = nodeObject;
        else:
            self.tail.next = nodeObject;
            self.tail = nodeObject;
    
class unionOf2LinkedList:
    def __init__(self, linkedlist1, linkedlist2):
        self.thirdList = linkedList()
        getFirstListHead = linkedlist1.head
        while(getFirstListHead != None):
            self.thirdList.add(getFirstListHead.data)
            getFirstListHead = getFirstListHead.next
        getFirstListHead = linkedlist1.head
        getSecondListHead = linkedlist2.head
        while(getSecondListHead != None):
            if self.elementExists(linkedlist1, getSecondListHead.data) == False:
                self.thirdList.add(getSecondListHead.data)
            getSecondListHead = getSecondListHead.next
        
    
    def elementExists(self, linkedlist, element):
        getHead = linkedlist.head
        while(getHead != None):
            if getHead.data == element:
                return True
            getHead = getHead.next
        return False

class printList:
    def __init__(self, linkedlist):
        tempHead = linkedlist.head
        while(linkedlist.head != None):
            print(linkedlist.head.data)
            linkedlist.head = linkedlist.head.next
        linkedlist.head = tempHead

linkedlist1 = linkedList()
linkedlist1.add("1")
linkedlist1.add("2")
linkedlist1.add("3")
linkedlist1.add("4")
print("#-- Start of List 1 elements--")
printList(linkedlist1)
print("#-- END of List 1 elements--")
linkedlist2 = linkedList()
linkedlist2.add("4")
linkedlist2.add("5")
linkedlist2.add("6")
linkedlist2.add("7")
print("#-- Start of List 2 elements--")
printList(linkedlist2)
print("#-- END of List 2 elements--")
linkedlistUnion = unionOf2LinkedList(linkedlist1, linkedlist2)
print("#-- Final union of linkedlist")
printList(linkedlistUnion.thirdList)
print("#-- End of union of linkedlist")