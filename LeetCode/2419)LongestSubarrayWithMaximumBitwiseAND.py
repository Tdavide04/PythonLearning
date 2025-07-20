'''
You are given an integer array nums of size n.

Consider a non-empty subarray from nums that has the maximum possible bitwise AND.

In other words, let k be the maximum value of the bitwise AND of any subarray of nums. Then, only subarrays with a bitwise AND equal to k should be considered.
Return the length of the longest such subarray.

The bitwise AND of an array is the bitwise AND of all the numbers in it.

A subarray is a contiguous sequence of elements within an array.

 

Example 1:

Input: nums = [1,2,3,3,2,2]
Output: 2
Explanation:
The maximum possible bitwise AND of a subarray is 3.
The longest subarray with that value is [3,3], so we return 2.
Example 2:

Input: nums = [1,2,3,4]
Output: 1
Explanation:
The maximum possible bitwise AND of a subarray is 4.
The longest subarray with that value is [4], so we return 1.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 106
'''

class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        # Find the maximum value in the array
        max_value = max(nums)
        
        # Variables to keep track of the maximum length and current length
        max_len = 0  # Longest subarray length of contiguous elements equal to max_value
        current_len = 0  # Current subarray length being tracked
        
        # Iterate through the array
        for num in nums:
            if num == max_value:
                # If the current number is equal to the max value, increase the current subarray length
                current_len += 1  
            else:
                # Otherwise, update the max length if the current subarray is longer
                max_len = max(max_len, current_len)
                # Reset the current subarray length since the sequence broke
                current_len = 0
        
        # After the loop, ensure the last subarray is considered
        max_len = max(max_len, current_len)
        
        # Return the maximum length of contiguous subarray with elements equal to max_value
        return max_len


if __name__ == "__main__":
    
    sos = Solution()