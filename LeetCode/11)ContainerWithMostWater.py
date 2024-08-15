'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
'''

class Solution:
    def maxArea(self, height: list[int]) -> int:
        # Initialize two pointers: one at the start (left_pointer) and one at the end (right_pointer) of the list
        left_pointer = 0
        right_pointer = len(height) -1
        max_area = 0
        while left_pointer < right_pointer:
            
            width = right_pointer - left_pointer
            # Using min() ensures that we are calculating the area correctly, because the water cannot go above the lowest line.
            current_area = min(height[left_pointer], height[right_pointer]) * width
            max_area = max(current_area, max_area)
            # Move the pointer that has the smaller height to try and find a larger area
            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1

        return max_area
            
        
    

if __name__ == "__main__":
    
    sos = Solution()
    print(sos.maxArea(height = [1,2,1]))