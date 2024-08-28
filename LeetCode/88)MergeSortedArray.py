'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 

Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109
 

Follow up: Can you come up with an algorithm that runs in O(m + n) time?
'''

class Solution: # 37 ms
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        # Remove the excess elements from nums1 that are beyond the first 'm' elements.
        # This ensures nums1 contains only the relevant initial elements.
        while len(nums1) > m:
            nums1.pop()
        i = 0 # Initialize a counter 'i' to keep track of the current position in nums2.
        while len(nums1) != m + n: # Merge the elements from nums2 into nums1 until the total length equals m + n.
            nums1.insert(i+1,nums2[i]) # Insert elements from nums2 into nums1 one by one at the appropriate position.
            i +=1
        nums1.sort()
        return nums1
    
class Solution: # 40 ms
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        while len(nums1) > m:
            nums1.pop()
        for e in nums2:
            nums1.append(e)
        nums1.sort()
        return nums1

if __name__ == "__main__":
    
    sos = Solution()
    print(sos.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))
        