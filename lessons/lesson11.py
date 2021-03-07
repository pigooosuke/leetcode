from typing import List
import itertools


class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        length = len(height)
        area_dict = dict()
        min_height = 0
        ignore_index = set()
        for pair in itertools.combinations(enumerate(height), 2):
            (i_0, h_0), (i_1, h_1) = pair
            if i_1 in ignore_index:
                continue
            if h_0 > h_1:
                ignore_index.add(i_1)
            if h_0 < min_height:
                continue
            if i_0 in area_dict:
                max_area = area_dict[i_0]
            else:
                max_area = (length - i_0) * h_0
                area_dict[i_0] = max_area
            if ans > max_area:
                continue
            w = i_1 - i_0
            h = min(h_1, h_0)
            ans = max(ans, w*h)
            min_height = h_0
        return ans


solution = Solution()
solution.maxArea(height=[4, 3, 2, 1, 4])
