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
        
        length = len(nums)
        # Initialize the result list with 1s, which will store the final output.
        # The list has the same length as the input list.
        result = [1] * length
        
        left_product = 1 # Initialize a variable to store the cumulative product of elements to the left of the current index.
        # calculate the product of all elements to the left of each index.
        # Traverse from left to right through the input list.
        for i in range(length):
            # At each index, store the current left_product in the result list.
            # This gives the product of all elements to the left of index i.
            result[i] = left_product
            # Update the left_product to include the current element (nums[i]).
            # This will be used for the next index in the subsequent iteration.
            left_product *= nums[i] 
            
        right_product = 1 # Initialize another variable to store the cumulative product of elements to the right of the current index.
        # calculate the product of all elements to the right of each index.
        # Traverse from right to left through the input list.
        for i in range(length - 1, -1, -1):
            # Multiply the existing value in the result list by the current right_product.
            # This combines the product of all elements to the left and right of index i.
            result[i] *= right_product
            # Update the right_product to include the current element (nums[i]).
            # This will be used for the next index in the subsequent iteration.
            right_product *= nums[i]
        
        return result
            
    
if __name__ == "__main__":
    
    sos = Solution()
    print(sos.productExceptSelf(nums = [1,2,3,4]))
    
'''
First Pass (Left Products):

The variable left_product is initialized to 1. 
It will be used to store the product of all elements to the left of the current index.
The first for loop iterates over the list from left to right.
At each index i, the value of left_product (which is the product of all elements to the left of i) is stored in result[i].
After updating result[i], left_product is multiplied by the current element nums[i]. 
This prepares left_product for the next index.


Second Pass (Right Products):

The variable right_product is also initialized to 1. 
It will be used to store the product of all elements to the right of the current index.
The second for loop iterates over the list from right to left.
At each index i, the current right_product (which is the product of all elements to the right of i) is multiplied by result[i]. 
This combines the left and right products at each index.
After updating result[i], right_product is multiplied by the current element nums[i]. 
This prepares right_product for the next index.


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