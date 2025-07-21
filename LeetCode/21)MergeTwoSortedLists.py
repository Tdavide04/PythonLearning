'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

 

Constraints:

    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both list1 and list2 are sorted in non-decreasing order.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Create a dummy node to serve as the head of the merged list
        list3: ListNode = ListNode(0)
        
        # Initialize pointers to traverse both input lists (list1 and list2)
        current1 = list1
        current2 = list2
        
        # Pointer to build the new merged list starting from the dummy node
        current3 = list3
        
        # Loop while both lists have elements to compare
        while current1 and current2:
            # Compare the values from both lists, attach the smaller node to the new list
            if current1.val < current2.val:
                current3.next = current1  # Attach current1 node to merged list
                current1 = current1.next  # Move current1 pointer to the next node
            else:
                current3.next = current2  # Attach current2 node to merged list
                current2 = current2.next  # Move current2 pointer to the next node
                
            # Move the merged list pointer forward
            current3 = current3.next

        # If one of the lists still has elements left, attach the remainder
        if current1:
            current3.next = current1
        if current2:
            current3.next = current2

        # Return the merged list, skipping the dummy node
        return list3.next
