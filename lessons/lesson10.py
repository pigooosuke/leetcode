import re


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = re.fullmatch(re.compile(p), s)
        if m:
            return True
        else:
            return False


solution = Solution()
solution.isMatch(s="aab", p="c*a*b")
