from typing import List
import itertools
from collections import Counter

# time exceeded


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        nums_counter = Counter(nums)
        memo = set()
        ans = []

        for d in itertools.combinations(nums, 3):
            d = tuple(sorted(d))
            if d in memo:
                continue
            memo.add(d)
            d_counter = Counter(d)
            diff = target - sum(d)
            if d_counter[diff] == nums_counter[diff]:
                continue
            d = list(d)
            d.append(diff)
            d.sort()
            if d in ans:
                continue
            ans.append(d)
            # print(ans)
        return ans


solution = Solution()
ans = solution.fourSum(nums=[1, 0, -1, 0, -2, 2], target=0)
