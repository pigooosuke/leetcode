from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        idx = 0
        m_i = 0
        n_i = 0
        save_index = set([(m + n) // 2])
        save_val = 0
        if (m+n) % 2 == 0:
            save_index.add(((m + n) // 2)-1)
        print("save", save_index)
        for i in range(m+n):
            m_value = nums1[m_i] if m != m_i else 9999999999999999999
            n_value = nums2[n_i] if n != n_i else 9999999999999999999
            print(m_value, n_value)
            if m_value <= n_value:
                if i in save_index:
                    print("m", m_value)
                    save_val += m_value
                if m_i != m:
                    m_i += 1
            else:
                if i in save_index:
                    print("n", n_value)
                    save_val += n_value
                if n_i != n:
                    n_i += 1
        print("total", save_val)
        if len(save_index) == 2:
            ans = save_val / 2
        else:
            ans = save_val
        print(ans)
        return ans


solution = Solution()
solution.findMedianSortedArrays([1, 2], [3, 4])
