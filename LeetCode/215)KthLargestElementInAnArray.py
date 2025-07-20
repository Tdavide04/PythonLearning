'''
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
'''

import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        min_heap = nums[:k] # Initialize a min-heap with the first k elements from nums
        heapq.heapify(min_heap) # Transform the list into a min-heap
        for num in nums[k:]:
            if num > min_heap[0]: # If the current element is larger than the smallest element in the heap
                heapq.heappushpop(min_heap, num) # Replace the smallest element (root of the min-heap) with the current element
        return min_heap[0]
    
if __name__ == "__main__":
    
    sos = Solution()
    print(sos.findKthLargest(nums = [3,2,1,5,6,4], k = 2))
    
'''
Strategy
The goal is to find the k-th largest element in a list. To achieve this efficiently:

Use a Min-Heap:

Maintain a min-heap of size k to keep track of the k largest elements seen so far.
The smallest element in this min-heap will be the k-th largest element overall after processing all elements.
Processing:

Initialize the heap with the first k elements of the list.
Iterate through the rest of the list and adjust the heap to ensure it always contains the k largest elements encountered.

Explanation of Functions
heapq.heapify:

Purpose: Transforms a list into a min-heap in-place.
Usage in Code: heapq.heapify(min_heap) ensures that the list min_heap satisfies the min-heap property, with the smallest element at the root.
heapq.heappushpop:

Purpose: Adds a new element to the heap and then removes and returns the smallest element (the root of the min-heap).
Usage in Code: heapq.heappushpop(min_heap, num) ensures that after adding num to the heap, 
the smallest element is removed, maintaining the heap size at k. This operation is more efficient than performing separate push and pop operations.
'''