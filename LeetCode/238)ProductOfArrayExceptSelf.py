'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
'''

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
       pass
            
    
if __name__ == "__main__":
    
    sos = Solution()
    print(sos.productExceptSelf(nums = [1,2,3,4]))
    
'''
Personal Note:
This is my first attempt, but it is Time Complexity = O(n**2)
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        i = 0
        result_list: list = []
        product : int = 1
        while i < len(nums):
            current_value: int = nums[i]
            nums[i] = 1
            for e in nums:
                product  *= e
            result_list.append(product )
            product  = 1
            nums[i] = current_value
            i += 1
        return result_list
'''