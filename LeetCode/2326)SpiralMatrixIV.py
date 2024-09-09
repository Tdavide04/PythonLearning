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
        # Directions: right, down, left, up
        # (0,1): move right; (1,0): move down; (0,-1): move left; (-1,0): move up
        direction: list = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # Create an empty m x n matrix initialized with -1
        result: list[list[int]] = [[-1] * n for _ in range(m)]
        # Initialize starting position at the top-left corner of the matrix
        x, y = 0, 0
        # Variable to keep track of the current direction (0=right, 1=down, 2=left, 3=up)
        direction_index: int = 0
        # Total number of cells to fill
        total_cells: int = m * n
        # Counter to track how many cells have been filled so far
        filled_cells: int = 0
        # Iterate until all cells are filled
        while filled_cells < total_cells:
            # If the linked list is not exhausted, assign the current node value to the matrix
            if head:
                result[x][y] = head.val  # Insert the value from the linked list node
                head = head.next  # Move to the next node in the linked list
            else:
                result[x][y] = -1  # If the linked list is finished, fill with -1
            # Increment the count of filled cells
            filled_cells += 1
            # Calculate the next position to move to based on the current direction
            new_x = x + direction[direction_index][0]
            new_y = y + direction[direction_index][1]
            # If the next position is out of bounds or already filled, change direction
            if not (0 <= new_x < m and 0 <= new_y < n and result[new_x][new_y] == -1):
                # Update direction index to the next direction (right -> down -> left -> up)
                direction_index = (direction_index + 1) % 4
                # Recalculate the next position with the updated direction
                new_x = x + direction[direction_index][0]
                new_y = y + direction[direction_index][1]
            # Update the current position to the next valid position
            x, y = new_x, new_y
        return result

if __name__ == "__main__":

    sos = Solution()

    # Esempio di test con output

    # Test 1: Matrice quadrata
    m = 3
    n = 3
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9)))))))))
    sos = Solution()
    print(sos.spiralMatrix(m, n, head))

    # Test 2: Matrice rettangolare orizzontale
    m = 2
    n = 4
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8))))))))
    print(sos.spiralMatrix(m, n, head))

    # Test 3: Lista più corta della matrice
    m = 3
    n = 3
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    print(sos.spiralMatrix(m, n, head))

    # Test 4: Lista più lunga della matrice
    m = 2
    n = 2
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
    print(sos.spiralMatrix(m, n, head))

    # Test 5: Matrice 1x1
    m = 1
    n = 1
    head = ListNode(1)
    print(sos.spiralMatrix(m, n, head))

    # Test 6: Matrice vuota
    m = 0
    n = 0
    head = None
    print(sos.spiralMatrix(m, n, head))
