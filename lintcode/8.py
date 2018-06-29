# 描述
# 给定一个字符串和一个偏移量，根据偏移量旋转字符串(从左向右旋转)
#
# 您在真实的面试中是否遇到过这个题？
# 样例
# 对于字符串 "abcdefg".
#
# offset=0 => "abcdefg"
# offset=1 => "gabcdef"
# offset=2 => "fgabcde"
# offset=3 => "efgabcd"
# 挑战
# 在数组上原地旋转，使用O(1)的额外空间
def rotateString( str, offset):
    # write your code here
    s = list(str)
    l = len(s)
    offset = offset%l
    for i in range(0,int(l/2)):
        tmp = s[i]
        s[i] = s[l-1-i]
        s[l-1-i] = tmp
    for i in range(0,int(offset/2)):
        tmp = s[i]
        s[i] = s[offset - 1 -i]
        s[offset - 1 -i] = tmp
    for i in range(offset,int((l + offset)/2)):
        tmp = s[i]
        s[i] = s[l - 1-i+offset]
        s[l - 1-i+offset] = tmp
    return "".join(s)



if __name__ == '__main__':
    print(rotateString("abcdefg", 3))