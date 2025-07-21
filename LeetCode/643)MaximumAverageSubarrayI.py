'''
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
 

Constraints:

n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104
'''

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # Calculate the sum of the first 'k' elements.
        window_sum = sum(nums[:k])
        max_sum = window_sum
        
        # Use a sliding window to calculate the maximum sum of any subarray of length 'k'.
        for i in range(k, len(nums)):
            # Slide the window right: subtract the element that is left behind and add the new element.
            window_sum += nums[i] - nums[i - k]
            # Update the maximum sum if the current window sum is greater.
            max_sum = max(max_sum, window_sum)
        
        # Calculate the maximum average and return it.
        return max_sum / k

    

if __name__ == "__main__":
    
    sos = Solution()
    print(sos.findMaxAverage(nums = [0,1,1,3,3], k = 4))
    print(sos.findMaxAverage(nums = [1,12,-5,-6,50,3], k = 4)) # Output: 12.75000
    print(sos.findMaxAverage(nums = [5], k = 1))
    print(sos.findMaxAverage(nums = [-6662,5432,-8558,-8935,8731,-3083,4115,9931,-4006,-3284,-3024,1714,-2825,-2374,-2750,-959,6516,9356,8040,-2169,-9490,-3068,6299,7823,-9767,5751,-7897,6680,-1293,-3486,-6785,6337,-9158,-4183,6240,-2846,-2588,-5458,-9576,-1501,-908,-5477,7596,-8863,-4088,7922,8231,-4928,7636,-3994,-243,-1327,8425,-3468,-4218,-364,4257,5690,1035,6217,8880,4127,-6299,-1831,2854,-4498,-6983,-677,2216,-1938,3348,4099,3591,9076,942,4571,-4200,7271,-6920,-1886,662,7844,3658,-6562,-2106,-296,-3280,8909,-8352,-9413,3513,1352,-8825], k = 90))
    print(sos.findMaxAverage(nums = [9,7,3,5,6,2,0,8,1,9], k = 6))