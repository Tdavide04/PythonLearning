'''
You are given two integers m and n, which represent the dimensions of a matrix.

You are also given the head of a linked list of integers.

Generate an m x n matrix that contains the integers in the linked list presented in spiral order (clockwise), starting from the top-left of the matrix. If there are remaining empty spaces, fill them with -1.

Return the generated matrix.

 

Example 1:

Input: m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
Output: [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]
Explanation: The diagram above shows how the values are printed in the matrix.
Note that the remaining spaces in the matrix are filled with -1.

Example 2:

Input: m = 1, n = 4, head = [0,1,2]
Output: [[0,1,2,-1]]
Explanation: The diagram above shows how the values are printed from left to right in the matrix.
The last space in the matrix is set to -1.

 

Constraints:

    1 <= m, n <= 105
    1 <= m * n <= 105
    The number of nodes in the list is in the range [1, m * n].
    0 <= Node.val <= 1000
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: ListNode) -> list[list[int]]:
        pass
    
def printMatrix(matrix):
    for row in matrix:
        print(row)

if __name__ == "__main__":

    sos = Solution()

    # Esempio di test con output

    # Test 1: Matrice quadrata
    m = 3
    n = 3
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9)))))))))
    sos = Solution()
    print("Test 1: Matrice quadrata")
    printMatrix(sos.spiralMatrix(m, n, head))

    # Test 2: Matrice rettangolare orizzontale
    m = 2
    n = 4
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8))))))))
    print("Test 2: Matrice rettangolare orizzontale")
    printMatrix(sos.spiralMatrix(m, n, head))

    # Test 3: Lista più corta della matrice
    m = 3
    n = 3
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    print("Test 3: Lista più corta della matrice")
    printMatrix(sos.spiralMatrix(m, n, head))

    # Test 4: Lista più lunga della matrice
    m = 2
    n = 2
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
    print("Test 4: Lista più lunga della matrice")
    printMatrix(sos.spiralMatrix(m, n, head))

    # Test 5: Matrice 1x1
    m = 1
    n = 1
    head = ListNode(1)
    print("Test 5: Matrice 1x1")
    printMatrix(sos.spiralMatrix(m, n, head))

    # Test 6: Matrice vuota
    m = 0
    n = 0
    head = None
    print("Test 6: Matrice vuota")
    printMatrix(sos.spiralMatrix(m, n, head))
