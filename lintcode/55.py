# 55. 比较字符串
# 比较两个字符串A和B，确定A中是否包含B中所有的字符。字符串A和B中的字符都是 大写字母
#
# 样例
# 给出 A = "ABCD" B = "ACD"，返回 true
#
# 给出 A = "ABCD" B = "AABC"， 返回 false

class Solution:
    """
    @param A: A string
    @param B: A string
    @return: if string A contains all of the characters in B return true else return false
    """
    def compareStrings(self, A, B):
        a = list(A)
        b = list(B)
        for i in b:
            if i not in a:
                return False
            else:
                for j in range(len(a)):
                    if a[j] == i:
                        break
                a.pop(j)
        return True
        # write your code here

if __name__ == '__main__':
    s = Solution()
    A = "ABC"
    B = "A"
    print(s.compareStrings(A,B))
