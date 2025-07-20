'''
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

 

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
 

Constraints:

1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000
'''

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        diz: dict = {} # Initialize an empty dictionary to store the frequency of each number in the array.
        for num in arr: # Iterate through each number in the array.
            if num not in diz: # If the number is not in the dictionary, add it with a count of 1.
                diz[num] = 1
            else: # If the number is already in the dictionary, increment its count.
                diz[num] += 1
        # Initialize an empty list to store the occurrence counts (frequencies).
        values_list: list = []
        # Iterate through the frequency values in the dictionary.
        for values in diz.values():
            # If the frequency is not already in the list, add it.
            if values not in values_list:
                values_list.append(values)
            # If the frequency is already in the list, return False because it means
            # there are duplicate occurrence counts, which should not happen.
            else:
                return False
        return True

    
if __name__ == "__main__":
    
    sos = Solution()
    print(sos.uniqueOccurrences(arr = [1,2,2,1,1,3]))
    print(sos.uniqueOccurrences(arr = [3,5,-2,-3,-6,-6]))
    print(sos.uniqueOccurrences(arr = [-3,0,1,-3,1,1,1,-3,10,0]))