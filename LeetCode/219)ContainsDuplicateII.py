'''
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
'''

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        diz: dict[int:int] = {} # Create a dictionary to store the last seen index of each number
        for i, num in enumerate(nums): # Iterate over the list with both index and value
            if num not in diz:
                diz[num] = i
            else:
                if abs(i - diz[num]) <= k: # If the number is already in the dictionary, check the distance
                    return True
                else:
                    diz[num] = i
        return False
                
    
    
if __name__ == "__main__":
    
    sos = Solution()
    print(sos.containsNearbyDuplicate(nums = [1,2,3,1], k = 3))
    print(sos.containsNearbyDuplicate(nums = [1,0,1,1], k = 1))
    
'''
Strategy
The strategy for solving the problem involves using a dictionary to track the last index of each element encountered in the list. 
As you iterate through the list:
Check Existence: For each element, check if it has been seen before by looking it up in the dictionary.
Distance Check: If the element has been seen before, calculate the difference between the current index and the stored index.
If the difference is less than or equal to the given threshold k, return True as the condition is met.
Update Index: If the difference exceeds k or the element was not previously seen, update the dictionary with the current index of the element.
Completion: If the iteration completes without finding any qualifying duplicates, return False.
This approach ensures efficient checking and updating of elements while maintaining a time complexity of O(n), where n is the number of elements in the list.
'''