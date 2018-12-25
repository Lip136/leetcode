class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        for k, v in Counter(nums).items():
            if v == 1:
                return k
        # 找了不一样的想法,但是我觉得python就是需要熟悉这些轮子
        #return sum(set(nums)) * 2 - sum(nums)