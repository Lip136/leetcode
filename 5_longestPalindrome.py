class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)<2 or s==s[::-1]:
            return s

        max_len = 1
        start = 0
        for i in range(1, len(s)):
            odd = s[i-max_len-1 : i+1]
            even = s[i-max_len : i+1]

            # 奇数
            if i-max_len-1>=0 and odd=odd[::-1]:
                start = i-max_len-1
                max_len += 2
                continue
            # 偶数
            if i-max_len>=0 and even=even[::-1]:
                start = i-max_len
                max_len += 1
            return s[start : start+max_len]