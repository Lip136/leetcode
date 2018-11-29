# encoding:utf-8
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # 遍历长度最短的str，查看是否在每一个字符串里面即可

        if not strs:
            return ""
        small_str = min(strs, key=len)
        for i, c in enumerate(small_str):
            for str_l in strs:
                if str_l[i] != c:
                    return small_str[:i]
        return small_str
