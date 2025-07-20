'''
You are given an array arr of positive integers. You are also given the array queries where queries[i] = [lefti, righti].

For each query i compute the XOR of elements from lefti to righti (that is, arr[lefti] XOR arr[lefti + 1] XOR ... XOR arr[righti] ).

Return an array answer where answer[i] is the answer to the ith query.

 

Example 1:

Input: arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
Output: [2,7,14,8] 
Explanation: 
The binary representation of the elements in the array are:
1 = 0001 
3 = 0011 
4 = 0100 
8 = 1000 
The XOR values for queries are:
[0,1] = 1 xor 3 = 2 
[1,2] = 3 xor 4 = 7 
[0,3] = 1 xor 3 xor 4 xor 8 = 14 
[3,3] = 8

Example 2:

Input: arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]
Output: [8,0,4,4]

 

Constraints:

    1 <= arr.length, queries.length <= 3 * 104
    1 <= arr[i] <= 109
    queries[i].length == 2
    0 <= lefti <= righti < arr.length
'''

#first attempt
class Solution:
    def xorQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        result: list = []
        current: int = 0
        for queri in queries:
            i = queri[0]
            while True:
                current ^= arr[i]
                if i == queri[1]:
                    result.append(current)
                    current = 0
                    i = 0
                    break
                i += 1
        return result


# second attempt
class Solution:
    def xorQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        answer = []
        for left, right in queries:
            xor_result = arr[left]
            for i in range(left + 1, right + 1):
                xor_result ^= arr[i] 
            answer.append(xor_result)
        return answer

# third attempt
class Solution:
    def xorQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        n = len(arr)
        prefix = [0] * n
        prefix[0] = arr[0]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] ^ arr[i]
        answer = []
        for left, right in queries:
            if left == 0:
                result = prefix[right]
            else:
                result = prefix[right] ^ prefix[left - 1]
            answer.append(result)
        return answer


if __name__ == "__main__":

    sos = Solution()
    print(sos.xorQueries(arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]))