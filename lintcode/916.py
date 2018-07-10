# 916. 回文排列
# 给定一个字符串，判断字符串是否存在一个排列是回文排列。
#
# 样例
# 给定s = "code", 返回 False.
# 给定s = "aab", 返回 True.
# 给定s = "carerac", 返回 True.

class Solution:
    """
    @param s: the given string
    @return: if a permutation of the string could form a palindrome
    """
    def canPermutePalindrome(self, s):
        a = list(s)
        dic = []
        for i in a:
            if i not in dic:
                dic.append(i)
            else:
                dic.remove(i)
        return len(dic) <= 1


if __name__ == '__main__':
    s = Solution()
    str = "aab"
    print(s.canPermutePalindrome(str))

        # write your code here
