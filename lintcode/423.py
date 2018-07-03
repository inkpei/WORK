#
# 423. 有效的括号序列
# 给定一个字符串所表示的括号序列，包含以下字符： '(', ')', '{', '}', '[' and ']'， 判定是否是有效的括号序列。
#
# 样例
# 括号必须依照 "()" 顺序表示， "()[]{}" 是有效的括号，但 "([)]"则是无效的括号。

class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """

    def isValidParentheses(self, s):
        s = list(s)
        # print(s)
        stack = []
        left = ['(', '{', '[']
        right = [')', '}', ']']
        for i in s:
            if i in left:
                stack.append(i)
            if i in right:
                if stack != [] and stack[len(stack) - 1] == left[right.index(i)]:
                    stack.pop(len(stack) - 1)
                else:
                    return False
        return stack == []

        # write your code here


if __name__ == '__main__':
    s = Solution()

    k = "]"
    print(s.isValidParentheses(k))
