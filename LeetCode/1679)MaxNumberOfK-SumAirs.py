'''
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

 

Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= 109
'''


class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        
        nums.sort() # Sort the list 'nums' to make it easier to find pairs that sum to 'k'.
        counter: int = 0
        # Initialize two pointers: 'left' starting at the beginning, and 'right' at the end of the list.
        left: int = 0
        right: int = len(nums) - 1
        while left < right: # Use a while loop to find pairs until the two pointers meet.
            if nums[left] + nums[right] == k: # If the sum of the elements at 'left' and 'right' equals 'k', a valid pair is found.
                counter += 1  # Increment the counter for a valid pair.
                left += 1 # Move the 'left' pointer to the right to check the next element.
                right -= 1 # Move the 'right' pointer to the left to check the next element.
            # If the sum is less than 'k', move the 'left' pointer to the right to increase the sum.
            elif nums[left] + nums[right] < k:
                left += 1
            # If the sum is greater than 'k', move the 'right' pointer to the left to decrease the sum.
            elif nums[left] + nums[right] > k:
                right -= 1
        return counter

    
if __name__ == "__main__":
    
    sos = Solution()
    print(sos.maxOperations(nums = [3,1,3,4,3], k = 6)) # Output: 1