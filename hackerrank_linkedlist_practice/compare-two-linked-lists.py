#link : https://www.hackerrank.com/challenges/compare-two-linked-lists

"""
 Merge two linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def CompareLists(headA, headB):
    getCountHeadA = 0
    getCountHeadB = 0
    tempHeadA = headA
    tempHeadB = headB
    while(headA != None):
        getCountHeadA += 1
        headA = headA.next
    while(headB != None):
        getCountHeadB += 1
        headB = headB.next
    headA = tempHeadA
    headB = tempHeadB
    if headA == None and headB == None:
        return 0
    elif headA != None and headB != None:
        if getCountHeadA == getCountHeadB:
            headA = tempHeadA
            headB = tempHeadB
            bothEqual = True
            while(headA != None):
                if headA.data != headB.data:
                    bothEqual = False
                headA = headA.next
                headB = headB.next
            if bothEqual == True:
                return 1
            else:
                return 0
        else:
            return 0
    else:
        return 0