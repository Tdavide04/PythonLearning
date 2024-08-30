'''
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.

 

Example 1:

Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]
Explanation:
For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6].
Example 2:

Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
Output: [[3],[]]
Explanation:
For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], their value is only included once and answer[0] = [3].
Every integer in nums2 is present in nums1. Therefore, answer[1] = [].
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
-1000 <= nums1[i], nums2[i] <= 1000
'''

class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        # Initialize the answer as a list of two empty lists.
        # The first list will store elements unique to nums1, and the second list will store elements unique to nums2.
        answer: list[list[int]] = [[], []]
        # Combine both lists (nums1 and nums2) and remove duplicates by converting to a set, then back to a list.
        nums = nums1 + nums2
        nums = list(set(nums))
        # Iterate over each unique number in the combined list.
        for num in nums:
            # If the number is not in nums1, it is unique to nums2, so add it to the second list in the answer.
            if num not in nums1:
                answer[1].append(num)
            # If the number is not in nums2, it is unique to nums1, so add it to the first list in the answer.
            if num not in nums2:
                answer[0].append(num)
        # Return the answer, which contains two lists of unique elements.
        return answer

    
class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        # Convert both lists (nums1 and nums2) to sets to remove duplicates and allow set operations.
        ones = set(nums1)
        twos = set(nums2)
        # Calculate the difference between the sets.
        # differences1 contains elements in nums1 but not in nums2.
        differences1 = ones - twos 
        # differences2 contains elements in nums2 but not in nums1.
        differences2 = twos - ones
        # Convert the set differences back to lists and store them in the answer list.
        answer = [list(differences1), list(differences2)]
        # Return the answer, which contains two lists of unique elements.
        return answer

    
if __name__ == "__main__":
    
    sos = Solution()
    print(sos.findDifference(nums1 = [1,2,3], nums2 = [2,4,6]))
    print(sos.findDifference(nums1 = [1,2,3,3], nums2 = [1,1,2,2]))
    print(sos.findDifference(nums1 = [-80,-15,-81,-28,-61,63,14,-45,-35,-10], nums2 = [-1,-40,-44,41,10,-43,69,10,2]))