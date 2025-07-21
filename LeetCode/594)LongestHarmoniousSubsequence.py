'''
We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: nums = [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
Example 2:

Input: nums = [1,2,3,4]
Output: 2
Example 3:

Input: nums = [1,1,1,1]
Output: 0
 

Constraints:

1 <= nums.length <= 2 * 104
-109 <= nums[i] <= 109
'''

class Solution:
    def findLHS(self, nums: list[int]) -> int:
        # Initialize the variable to keep track of the maximum length of harmonious subsequence
        max_len: int = 0
        # Initialize a dictionary to store the frequency of each number
        num_freq: dict[int] = {}
        # Populate the frequency dictionary with counts of each number in the input list
        for num in nums:
            if num in num_freq:
                num_freq[num] += 1  # Increment the count if the number is already in the dictionary
            else:
                num_freq[num] = 1   # Initialize the count to 1 if the number is not in the dictionary
        # Iterate through the list of numbers again
        for num in nums:
            # Check if the number + 1 exists in the frequency dictionary
            if num + 1 in num_freq:
                # Calculate the length of the harmonious subsequence that includes both num and num + 1
                current_len = num_freq[num] + num_freq[num + 1]
                # Update the maximum length if the current subsequence length is greater
                max_len = max(max_len, current_len)
        return max_len

    

if __name__ == "__main__":
    
    sos = Solution() 
    print(sos.findLHS(nums = [1,3,2,2,5,2,3,7])) # Output: 5
    print(sos.findLHS(nums = [1,2,3,4])) # Output: 2
    print(sos.findLHS(nums = [1,1,1,1])) # Output: 0
    print(sos.findLHS(nums = [1, 2, 2, 1, 1, 2, 2, 1])) # Output: 8
    
'''
Strategy for Using the Dictionary:
Frequency Counting:

Use a dictionary num_freq to count the frequency of each integer in the input list nums. This allows for efficient retrieval of the count of any number.
Iterate through the list nums and populate the dictionary. 
If a number is already present in the dictionary, increment its count; otherwise, add it with an initial count of 1.
Finding Harmonious Subsequences:

After populating the frequency dictionary, iterate through the list nums again.
For each number num, check if num + 1 exists in the frequency dictionary. This check ensures that you only consider pairs of numbers that differ by exactly 1.
If num + 1 exists, calculate the length of the harmonious subsequence that includes both num and num + 1. The length is the sum of the counts of these two numbers.
Update the maximum length found so far (max_len) if the current subsequence length is greater.
Efficiency:

The time complexity is O(N), where N is the number of elements in the input list nums. 
This is because we iterate through the list twice: once to build the frequency dictionary and once to find the maximum length of the harmonious subsequence.
The space complexity is also O(N) due to the storage of the frequency counts in the dictionary.
By following this strategy, the code efficiently finds the longest harmonious subsequence by leveraging the frequency dictionary to perform quick lookups and updates.
'''