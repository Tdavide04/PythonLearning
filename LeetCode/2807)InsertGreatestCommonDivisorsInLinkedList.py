'''
Given the head of a linked list head, in which each node contains an integer value.

Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them.

Return the linked list after insertion.

The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

 

Example 1:

Input: head = [18,6,10,3]
Output: [18,6,6,2,10,1,3]
Explanation: The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after inserting the new nodes (nodes in blue are the inserted nodes).
- We insert the greatest common divisor of 18 and 6 = 6 between the 1st and the 2nd nodes.
- We insert the greatest common divisor of 6 and 10 = 2 between the 2nd and the 3rd nodes.
- We insert the greatest common divisor of 10 and 3 = 1 between the 3rd and the 4th nodes.
There are no more adjacent nodes, so we return the linked list.

Example 2:

Input: head = [7]
Output: [7]
Explanation: The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after inserting the new nodes.
There are no pairs of adjacent nodes, so we return the initial linked list.

 

Constraints:

    The number of nodes in the list is in the range [1, 5000].
    1 <= Node.val <= 1000
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: ListNode) -> ListNode:
        # Helper function to calculate the Greatest Common Divisor (GCD)
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        # Create a new dummy head for the new linked list
        new_head: ListNode = ListNode(0)
        # Pointer to track the current position in the new linked list
        current_new = new_head
        # Pointer to traverse the original linked list
        current = head
        
        # Traverse the linked list, processing nodes pairwise
        while current and current.next:
            # Add the current node from the original list to the new list
            current_new.next = ListNode(current.val)
            current_new = current_new.next
            
            # Add a new node with the GCD between current and next node's values
            current_new.next = ListNode(gcd(current.val, current.next.val))
            current_new = current_new.next
            
            # Move to the next node in the original linked list
            current = current.next
        
        # Add the last node from the original list to the new list
        current_new.next = current
        
        # Return the head of the new linked list (skipping the dummy node)
        return new_head.next

    

def list_to_linked_list(arr):
    if not arr:  # Se la lista è vuota
        return None
    
    head = ListNode(arr[0])  
    current = head  
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next  
    return head  
def linked_list_to_list(head):
    arr = [] 
    current = head 
    while current:
        arr.append(current.val) 
        current = current.next  
    return arr 


if __name__ == "__main__":

    sos = Solution()
    print(sos.insertGreatestCommonDivisors(linked_list_to_list(list_to_linked_list([18,6,10,3]))))