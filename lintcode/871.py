#
# 871. 最小分解
# 给定一个正整数a，找到最小的正整数b，它的每个数字相乘之后等于a。
# 如果没有答案，或者答案不符合32位整数，则返回0
#
# 样例
# 给定 a = 48, 返回 68. 给定 a = 15, 返回 35.

class Solution:
    """
    @param a: a positive integer
    @return: the smallest positive integer whose multiplication of each digit equals to a
    """
    def smallestFactorization(self, a):
        if a == 1 : return 1
        res =""
        for x in range(2,10)[::-1]:
            while a % x == 0:
                    res = str(x) + res
                    a = int(a/x)
        if a > 1 : return  0
        res = int(res)
        if res > pow(2,32)-1 : return 0
        return res



if __name__ == '__main__':
    s = Solution()
    a = s.smallestFactorization(18000000)
    print(a)
    t = 1
    for i in list(str(a)):
        t *= int(i)
    print(t)


