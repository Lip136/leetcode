class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = s.split()
        if not res:
            return 0
        else:
            return len(res[-1])