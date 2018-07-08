# 662. Guess Number Higher or Lower
# 我们正在玩猜数游戏。 游戏如下：
# 我从 1 到 n 选择一个数字。 你需要猜我选择了哪个号码。
# 每次你猜错了，我会告诉你这个数字是高还是低。
# 你调用一个预定义的接口 guess(int num)，它会返回 3 个可能的结果(-1，1或0):
#
# 样例
# n = 10, 我选择了 4 (但是你不知道)
# 返回 4。正确！


"""
The guess API is already defined for you.
@param num, your guess
@return -1 if my number is lower, 1 if my number is higher, otherwise return 0
you can call Guess.guess(num)
"""


class Solution:
    # @param {int} n an integer
    # @return {int} the number you guess


    def guess(self,m):

        a = 16
        if a == m :
            return 0
        return 1 if m > a else -1
    def guessNumber(self, n):
        l = 0
        r = n
        k = int((l+r)/2)
        while l != r:
            print(k)
            f = self.guess(k)
            if f == 0:
                return k
            if f > 0:
                l = k
            else:
                r = k
            k = int((l+r)/2)

        # Write your code here

if __name__ == '__main__':
    s = Solution()
    print(s.guess(100))