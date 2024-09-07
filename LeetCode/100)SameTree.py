'''
100. Same Tree
Easy
Topics
Companies
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false
 

Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def preOrder_iterative(root) -> list:
            result: list = []  # Initialize an empty list to store the pre-order traversal
            stack: list = [root]  # Initialize the stack with the root node

            while stack:
                node = stack.pop()  # Pop a node from the stack

                if node:
                    result.append(node.val)  # If the node is not None, append its value to the result list
                    stack.append(node.right)  # Push the right child onto the stack
                    stack.append(node.left)   # Push the left child onto the stack
                else:
                    result.append("null")  # If the node is None, append "null" to the result list

            return result  # Return the list representing the pre-order traversal of the tree

        # Compare the pre-order traversals of both trees
        return preOrder_iterative(p) == preOrder_iterative(q)


        
if __name__ == "__main__":
    
    sos = Solution()
    
    tree1 = TreeNode(1)
    tree1.left = TreeNode(2)
    tree1.right = TreeNode(3)
    tree1.left.left = TreeNode(4)
    tree1.left.right = TreeNode(5)

    # Tree 2 (Same as Tree 1)
    tree2 = TreeNode(1)
    tree2.left = TreeNode(2)
    tree2.right = TreeNode(3)
    tree2.left.left = TreeNode(4)
    tree2.left.right = TreeNode(5)

    # Tree 3 (Different structure)
    tree3 = TreeNode(1)
    tree3.left = TreeNode(2)
    tree3.right = TreeNode(3)
    tree3.left.right = TreeNode(4)

    # Tree 4 (Different structure)
    tree4 = TreeNode(1)
    tree4.left = TreeNode(2)
    tree4.right = TreeNode(2)
    tree4.left.left = TreeNode(3)
    tree4.right.right = TreeNode(3)
    
    print(sos.isSameTree(tree1, tree2))
    print(sos.isSameTree(tree1, tree4))
    print(sos.isSameTree(tree1, tree3))