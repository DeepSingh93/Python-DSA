# link : https://www.hackerrank.com/challenges/maximum-element/
# ---- IMPORTANT : TEST CASE 13,14,15 TERMINATED DUE TO TIMEOUT ----

class stack:
    def __init__(self, max_elements):
        self.top = -1
        self.elements = [-1]*max_elements
        self.max_elements = max_elements
        self.maximum = -1
    
    def push(self, element):
        self.top += 1
        self.elements[self.top] = element
        if element > self.maximum:
            self.maximum = element
    
    def pop(self):
        getTempTop = self.top
        self.top = self.top - 1
        if self.elements[getTempTop] == self.maximum:
            self.elements[getTempTop] = -1
            self.maximum = max(self.elements)
        self.elements[getTempTop] = -1
        

getTotalIter = int(input())
tStack = stack(getTotalIter)
for i in range(0, getTotalIter):
    inputElements = input()
    getChoice = int(inputElements.split(' ')[0])
    if getChoice == 1:
        tStack.push(int(inputElements.split(' ')[1]))
    if getChoice == 2:
        tStack.pop()
    if getChoice == 3:
        print(tStack.maximum)
        