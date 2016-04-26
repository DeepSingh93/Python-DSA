#link : https://www.hackerrank.com/contests/101hack36/challenges/reduced-string
# Shil has a string, SS, consisting of NN lowercase English letters. In one operation, he can delete any pair of adjacent letters with same value. For example, string "aabccaabcc" would become either "aabaab" or "bccbcc" after 11 operation.

# Shil wants to reduce SS as much as possible. To do this, he will repeat the above operation as many times as it can be performed. Help Shil out by finding and printing SS's non-reducible form!

# Note: If the final string is empty, print Empty StringEmpty String.

# Input Format

# A single string, SS.

# Constraints

#     1≤N≤1001≤N≤100

# Output Format

# If the final string is empty, print Empty StringEmpty String; otherwise, print the final non-reducible string.

#--------------- USING LINKEDLIST ONLY -----------------

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
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
    
    def countNodes(self):
        getTempHead = self.head
        count = 0
        while(self.head != None):
            count += 1
            self.head = self.head.next
        self.head = getTempHead
        return count
    
    def replaceElement(self, position):
        pos = 0
        getTempHead = self.head
        while(pos != position):
            self.head = self.head.next
            pos += 1
        self.head.data = "_"
        self.head = getTempHead
     
    def count_nodes(self):
        count = 0
        getTempHead = self.head
        while(self.head != None):
            if self.head.data == "_":
                count += 1
            self.head = self.head.next
        self.head = getTempHead
        return count
        
    def removeDuplicates(self):
        getCount = self.countNodes()
        iteration = 0
        
        while(iteration <= getCount/2):
            getTempHead1 = self.head
            positionTODelete = 0
            if getTempHead1 != None:
                while(getTempHead1.next != None):
                    if getTempHead1.data == getTempHead1.next.data : 
                        self.replaceElement(positionTODelete)
                        self.replaceElement(positionTODelete + 1)
                    positionTODelete += 1
                    getTempHead1 = getTempHead1.next             
            getTempHead1 = None
            getList = self.PrintList()
            self.head = None
            for i in getList :
                if i != "_":
                    self.add(i)
            iteration += 1
    
    def PrintList(self):
        if self.head == None:
            return "Empty String"
        else:
            getTempHead = self.head
            str = ""
            while(self.head != None):
                str += self.head.data
                self.head = self.head.next
            self.head = getTempHead
            return str
        
getInput = input()
linkedListObject = Linkedlist()
for i in getInput:
    linkedListObject.add(i)
linkedListObject.removeDuplicates()
print(linkedListObject.PrintList())
        