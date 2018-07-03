#
# 1017. Similar RGB Color
# In the following, every capital letter represents some hexadecimal digit from 0 to f.
#
# The red-green-blue color "#AABBCC" can be written as "#ABC" in shorthand. For example, "#15c" is shorthand for the color "#1155cc".
#
# Now, say the similarity between two colors "#ABCDEF" and "#UVWXYZ" is -(AB - UV)^2 - (CD - WX)^2 - (EF - YZ)^2.
#
# Given the color "#ABCDEF", return a 7 character color that is most similar to #ABCDEF, and has a shorthand (that is, it can be represented as some "#XYZ")
#
# 样例
# Input: color = "#09f166"
# Output: "#11ee66"
# Explanation:
# The similarity is -(0x09 - 0x11)^2 -(0xf1 - 0xee)^2 - (0x66 - 0x66)^2 = -64 -9 -0 = -73.
# This is the highest among any shorthand color.


class Solution:
    """
    @param color: the given color
    @return: a 7 character color that is most similar to the given color
    """
    def cala(self,s):
        if s[0] == s[1]:
            return s
        m = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        t = [s[0],s[0]]
        a = m.index(s[0])*16 + m.index(s[1])
        b = m.index(t[0])*16 + m.index(t[1])
        if abs(a-b) < 9:
            return t
        else:
            if a > b :
                return [m[m.index(s[0])+1],m[m.index(s[0])+1]]
            else:
                return [m[m.index(s[0])-1],m[m.index(s[0])-1]]

    def similarRGB(self, color):

        if len(color) != 7:
            return color
        s = list(color)[1:]
        # print(s)
        res = ""
        while s != []:
            tmp = s[0:2]
            s = s [2:]

            k = self.cala(tmp)
            for i in k :
                res += i
        return "#"+res





if __name__ == '__main__':
    k = "#09f166"
    s = Solution()
    print(s.similarRGB(k))

        # Write your code here