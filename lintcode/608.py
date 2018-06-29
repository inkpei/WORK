# 描述
# 给定一个已经 按升序排列 的数组，找到两个数使他们加起来的和等于特定数。
# 函数应该返回这两个数的下标，index1必须小于index2。注意返回的值不是 0-based。
#
# 你可以假设每个输入刚好只有一个答案
# 样例
# 给定数组为 [2,7,11,15] ，target = 9
# 返回 [1,2]

"""
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
def twoSum(nums, target):
    # write your code here
    for x in range(len(nums)):
        find = target - nums[x]
        # print(find)
        if find < nums[x] :
            continue
        for t in range(x+1,len(nums)):
            if find == nums[t]:
                return x +1,t+1
    return

if __name__ == '__main__':
    nums = [0,0,3,4]
    target = 0
    print(twoSum(nums, target))
