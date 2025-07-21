'''
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
'''

class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        
        left: int = 0
        max_len: int = 0
        zeros: int = 0
        
        # Edge case: If there are no zeros in the array, the result should be len(nums) - 1
        # because we need to delete one element.
        if 0 not in nums:
            return len(nums) -1
        
        for right in range(len(nums)):
            if nums[right] == 0: # If the current element is a zero, increment the zero count.
                zeros += 1
                
            # If there is more than one zero in the current window,
            # shrink the window from the left until there is only one zero.    
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
                
            # Update max_len with the length of the current valid window.
            # Subtract 1 from right - left because we must delete one element.
            max_len = max(max_len, right - left)
            
        return max_len
            
    
if __name__ == "__main__":
    
    sos = Solution()
    print(sos.longestSubarray(nums = [1,1,0,1]))
    print(sos.longestSubarray(nums = [0,1,1,1,0,1,1,0,1]))
    print(sos.longestSubarray(nums = [1,1,1]))
    
    
'''
Explanation:
Window Expansion: We use right to expand the window.
Window Contraction: When more than one zero is encountered, we shrink the window from the left by moving left.
Length Calculation: The length of the window is calculated by right - left, which gives us the number of 1's (considering that we must delete one zero).
Example Walkthrough:
For the input [0, 1, 1, 1, 0, 1, 1, 0, 1]:

The optimal subarray is [1, 1, 1, 0, 1, 1], where we can remove one 0 to get a subarray of length 5 of consecutive 1s.
The code correctly calculates this by using the sliding window technique.
'''