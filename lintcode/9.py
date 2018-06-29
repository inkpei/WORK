# 描述
# 给你一个整数n. 从 1 到 n 按照下面的规则打印每个数：
#
# 如果这个数被3整除，打印fizz.
# 如果这个数被5整除，打印buzz.
# 如果这个数能同时被3和5整除，打印fizz buzz.
# 您在真实的面试中是否遇到过这个题？
# 样例
# 比如 n = 15, 返回一个字符串数组：
#
# [
#   "1", "2", "fizz",
#   "4", "buzz", "fizz",
#   "7", "8", "fizz",
#   "buzz", "11", "fizz",
#   "13", "14",
# ]
# 挑战
# Can you do it with only one if statement?
def fizzBuzz(n):
    res = []
    for i in range(1,n+1):
        if i % 3 == 0 or i % 5 == 0:
            if i % 3 == 0 and i % 5 == 0:
                res.append("fizz buzz")
            else:
                if i % 3 == 0:
                    res.append("fizz")
                else:
                    res.append("buzz")

        else:
            res.append(str(i))
    return res

if __name__ == '__main__':
    print(fizzBuzz(15))
