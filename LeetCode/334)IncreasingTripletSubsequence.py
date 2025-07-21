'''
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
 

Constraints:

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?
'''

class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        
        # Initialize 'first' and 'second' with a large value, using the sum of all elements in nums plus the lenght of the list.
        # This ensures that any element in nums will be smaller initially and can update 'first' or 'second'.
        first = sum(nums) + len(nums)
        second = sum(nums) + len(nums)
        for i in nums:
            if i < first: # If the current element is smaller than 'first', update 'first' to this element.
                first = i
            elif i > first and i < second: # If the current element is larger than 'first' but smaller than 'second', update 'second'.
                second = i
            elif i > second: # If the current element is larger than 'second', it means we've found a valid increasing triplet.
                return True
        return False
                
            
    
if __name__ == "__main__":
    
    sos = Solution()
    print(sos.increasingTriplet(nums = [6,7,1,2])) # False
    print(sos.increasingTriplet(nums = [2,1,5,0,4,6])) # True
    print(sos.increasingTriplet(nums = [5,4,3,2,1])) # False
    print(sos.increasingTriplet(nums = [1,5,0,4,1,3])) # True
    print(sos.increasingTriplet(nums = [20,100,10,12,5,13])) # True
    print(sos.increasingTriplet(nums = [1])) # False
    print(sos.increasingTriplet(nums = [0,4,2,1,0,-1,-3])) # False
    print(sos.increasingTriplet(nums = [5,0,6])) # False
