'''
Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.

The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.

The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.

Return an array of the k parts.

 

Example 1:


Input: head = [1,2,3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but its string representation as a ListNode is [].
Example 2:


Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
Output: [[1,2,3,4],[5,6,7],[8,9,10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.
 

Constraints:

The number of nodes in the list is in the range [0, 1000].
0 <= Node.val <= 1000
1 <= k <= 50
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> list[ListNode]:
        # Determine the total length of the linked list
        length: int = 0
        current: ListNode = head
        while current: # Traverse the entire linked list to count its length
            length += 1
            current = current.next
        
        # Calculate the size of each part and the number of extra nodes
        part_size: int = length // k  # Each part should have this many nodes
        extra: int = length % k      # These many extra nodes need to be distributed
        
        # Initialize the result list which will contain the heads of the split parts
        result: list[ListNode] = []
        current: ListNode = head
        
        # Split the list into k parts
        for i in range(k):
            new_head = current # Start of the current part
            size = part_size # Determine the size of the current part
            if extra > 0:
                size += 1  # If there are extra nodes, increase the size of this part by 1
                extra -= 1  # Decrement the count of extra nodes
            
            # Traverse to the end of the current part
            for j in range(size - 1):
                if current:
                    current = current.next
            
            # Disconnect the current part from the rest of the list
            if current:
                next_part = current.next  # Save the next part of the list
                current.next = None  # End the current part by setting the next pointer to None
                current = next_part  # Move to the next part of the list
            
            # Append the current part (head) to the result list
            result.append(new_head)
        
        # If there are fewer parts than k, append None to the result list
        while len(result) < k:
            result.append(None)
        
        return result

        

    

if __name__ == "__main__":
    sos = Solution()
    print(sos.splitListToParts([1, 2, 3], 5))
    