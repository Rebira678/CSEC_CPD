https://leetcode.com/problems/missing-number/description/
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=max(nums)
        numbers=set([i for i in range(0,n+1)])

        for i in nums:
            if i not in numbers:
                return i
