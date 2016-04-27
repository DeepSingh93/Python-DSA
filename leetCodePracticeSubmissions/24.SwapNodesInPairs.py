#Ref link : https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        rtype = []
        getTempHead = head
        count = 0
        if getTempHead != None:
            if getTempHead.next == None:
                rtype.append(getTempHead.val)
            while(getTempHead.next != None):
                tempValue = getTempHead.val
                rtype.append(getTempHead.next.val)
                rtype.append(tempValue)
                getTempHead = getTempHead.next
                if getTempHead.next != None:
                    if getTempHead.next.next == None:
                         rtype.append(getTempHead.next.val)
                    getTempHead = getTempHead.next
        return (rtype) 