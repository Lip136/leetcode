class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # nums上进行赋值
        index = 0
        for i, c in enumerate(nums):
            if val == c:
                continue
            else:
                nums[index] = c
                index += 1
        return len(nums[:index])