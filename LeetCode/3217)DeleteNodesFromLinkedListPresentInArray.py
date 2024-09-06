'''
You are given an array of integers nums and the head of a linked list. Return the head of the modified linked list after removing all nodes from the linked list that have a value that exists in nums.

 

Example 1:

Input: nums = [1,2,3], head = [1,2,3,4,5]

Output: [4,5]

Explanation:

Remove the nodes with values 1, 2, and 3.

Example 2:

Input: nums = [1], head = [1,2,1,2,1,2]

Output: [2,2,2]

Explanation:

Remove the nodes with value 1.

Example 3:

Input: nums = [5], head = [1,2,3,4]

Output: [1,2,3,4]

Explanation:

No node has value 5.

 

Constraints:

    1 <= nums.length <= 105
    1 <= nums[i] <= 105
    All elements in nums are unique.
    The number of nodes in the given list is in the range [1, 105].
    1 <= Node.val <= 105
    The input is generated such that there is at least one node in the linked list that has a value not present in nums.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def modifiedList(self, nums: list[int], head: ListNode) -> ListNode:
        nums = set(nums)
        pippo = ListNode(0)
        pippo.next = head
        current_node = pippo
        while current_node.next:
            if current_node.next.val in nums:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
        return pippo.next


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
    print(linked_list_to_list(sos.modifiedList([1,2,3], list_to_linked_list([1,2,3,4,5,6]))))