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
        # Write your code here
        total = 6 ** n
        result = []
        f = [0] * (n * 6 + 1)
        g = f[:]
        for i in range(1, 7):
            f[i] = 1
        for k in range(2, n + 1):
            for i in range(1, 6 * k + 1):
                for j in range(1, 7):
                    if i - j > 0:
                        g[i] += f[i - j]
                    else:
                        break
            f = g[:]
            print(f)
            g = [0] * (n * 6 + 1)
        for i in range(1 * n, 6 * n + 1):
            arr = [i]
            arr.append(float(f[i]) / float(total))
            result.append(arr)
        return result

        # Write your code here


if __name__ == '__main__':
    s = Solution()
    print(s.dicesSum(5))
