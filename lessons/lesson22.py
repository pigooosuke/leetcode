from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def gen(pat, left, right, ans):
            print(pat, left, right)
            if left:
                print("A")
                gen(pat + "(", left - 1, right, ans)
            if right > left:
                print("B")
                gen(pat + ")", left, right - 1, ans)
            if not right:
                print("C")
                ans.append(pat)
            return ans
        if n == 0:
            return ['']
        ans = []
        ans = gen("", n, n, ans)
        return ans


solution = Solution()
ans = solution.generateParenthesis(n=3)
print(f"{ans=}")
