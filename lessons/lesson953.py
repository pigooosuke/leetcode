class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        def comp_w(first, second):
            min_len = min(len(first), len(second))
            for i in range(min_len):
                if first[i] == second[i]:
                    continue
                else:
                    if order_dict[first[i]] < order_dict[second[i]]:
                        print("A", i)
                        return True
                    if order_dict[first[i]] > order_dict[second[i]]:
                        print("B", i)
                        return False
            if len(first) > len(second):
                return False
            return True
        res = True
        n_words = len(words)
        order_dict = {w: i for i, w in enumerate(order)}
        for n in range(0, n_words-1):
            first = words[n]
            second = words[n+1]
            res = comp_w(first, second)
            if res is False:
                if first == second:
                    res = True
                    continue
                return res

        return res


solution = Solution()
ans = solution.isAlienSorted(
    words=["hello", "hello"], order="abcdefghijklmnopqrstuvwxyz")
print(f"{ans=}")
