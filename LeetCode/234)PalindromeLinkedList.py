'''
Given the head of a singly linked list, return true if it is a
palindrome
or false otherwise.

 

Example 1:

Input: head = [1,2,2,1]
Output: true

Example 2:

Input: head = [1,2]
Output: false

 

Constraints:

    The number of nodes in the list is in the range [1, 105].
    0 <= Node.val <= 9

 
Follow up: Could you do it in O(n) time and O(1) space?
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        values: list = []  # Create an empty list to store node values
        curr = head  # Set the current pointer to the head of the linked list
        # Traverse the linked list and collect the values of each node
        while curr:
            values.append(curr.val)  # Add the current node's value to the list
            curr = curr.next  # Move to the next node in the list
        # Check if the list is the same as its reverse
        return values == values[::-1]  # If they are equal, the list is a palindrome

if __name__ == "__main__":

    sos = Solution()
    print(sos.isPalindrome(ListNode(1,ListNode(2,ListNode(2,ListNode(1))))))