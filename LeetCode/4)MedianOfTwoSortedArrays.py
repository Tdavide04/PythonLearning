'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
'''

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums1.extend(nums2) # Merge the two lists 'nums1' and 'nums2' by extending 'nums1' with the elements of 'nums2'.
        nums1.sort() # Sort the merged list to ensure all elements are in order.
        len_nums1 = len(nums1) // 2 # Calculate the middle index of the sorted list.
        left = nums1[len_nums1 - 1]
        right = nums1[len_nums1]
        if len(nums1) % 2 == 0:
            return (left + right) / 2 # If even, the median is the average of the two middle elements.
        else:
            return nums1[len_nums1] # If odd, the median is the middle element in the sorted list.
    
    
    
if __name__ == "__main__":
    
    sos = Solution()
    print(sos.findMedianSortedArrays(nums1 = [], nums2 = [2]))