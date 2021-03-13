import itertools
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        for pair in itertools.combinations(nums, 3):
            if sum(pair) == 0:
                ans.add(list(set(pair)))
        ans = list(ans)
        return ans



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) < 3:
            return res
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i-1]:
                self.twosum(i, nums, res)
                
        return res

    def twosum(self, i: int, nums: List[int],  res: List[int]):
        lo, hi = i+1, len(nums) - 1
        while (lo < hi):
            sum_v = nums[i] + nums[lo] + nums[hi]
            if sum_v > 0:
                hi -= 1
            elif sum_v < 0:
                lo += 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo -1]:
                    lo += 1
                    