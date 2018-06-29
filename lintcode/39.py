# 描述
# 给定一个旋转排序数组，在原地恢复其排序。
#
# 您在真实的面试中是否遇到过这个题？
# 说明
# 什么是旋转数组？
#
# 比如，原始数组为[1,2,3,4], 则其旋转数组可以是[1,2,3,4], [2,3,4,1], [3,4,1,2], [4,1,2,3]
# 样例
# [4, 5, 1, 2, 3] -> [1, 2, 3, 4, 5]
#
# 挑战
# 使用O(1)的额外空间和O(n)时间复杂度

class Solution:
    """
    @param nums: An integer array
    @return: nothing
    """
    def reslove(self,nums,start,end):
        while start < end:
            t = nums[start]
            nums[start] = nums[end]
            nums[end] = t
            start += 1
            end -= 1
    def recoverRotatedSortedArray(self, nums):
        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i+1]:
                Solution.reslove(self,nums,0,i)
                Solution.reslove(self,nums,i+1,len(nums)-1)
                Solution.reslove(self,nums,0,len(nums) -1)
                return


        # write your code here
