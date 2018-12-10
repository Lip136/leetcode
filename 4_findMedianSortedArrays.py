class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1+nums2
        nums = sorted(nums)
        mid = int(len(nums)/2)
        if len(nums) % 2 == 0:
            return (nums[mid] + nums[mid-1])/2.0
        else:
            return float(nums[mid])