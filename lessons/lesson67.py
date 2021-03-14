class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = int(a) + int(b)
        res = str(res)
        ans = ""
        supplement = 0
        while len(a) > 0 or len(b) > 0:
            if len(a) > 0:
                a_bi = int(a[-1])
                a = a[:-1]
            else:
                a_bi = 0
            if len(b) > 0:
                b_bi = int(b[-1])
                b = b[:-1]
            else:
                b_bi = 0
            sum_v = supplement + a_bi + b_bi
            supplement, mod = divmod(sum_v, 2)
            ans = str(mod) + ans
        if supplement == 1:
            ans = str(supplement) + ans
        return ans
