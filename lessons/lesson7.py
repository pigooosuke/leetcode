class Solution:
    def reverse(self, x: int) -> int:
        max_boundary = 2 ** 31 -1
        min_boundary = 2 ** 31 * (-1)
        ans = int(str(abs(x))[::-1])
        if x < 0:
            ans = ans * (-1)

        if max_boundary < ans or ans < min_boundary:
            return 0
        return ans