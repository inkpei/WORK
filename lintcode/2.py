# 描述
# 设计一个算法，计算出n阶乘中尾部零的个数
#
# 您在真实的面试中是否遇到过这个题？
# 样例
# 11! = 39916800，因此应该返回 2
#
# 挑战
# O(logN)的时间复杂度
"""
@param: n: An integer
@return: An integer, denote the number of trailing zeros in n!
"""
def trailingZeros( n):
    res = 0
    while True:
        n = int(n/5)
        res += n
        if n == 0:
            break
    return res


def test(n):
    res = 0
    for i in range(1, n + 1):
        while i % 5 == 0:
            res += 1
            i = int(i / 5)
    return res
if __name__ == '__main__':
    print(trailingZeros(100752768278672))
    # print(pow(5, 5))
