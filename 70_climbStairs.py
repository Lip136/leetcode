class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 使用递归会超时，因此使用列表
        # 2 - 2
        # 3 - 3
        # 4 - 5
        res = [1]
        if n >= 2:
            res.append(2)
        for i in range(2, n):
            res.append(res[i - 1] + res[i - 2])
        return res[n - 1]