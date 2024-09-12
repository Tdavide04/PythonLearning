'''
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

Example 1:

Input: head = [1,1,2]
Output: [1,2]

Example 2:

Input: head = [1,1,2,3,3]
Output: [1,2,3]

 

Constraints:

    The number of nodes in the list is in the range [0, 300].
    -100 <= Node.val <= 100
    The list is guaranteed to be sorted in ascending order.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        values: list[int] = []
        dummy: ListNode = ListNode(0)
        current = head
        while current:
            if current.val not in values:
                values.append(current.val)
                dummy.next = current
            current = current.next
        return dummy.next


if __name__ == "__main__":

    sos = Solution()
    print(sos.deleteDuplicates(ListNode(1, ListNode(1, ListNode(2)))))