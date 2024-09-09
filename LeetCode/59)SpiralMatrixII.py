'''
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 

Example 1:

Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:

Input: n = 1
Output: [[1]]

 

Constraints:

    1 <= n <= 20
'''

class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        # Define directions for moving: right, down, left, and up.
        # Each tuple represents a movement (dx, dy) where dx is the change in x (row) and dy is the change in y (column).
        direction: list = [(0,1), (1,0), (0,-1), (-1,0)]
        
        # Create an n x n matrix initialized with 0. This will store the spiral numbers.
        result: list[list[int]] = [[0]*n for _ in range(n)]
        
        # Initialize starting position at the top-left corner of the matrix.
        x, y = 0, 0
        
        # Keep track of the current direction we are moving in. Start by moving right (index 0 in the direction list).
        direction_index: int = 0
        
        # The number to be inserted into the matrix starts from 1.
        num: int = 0
        
        # Continue filling the matrix until all n*n positions are filled.
        while num < n*n:
            # Only place a number if the current cell hasn't been filled yet (i.e., if it's 0).
            if result[x][y] == 0:
                num += 1  # Increment the number to be placed.
                result[x][y] = num  # Place the number in the current cell.
            
            # Calculate the next position based on the current direction.
            new_x = x + direction[direction_index][0]  # Change in row (x-coordinate).
            new_y = y + direction[direction_index][1]  # Change in column (y-coordinate).
            
            # Check if the new position is valid: it must be within bounds and the target cell must be unfilled (i.e., still 0).
            if 0 <= new_x < n and 0 <= new_y < n and result[new_x][new_y] == 0:
                # If the position is valid, update x and y to the new coordinates.
                x, y = new_x, new_y
            else:
                # If the position is not valid (either out of bounds or the cell is already filled),
                # change the direction by rotating clockwise (move to the next direction in the list).
                direction_index = (direction_index + 1) % 4  # Ensure the direction index cycles between 0 and 3.
        return result

if __name__ == "__main__":

    sos = Solution()
    print(sos.generateMatrix())