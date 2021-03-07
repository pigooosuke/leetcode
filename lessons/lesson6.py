class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        save_dict = dict()
        for r in range(numRows):
            save_dict[r] = []
        mid = numRows * 2 - 2
        chunked = list(chunks(s, mid))
        for d in chunked:
            # print(d)
            for i, w in enumerate(d):
                if i > numRows - 1:
                    # print(numRows - (i - numRows) -2, w)
                    save_dict[numRows - (i - numRows)-2].append(w)
                else:
                    # print(i,w)
                    save_dict[i].append(w)
        ans = ""
        for k, v in save_dict.items():
            ans += "".join(v)
        return ans



def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


test = "PAYPALISHIRING"
solution = Solution()
ans = solution.convert(s=test, numRows=3)
print(ans)