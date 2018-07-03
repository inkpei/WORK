# 888. 有效单词词广场
# 给定一个单词序列，检查它是否构成一个有效单词广场。
# 一个有效的单词广场满足：如果第k行和第k列读取相同的字符串,并且0≤k<max(numRows numColumns)。
#
# 样例
# 给定
# [
#   "abcd",
#   "bnrt",
#   "crmy",
#   "dtye"
# ]
# 返回 true
#
# 解释:
# 第一行和第一列都是“abcd”。
# 第二行和第二列都是“bnrt”。
# 第三行和第三列都是“crmy”。
# 第四行和第四列都是“dtye”。
#
# 因此，这是一个有效的单词广场.
# 给定
# [
#   "abcd",
#   "bnrt",
#   "crm",
#   "dt"
# ]
# 返回 true
#
# 解释:
# 第一行和第一列都是“abcd”。
# 第二行和第二列都是“bnrt”。
# 第三行和第三列都是“crm”。
# 第四行和第四列都是“dt”。
#
# 因此，这是一个有效的单词广场.
# 给定
# [
#   "ball",
#   "area",
#   "read",
#   "lady"
# ]
# 返回 false
#
# 解释:
# 第三行是 "read" 但是第三列是 "lead".
#
# 因此，这不是一个有效的单词广场.

class Solution:
    """
    @param words: a list of string
    @return: a boolean
    """
    def validWordSquare(self, words):
        ls = []
        for i in words:
            ls.append(list(i))
        try:
            for i in range(len(ls)):
                word = ls[i]
                for j in range(len(word)):
                    if ls[i][j] != ls[j][i]:
                        return False
        except:
            return False
        return True






        # Write your code here

