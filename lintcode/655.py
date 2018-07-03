#
# 655. Add Strings
# 以字符串的形式给出两个非负整数 num1 和 num2，返回 num1 和 num2 的和。
#
# 样例
# 给定 num1 = "123"，num2 = "45"
# 返回 "168"


class Solution:
    """
    @param num1: a non-negative integers
    @param num2: a non-negative integers
    @return: return sum of num1 and num2
    """
    def addStrings(self, num1, num2):
        a = num1 if len(num1) > len(num2) else num2
        b = num1 if len(num1) <= len(num2) else num2
        a = [int(x) for x in list(a)]
        b = [int(x) for x in list(b)]
        l1 = len(a)
        l2 = len(b)
        for i in range(l1 - l2,l1):
            a[i] += b[i-(l1-l2)]
        for i in range(1,l1)[::-1]:
            if a[i] > 9:
                a[i] -= 10
                a[i - 1] += 1
        if a[0] > 9:
            a[0] -= 10
            a.insert(0,1)
        res = ""
        for i in a:
            res += str(i)

        return res


if __name__ == '__main__':

    s = Solution()
    num1 = "19999999"
    num2 = "1"
    print(s.addStrings(num1,num2))

        # write your code here