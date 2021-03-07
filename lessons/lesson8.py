class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        target_str = ""
        value_sign = 1
        for i, w in enumerate(s):
            if w.isdigit():
                target_str += w
                continue
            if i == 0 and w in ["-", "+"]:
                if w == "-":
                    value_sign = -1
                elif w == "+":
                    value_sign = 1
                continue
            if len(target_str) > 0 and not w.isdigit():
                break
            break

        if len(target_str) == 0:
            return 0
        ans = int(target_str) * (value_sign)
        if ans <= 2 ** 31 * (-1):
            ans = 2 ** 31 * (-1)
        elif ans >= 2 ** 31 - 1:
            ans = 2 ** 31 - 1
        return ans


solution = Solution()
solution.myAtoi(s="   -42")
