class Solution:
    def missingNumber(self, nums: list[int]) -> int:

        len_nums = len(nums)
        nums2 = [e for e in range(0, len_nums + 1)]
        for e in nums:
            if e in nums2:
                nums2.remove(e)
        target = nums2[0]
        return target

if __name__ == "__main__":
    sos = Solution()
    print(sos.missingNumber([9,6,4,2,3,5,7,0,1]))
    
   