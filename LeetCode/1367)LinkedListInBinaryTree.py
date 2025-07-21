'''
Given a binary tree root and a linked list with head as the first node. 

Return True if all the elements in the linked list starting from the head correspond to some downward path connected in the binary tree otherwise return False.

In this context downward path means a path that starts at some node and goes downwards.

 

Example 1:



Input: head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true
Explanation: Nodes in blue form a subpath in the binary Tree.  
Example 2:



Input: head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true
Example 3:

Input: head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: false
Explanation: There is no path in the binary tree that contains all the elements of the linked list from head.
 

Constraints:

The number of nodes in the tree will be in the range [1, 2500].
The number of nodes in the list will be in the range [1, 100].
1 <= Node.val <= 100 for each node in the linked list and binary tree.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        # Helper function to check if a path in the tree matches the linked list from a given node
        def dfs(node, current):
            # If the linked list is fully traversed, return True (we found a path)
            if not current:  
                return True
            # If the tree node is None and we haven't finished the linked list, return False
            if not node:  
                return False
            # If the current tree node value matches the linked list node value
            if node.val == current.val:  
                # Recursively check both left and right children for the next node in the list
                return dfs(node.left, current.next) or dfs(node.right, current.next)
            # If the values don't match, return False
            return False
        
        # Base case: if the tree is empty, no path can exist
        if not root:
            return False
        
        # Check if there's a path from the current node (root) or from its left or right child
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right) or dfs(root, head)

'''
Explanation of Key Points:
dfs Function:

Base cases:
If current (linked list node) is None, it means we've successfully matched the entire list, so we return True.
If node (tree node) is None and we haven't matched the whole list, we return False.
If the value of the tree node matches the value of the current list node, we recursively check both the left and right children for the next node in the list.
If the values don't match, return False because this path is invalid.
isSubPath Function:

This is the main function that will be called recursively.
First, it checks if the root is None—if so, it returns False since there's no tree.
It calls dfs on the current node (root), but it also checks the left and right children in case the match could start from there.
'''
 
if __name__ == "__main__":
    
    sos = Solution()
    
    # Test 1: Linked list exists in the binary tree
    # Binary Tree:
    #       1
    #      / \
    #     4   2
    #        / \
    #       1   3
    # Linked List: 4 -> 2 -> 1
    tree1 = TreeNode(1)
    tree1.left = TreeNode(4)
    tree1.right = TreeNode(2)
    tree1.right.left = TreeNode(1)
    tree1.right.right = TreeNode(3)

    list1 = ListNode(4)
    list1.next = ListNode(2)
    list1.next.next = ListNode(1)

    # Test 2: Linked list does not exist in the binary tree
    # Binary Tree:
    #       1
    #      / \
    #     4   2
    #        / \
    #       1   3
    # Linked List: 4 -> 2 -> 3
    tree2 = TreeNode(1)
    tree2.left = TreeNode(4)
    tree2.right = TreeNode(2)
    tree2.right.left = TreeNode(1)
    tree2.right.right = TreeNode(3)

    list2 = ListNode(4)
    list2.next = ListNode(2)
    list2.next.next = ListNode(3)

    # Test 3: Linked list is empty
    # Binary Tree:
    #       1
    #      / \
    #     2   3
    # Linked List: None
    tree3 = TreeNode(1)
    tree3.left = TreeNode(2)
    tree3.right = TreeNode(3)

    list3 = None

    # Test 4: Binary tree is empty
    # Binary Tree: None
    # Linked List: 1
    tree4 = None

    list4 = ListNode(1)

    # Test 5: Both binary tree and linked list are empty
    # Binary Tree: None
    # Linked List: None
    tree5 = None
    list5 = None

    # Test 6: Linked list matches a path in the binary tree
    # Binary Tree:
    #       1
    #      / \
    #     2   3
    #    /
    #   4
    # Linked List: 1 -> 2 -> 4
    tree6 = TreeNode(1)
    tree6.left = TreeNode(2)
    tree6.right = TreeNode(3)
    tree6.left.left = TreeNode(4)

    list6 = ListNode(1)
    list6.next = ListNode(2)
    list6.next.next = ListNode(4)
    
    print(sos.isSubPath(list1, tree1)) # True
    print(sos.isSubPath(list2, tree2)) # False
    print(sos.isSubPath(list3, tree3)) # True
    print(sos.isSubPath(list4, tree4)) # False
    print(sos.isSubPath(list5, tree5)) # True
    print(sos.isSubPath(list6, tree6)) # True