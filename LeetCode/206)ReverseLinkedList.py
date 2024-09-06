'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
    
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
    
    head = list_to_linked_list([1, 2, 3, 4, 5])
    reversed_head = sos.reverseList(head)
    print(linked_list_to_list(reversed_head))

    head = list_to_linked_list([1, 2, 3, 4, 6])
    reversed_head = sos.reverseList(head)
    print(linked_list_to_list(reversed_head))


    print(linked_list_to_list(sos.reverseList(list_to_linked_list([4, 2, 3, 4, 5]))))
    
