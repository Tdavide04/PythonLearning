'''
You are given an integer array arr. Sort the integers in the array in ascending order by the number of 1's in their binary representation and in case of two or more integers have the same number of 1's you have to sort them in ascending order.

Return the array after sorting it.

 

Example 1:

Input: arr = [0,1,2,3,4,5,6,7,8]
Output: [0,1,2,4,8,3,5,6,7]
Explantion: [0] is the only integer with 0 bits.
[1,2,4,8] all have 1 bit.
[3,5,6] have 2 bits.
[7] has 3 bits.
The sorted array by bits is [0,1,2,4,8,3,5,6,7]
Example 2:

Input: arr = [1024,512,256,128,64,32,16,8,4,2,1]
Output: [1,2,4,8,16,32,64,128,256,512,1024]
Explantion: All integers have 1 bit in the binary representation, you should just sort them in ascending order.
 

Constraints:

1 <= arr.length <= 500
0 <= arr[i] <= 104
'''

class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        # The sorted() function sorts the array based on the custom key defined by the lambda function.
        # The lambda function sorts by two criteria:
        # 1. The number of '1' bits in the binary representation of each integer (bin(x).count('1')).
        # 2. In case of a tie (same number of '1' bits), it sorts by the integer's value (x).
        
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))
    
'''
Breakdown:
sorted(arr, key=lambda x: (bin(x).count('1'), x)):
This sorts the arr using a custom sorting rule provided by lambda.
lambda x: (bin(x).count('1'), x) creates an anonymous function that takes an element x and returns a tuple with two values:
bin(x).count('1'): Converts the integer x to its binary representation using bin(x) and counts how many '1' bits are present.
x: The integer itself, used as a secondary sort criterion in case two numbers have the same number of '1' bits.
sorted() first sorts by the number of '1' bits, and then by the integer value in case of a tie.
'''

    
if __name__ == "__main__":
    
    sos = Solution()
    