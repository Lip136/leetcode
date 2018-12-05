class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # nums是有序列表
        # if target in nums:
        #     return nums.index(target)
        # else:
        #     nums.append(target)
        #     return sorted(nums).index(target)

        # 二分法[i, j]
        i = 0
        j = len(nums) - 1
        mid = int((i+j)/2)
        while True:
            if j<0:
                return 0
            if i>=len(nums):
                return i
            if i>j:
                return i+1 if nums[i]<target else i

            mid = int((i+j)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid]>target:
                j = mid-1
            elif nums[mid]<target:
                i = mid+1