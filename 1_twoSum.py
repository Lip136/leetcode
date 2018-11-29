# encoding:utf-8
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        # 自己写的方法是for循环，但是发现字典能节省很多时间
        d={}
        for i in range(len(nums)):
            if nums[i] in d:
                return [d[nums[i]],i]
            else:
                d[target-nums[i]]=i