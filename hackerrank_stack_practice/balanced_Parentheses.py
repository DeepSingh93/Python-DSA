#Link : https://www.hackerrank.com/challenges/balanced-parentheses
class stack:
    def __init__(self, __max):
        self.elements = [None] * __max
        self.top = -1
    
    def push(self, __element):
        self.top = self.top + 1
        self.elements[self.top] = __element
    
    def pop(self):
        getPopedElement = self.elements[self.top]
        self.elements[self.top] == None
        self.top = self.top - 1
        return getPopedElement
    
getIterCount = int(input())

for i in range(0, getIterCount):
        perfectBrackets = True
        OStack = stack(1000)
        getInput = input()
        for i in getInput:
            if perfectBrackets:
                if i in ("{","[","("):
                    OStack.push(i)
                else:
                    getPop = OStack.pop()
                    if (getPop == "{" and i == "}") or (getPop == "(" and i == ")") or (getPop == "[" and i == "]") :
                        pass
                    else:
                        perfectBrackets = False
        
        if perfectBrackets and OStack.top == -1:
            print("YES")
        else:
            print("NO")
             
        