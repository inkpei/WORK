# 53. 翻转字符串
# 给定一个字符串，逐个翻转字符串中的每个单词。

class Solution:
    """
    @param: s: A string
    @return: A string
    """


    def reverseWords(self, s):

        s = list(s)
        p = s[0]
        res = []
        tmp = []
        for i in s:
            if i == ' ' and p == ' ':
                continue
            else:
                if i == ' ':
                    res = [' '] + tmp + res
                    tmp = []
                    p = ' '
                else:
                    tmp.append(i)
                    p = i
        t = ""
        for i in res[1:]:
            t += i
        return t



        # write your code here
if __name__ == '__main__':
    s = Solution()
    st = "      list dsfjgs dfg    "
    print(st.split(' '))
    # print(s.reverseWords(st))