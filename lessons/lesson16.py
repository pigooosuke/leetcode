from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = float("inf")
        nums.sort()
        # print(nums)
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                ans = self.twosum(i, nums, target, ans)
        return ans

    def twosum(self, i: int, nums: List[int], target: int, ans: float) -> int:
        lo, hi = i+1, len(nums) - 1
        while (lo < hi):
            sum_v = nums[i] + nums[lo] + nums[hi]
            # print(f"{i=}, {lo=}, {hi=}, {ans=} {sum_v=}")
            if abs(target - ans) > abs(target - sum_v):
                ans = sum_v
            if target > sum_v:
                lo += 1
                # memory less
                while (lo < hi and lo > 2 and nums[lo - 1] == nums[lo] == nums[lo+1]):
                    lo += 1
            elif target < sum_v:
                hi -= 1
                # memory less
                while (lo < hi and hi < len(nums) - 2 and nums[hi-1] == nums[hi] == nums[hi+1]):
                    hi -= 1
            else:
                return ans
        return ans


solution = Solution()
ans = solution.threeSumClosest(nums=[1, 1, -1, -1, 3], target=1)
print(f"{ans=}")
