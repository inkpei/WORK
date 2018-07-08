# 12. 带最小值操作的栈
# 实现一个带有取最小值min方法的栈，min方法将返回当前栈中的最小值。
#
# 你实现的栈将支持push，pop 和 min 操作，所有操作要求都在O(1)时间内完成。
#
# 样例
# 如下操作：push(1)，pop()，push(2)，push(3)，min()， push(1)，min() 返回 1，2，1


class MinStack:
    stack = []
    length = 0
    min_num = []

    def __init__(self):
        pass


    # do intialization if necessary

    """
    @param: number: An integer
    @return: nothing
    """

    def push(self, number):

        self.stack.append(number)
        self.min_num.append(number)
        self.min_num.sort()
        self.length += 1
        # print(self.stack,self.length)


    # write your code here

    """
    @return: An integer
    """

    def pop(self):
        if self.length > 0:
            k = self.stack[self.length - 1]

            for i in range(0,self.length):

                if self.min_num[i] == k:
                    self.min_num.pop(i)
                    break
            self.stack.pop(self.length-1)
            self.length -= 1
            return k
        return None

    # write your code here

    """
    @return: An integer
    """

    def min(self):
        if self.min_num:
            return self.min_num[0]
        return None
# write your code here

if __name__ == '__main__':
    s = MinStack()
    s.push(-1)
    s.push(-2)
    s.min()
    s.pop()
    s.push(-3)
    s.push(3)
    s.push(2)
    s.pop()
