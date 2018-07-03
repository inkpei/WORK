#
#
#   
# 914. 翻转游戏
# 翻转游戏：给定一个只包含两种字符的字符串：+和-，你和你的小伙伴轮流翻转"++"变成"--"。当一个人无法采取行动时游戏结束，另一个人将是赢家。
#
# 编写一个函数，计算字符串在一次有效移动后的所有可能状态。
#
# 样例
# 给定 s = "++++", 在一次有效移动后，它会变成下列状态之一：
#
# [
#   "--++",
#   "+--+",
#   "++--"
# ]
# 如果无法移动，则返回一个空列表[].


class Solution:
    """
    @param s: the given string
    @return: all the possible states of the string after one valid move
    """
    def generatePossibleNextMoves(self, s):
        s = list(s)
        length = len(s)
        res = []
        for i in range(0,length - 1):
            if s[i] =='+' and s[i] == s[i+1]:
                tmp = s[:]

                tmp[i] = '-'
                tmp[i+1] = '-'
                t = ""
                for i in tmp:
                    t += i

                res.append(t)
        return res
        # write your code here
