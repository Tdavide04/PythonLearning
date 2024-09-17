'''
Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.

Return the positive integer k. If there is no such integer, return -1.

 

Example 1:

Input: nums = [-1,2,-3,3]
Output: 3
Explanation: 3 is the only valid k we can find in the array.

Example 2:

Input: nums = [-1,10,6,7,-7,1]
Output: 7
Explanation: Both 1 and 7 have their corresponding negative values in the array. 7 has a larger value.

Example 3:

Input: nums = [-10,8,6,7,-2,-3]
Output: -1
Explanation: There is no a single valid k, we return -1.

 

Constraints:

    1 <= nums.length <= 1000
    -1000 <= nums[i] <= 1000
    nums[i] != 0
'''

class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        max_count: int = 0  # Initialize a variable to store the maximum positive integer with its negative counterpart
        nums = list(set(nums))  # Convert the list to a set to remove duplicates, then back to a list
        for i in range(len(nums)):  # Loop through each element in the list
            if -nums[i] in nums:  # Check if the negative counterpart of the current number exists in the list
                if nums[i] > max_count:  # If the current number is greater than the current max_count
                    max_count = nums[i]  # Update max_count with the current number
        return max_count  # Return the maximum positive number found, or 0 if none found


if __name__ == "__main__":

    sos = Solution()
    print(sos.findMaxK([-1,2,-3,3]))