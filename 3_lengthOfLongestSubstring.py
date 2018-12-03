class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #　使用滑动窗口的方法去找最大子串[slow, fast]
    table = dict()
    slow = 0
    fast = 0
    ret_max = 0

    while slow<len(s) and fast<len(s):
        if s[fast] in table:
            del table[s[slow]]
            slow += 1
        else:
            table[s[fast]] = fast
            fast += 1
            ret_max = max(ret_max, fast-slow)

    return ret_max