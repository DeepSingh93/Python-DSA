class stack_push:
    def __init__(self, max_size):
        self.max_size = max_size
        self.elements = [None] * self.max_size
        self.top = -1
    
    def isFull(self):
        if (self.top + 1) == self.max_size:
            return True
        else:
            return False
    
    def push(self, data):
        if self.isFull() == False:
            self.top = self.top + 1
            self.elements[self.top] = data
            print("Element Added : " + str(self.elements[self.top]))
        else:
            print("Stack Full")
    
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
    
    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            self.elements[self.top] = None
            self.top = self.top - 1
            print("Element poped")
    
    def display(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            getTempTop = self.top
            while(getTempTop != -1):
                print(self.elements[getTempTop])
                getTempTop -= 1
                

stack = stack_push(4)
stack.display()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.display()
stack.pop()
stack.push(5)
stack.display()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()