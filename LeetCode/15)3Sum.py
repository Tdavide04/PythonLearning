'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
'''

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Sort the array to make it easier to avoid duplicates and use the two-pointer technique
        nums.sort()
        result = []
        # Iterate through the array, treating each element as the potential first element of a triplet. 
        # The length of the range is set to len(nums) - 2 because we need to leave space for at least two more elements to form a valid triplet.
        for i in range(len(nums) - 2):
            # Skip duplicate values for the first element to avoid repeating the same triplet
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Use two pointers to find the other two elements of the triplet
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]: # Skip duplicate values for the second element
                        left += 10
                    while left < right and nums[right] == nums[right - 1]: # Skip duplicate values for the third element
                        right -= 1
                    # Move both pointers inward after finding a valid triplet
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1 # If the total is less than zero, move the left pointer to the right to increase the sum
                else:
                    right -= 1 # If the total is greater than zero, move the right pointer to the left to decrease the sum
        return result


if __name__ == "__main__":
    
    sos = Solution()
    print(sos.threeSum([1,2,-2,-1]))
    
    
