#Link : https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        getCountL1 = 0
        getCountL2 = 0
        
        getTempL1 = l1
        getTempL2 = l2
        
        while(getTempL1 != None):
            getCountL1 += 1
            getTempL1 = getTempL1.next
        
        while(getTempL2 != None):
            getCountL2 += 1
            getTempL2 = getTempL2.next
        
        getTempL1 = l1
        getTempL2 = l2
        
        rtypeList = []
        
        if getCountL1 > getCountL2:
            carryOver = 0
            sum = 0
            while(getTempL2 != None):
                sum = getTempL1.val + getTempL2.val + carryOver
                
                if sum > 9:
                    carryOver = 1
                    sum = (int(str(sum)[1]))
                else:
                    carryOver = 0
                    
                rtypeList.append(sum)
                
                getTempL1 = getTempL1.next
                getTempL2 = getTempL2.next
            
            while(getTempL1 != None):
                sum = getTempL1.val + carryOver
                
                if sum > 9:
                    carryOver = 1
                    sum = (int(str(sum)[1]))
                else:
                    carryOver = 0
                
                rtypeList.append(sum)
                getTempL1 = getTempL1.next
            
            if carryOver == 1:
                rtypeList.append(carryOver)
                carryOver = 0
                
        elif getCountL1 < getCountL2:
            carryOver = 0
            sum = 0
            while(getTempL1 != None):
                sum = getTempL1.val + getTempL2.val + carryOver
                
                if sum > 9:
                    carryOver = 1
                    sum = (int(str(sum)[1]))
                else:
                    carryOver = 0
                    
                rtypeList.append(sum)
                
                getTempL1 = getTempL1.next
                getTempL2 = getTempL2.next
            
            while(getTempL2 != None):
                sum = getTempL2.val + carryOver
                
                if sum > 9:
                    carryOver = 1
                    sum = (int(str(sum)[1]))
                else:
                    carryOver = 0
                
                rtypeList.append(sum)
                getTempL2 = getTempL2.next
            
            if carryOver == 1:
                rtypeList.append(carryOver)
                carryOver = 0
        else:
            carryOver = 0
            sum = 0
            while(getTempL2 != None):
                sum = getTempL1.val + getTempL2.val + carryOver
                
                if sum > 9:
                    carryOver = 1
                    sum = (int(str(sum)[1]))
                else:
                    carryOver = 0
                    
                rtypeList.append(sum)
                
                getTempL1 = getTempL1.next
                getTempL2 = getTempL2.next
            
            if carryOver > 0:
                rtypeList.append(carryOver)
            
        return rtypeList
            
        