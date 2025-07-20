'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # If the root node is None, the tree is empty and the depth is 0
        if not root:
            return 0
        
        # Initialize a stack for iterative DFS.
        # Each element in the stack is a tuple (node, depth)
        stack: list = [(root, 1)]
        
        # Variable to keep track of the maximum depth found
        max_depth: int = 0
        
        # Loop while there are nodes in the stack
        while stack:
            # Pop the last node and its depth from the stack
            node, depth = stack.pop()
            
            # Update the maximum depth if necessary
            max_depth = max(max_depth, depth)
            
            # If the current node has a left child, add it to the stack
            # with the depth incremented by 1
            if node.left:
                stack.append((node.left, depth + 1))
            
            # If the current node has a right child, add it to the stack
            # with the depth incremented by 1
            if node.right:
                stack.append((node.right, depth + 1))
        
        return max_depth


        
        
        
    
if __name__ == "__main__":
    
    sos = Solution()
    
    tree1 = TreeNode(1)  
    tree2 = TreeNode(1, TreeNode(2))  
    tree3 = TreeNode(1, TreeNode(2, TreeNode(3)))  

    print("Depth of tree1:", sos.maxDepth(tree1))  # Output: 1
    print("Depth of tree2:", sos.maxDepth(tree2))  # Output: 2
    print("Depth of tree3:", sos.maxDepth(tree3))  # Output: 3