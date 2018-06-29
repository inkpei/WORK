
#
# 描述
# 给定一个整数数组A。
#
# 定义B[i] = A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]， 计算B的时候请不要使用除法。

# 样例
# 给出A=[1, 2, 3]，返回 B为[6, 3, 2]

"""
    @param: nums: Given an integers array A
    @return: A long long array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """
def productExcludeItself( nums):
# write your code here
    B = []
    for x in range(len(nums)):
        B.append(1)
        for j in range(len(nums)):
            if x == j:
                continue
            B[x] *= nums[j]
    return B

if __name__ == '__main__':
    A = [1, 2, 3]
    print(productExcludeItself(A))