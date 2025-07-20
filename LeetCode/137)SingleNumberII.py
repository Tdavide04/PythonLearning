'''
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,3,2]
Output: 3
Example 2:

Input: nums = [0,1,0,1,0,1,99]
Output: 99
 

Constraints:

1 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
Each element in nums appears exactly three times except for one element which appears once.
'''


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        # Initialize an empty dictionary to keep track of the count of each number
        diz: dict = {}
        # Loop through each number in the list `nums`
        for num in nums:
            # Use `get` to retrieve the current count of `num` and default to 0 if it doesn't exist
            diz[num] = diz.get(num, 0) + 1
        # Now loop through the dictionary to find the number that appears exactly once
        for key, values in diz.items():
            # If the value (count) of the key is 1, this is the unique number
            if values == 1:
                return key

    
    

if __name__ == "__main__":
    
    sos = Solution()