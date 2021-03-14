
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        for n in range(len(nums)):
            head = n
            tail = n + 1
            while head < tail and len(nums) > tail:
                sum_v = sum(nums[head:tail])
                res = max(res, sum_v)
                tail += 1
        return res


solution = Solution()
ans = solution.maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(f"{ans=}")
