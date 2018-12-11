class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # input:[-2,1,-3,4,-1,2,1,-5,4]
        # output:6
        # [4,-1,2,1]
        res = nums[0]
        total = 0
        for i, c in enumerate(nums):
            if total > 0:
                total += c
            else:
                total = c
            res = max(res, total)

        return res