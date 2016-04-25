# Link : https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list
"""
 Delete Node at a given position in a linked list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""

def Delete(head, position):
    if position == 0:
        return head.next
    else:
        tempHead = head
        for pos in range(1, position):
            head = head.next
        if head.next.next == None:
            #This is the last element
            head.next = None
        else:
            #Not the last element
            head.next.data = head.next.next.data
            head.next = head.next.next
        return tempHead
