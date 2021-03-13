from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = None
        max_diff = None
        for i, val in enumerate(nums[1:-1]):
            # print(nums[i: i + 3])
            vals = sum(nums[i: i + 3])
            diff = abs(target - vals)
            if max_diff is None:
                max_diff = diff
                ans = vals
            else:
                if max_diff > diff:
                    max_diff = diff
                    ans = vals
            # print(f"{diff=}, {ans=}")
        return ans


solution = Solution()
ans = solution.threeSumClosest(nums=[-1, 2, 1, -4], target=1)
print(f"{ans}")
