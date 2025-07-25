'''
You are given a positive integer array nums.

Partition nums into two arrays, nums1 and nums2, such that:

Each element of the array nums belongs to either the array nums1 or the array nums2.
Both arrays are non-empty.
The value of the partition is minimized.
The value of the partition is |max(nums1) - min(nums2)|.

Here, max(nums1) denotes the maximum element of the array nums1, and min(nums2) denotes the minimum element of the array nums2.

Return the integer denoting the value of such partition.

 

Example 1:

Input: nums = [1,3,2,4]
Output: 1
Explanation: We can partition the array nums into nums1 = [1,2] and nums2 = [3,4].
- The maximum element of the array nums1 is equal to 2.
- The minimum element of the array nums2 is equal to 3.
The value of the partition is |2 - 3| = 1. 
It can be proven that 1 is the minimum value out of all partitions.
Example 2:

Input: nums = [100,1,10]
Output: 9
Explanation: We can partition the array nums into nums1 = [10] and nums2 = [100,1].
- The maximum element of the array nums1 is equal to 10.
- The minimum element of the array nums2 is equal to 1.
The value of the partition is |10 - 1| = 9.
It can be proven that 9 is the minimum value out of all partitions.
 

Constraints:

2 <= nums.length <= 105
1 <= nums[i] <= 109
'''

class Solution:
    def findValueOfPartition(self, nums: list[int]) -> int:
        nums.sort()
        # Initialize min_partition to the maximum value in the list
        # This ensures that any smaller difference found will replace it
        min_partition = 100 
        for i in range(len(nums) - 1): # Iterate through the list, comparing each pair of adjacent elements
            x = nums[i] - nums[i+1] # Calculate the difference between the current element and the next one
            if abs(x) < min_partition:  # If the absolute value of the difference is smaller than the current min_partition,
                min_partition = abs(x) # update min_partition to this smaller value
            
        return min_partition
    
    
if __name__ == "__main__":
    
    sos = Solution()
    print(sos.findValueOfPartition([84,11,100,100,75]))