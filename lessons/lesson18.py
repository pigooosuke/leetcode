from typing import List

# time exceeded


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def twosum(nums: List[int],  target: int) -> List[int]:
            res = []
            lo, hi = 0, len(nums) - 1
            while (lo < hi):
                sum_v = nums[lo] + nums[hi]
                # print(f"{lo=},{hi=},{sum_v}, {target=}, {sum_v=}")
                if target > sum_v or (lo > 0 and nums[lo] == nums[lo - 1]):
                    lo += 1
                elif target < sum_v or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
                    hi -= 1
                else:
                    res.append([nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
            # print(res)
            return res

        def ksum(nums: List[int], target: int, k: int) -> List[int]:
            res = []

            if len(nums) == 0 or nums[0] * k > target or target > nums[-1] * k:
                return res
            if k == 2:
                res = twosum(nums, target)
            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for set in ksum(nums[i+1:], target - nums[i], k-1):
                        res.append([nums[i]]+set)

            return res

        # do
        nums.sort()
        # print(nums)
        return ksum(nums, target, 4)


solution = Solution()
ans = solution.fourSum(nums=[1, 0, -1, 0, -2, 2], target=0)
print(f"{ans=}")
