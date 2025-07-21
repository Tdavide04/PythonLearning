'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
'''

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        
        nums2 = []
        for e in nums:
            if e < target:
                nums2.append(e)

        return len(nums2)


if __name__ == "__main__":

    sos = Solution()
    print(sos.searchInsert([1,2,4,5,6], 3))