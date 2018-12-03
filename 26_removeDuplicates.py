class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return len(nums)

        tmp = nums[0]
        index = 0
        for i, c in enumerate(nums):
            if tmp == c:
                continue
            else:
                nums[index] = tmp
                tmp = c
                index += 1
        nums[index] = tmp
        return len(nums[:index+1])