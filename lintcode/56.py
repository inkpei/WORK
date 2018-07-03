#
# 56. 两数之和
# 给一个整数数组，找到两个数使得他们的和等于一个给定的数 target。
#
# 你需要实现的函数twoSum需要返回这两个数的下标, 并且第一个下标小于第二个下标。注意这里下标的范围是 0 到 n-1。
#
# 样例
# 给出 numbers = [2, 7, 11, 15], target = 9, 返回 [0, 1].
#
# 挑战
# Either of the following solutions are acceptable:
#
# O(n) Space, O(nlogn) Time
# O(n) Space, O(n) Time

class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        dic = {}
        for i in range(len(numbers)):
            dic[i] = numbers[i]
        for i in dic.values():
            if target - dic[i] in dic.values():
                a = []
                for k,v in dic.items():
                    if v == target - dic[i]:
                        a.append(i)



if __name__ == '__main__':
    s = Solution()
    a = [0,4,3,0]
    b = 0
    print(s.twoSum(a,b))

        # write your code here