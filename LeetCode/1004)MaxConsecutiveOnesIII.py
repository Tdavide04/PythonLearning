'''
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
'''

class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left: int = 0  # Initialize the left pointer of the sliding window
        zeros: int = 0  # Counter to track the number of zeros in the current window
        max_len: int = 0  # Variable to store the maximum length of a valid subarray
        
        for right in range(len(nums)): # Iterate through the array using the right pointer
            if nums[right] == 0: # If the current element is a zero, increment the zero counter
                zeros += 1
            
            while zeros > k: # If the number of zeros exceeds k, shrink the window from the left
                if nums[left] == 0: # If the element at the left pointer is a zero, decrement the zero counter
                    zeros -= 1
                left += 1 # Move the left pointer to the right to reduce the window size
            max_len = max(max_len, right - left + 1) # Calculate the length of the current valid window and update max_len
            
        return max_len

if __name__ == "__main__":
    
    sos = Solution()
    print(sos.longestOnes(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2))