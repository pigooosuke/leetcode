class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        target_index = 0
        
        memory_dict = dict()
        start_index = 0
        for target_index in range(len(s)):
            if s[target_index] in memory_dict:
                start_index = max(start_index, memory_dict[s[target_index]])
            ans = max(ans, target_index - start_index + 1)
            memory_dict[s[target_index]] = target_index + 1

        
        return ans


solution = Solution()
solution.lengthOfLongestSubstring("pwwkew")