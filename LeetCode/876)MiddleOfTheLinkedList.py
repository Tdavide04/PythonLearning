'''
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 

Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        array: list = []
        
        while head:
            array.append(head.val)
            head = head.next
            
        middle_index: int = len(array) // 2
        result = ListNode(array[middle_index])
        current = result
        for val in array[middle_index + 1:]:
            current.next = ListNode(val)
            current = current.next
        return result
        
# Converte una lista Python in una linked list
def list_to_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Converte una linked list in una lista Python
def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result  
    
if __name__ == "__main__":
    
    sos = Solution()
    
    print(linked_list_to_list(sos.middleNode(list_to_linked_list([4, 2, 3, 4, 5]))))   