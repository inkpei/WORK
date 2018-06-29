#
# 描述
# 扔 n 个骰子，向上面的数字之和为 S。给定 Given n，请列出所有可能的 S 值及其相应的概率。
#
# You do not care about the accuracy of the result, we will help you to output results.
#
# 您在真实的面试中是否遇到过这个题？
# 样例
# 给定 n = 1，返回 [ [1, 0.17], [2, 0.17], [3, 0.17], [4, 0.17], [5, 0.17], [6, 0.17]]

class Solution:
    # @param {int} n an integer
    # @return {tuple[]} a list of tuple(sum, probability)
    def dicesSum(self, n):
        tmp = []
        for i in range(6):
            tmp.append(1)
        for i in range(2,n+1):
            re = []
            x = 0
            for j in range(i,6*i+1):
                k = 1
                while k <= 6:
                    if j - k > 0:
                        print(j , k , i)
                        x += tmp[j-k-i]
                    k += 1
                re.append(x)
            tmp = re
        res = []
        total = 0
        for i in range(n,6*n+1):
            total += tmp[n][i]
        for i in range(n,6*n+1):
            res.append([i,round(tmp[n][i]/total,2)])
        return res

        # Write your code here


if __name__ == '__main__':
    s = Solution()
    print(s.dicesSum(5))
