# 描述
# 给定一个列表，该列表中的每个要素要么是个列表，要么是整数。将其变成一个只包含整数的简单列表。
#
# 如果给定的列表中的要素本身也是一个列表，那么它也可以包含列表。
#
# 您在真实的面试中是否遇到过这个题？
# 样例
# 给定 [1,2,[1,2]]，返回 [1,2,1,2]。
#
# 给定 [4,[3,[2,[1]]]]，返回 [4,3,2,1]。
#
# 挑战
# 请用非递归方法尝试解答这道题。

def flatten(nestedList):
    # Write your code here
    # nestedList = []
    # print(nestedList[1][1])
    if type(nestedList) != type([]):
        return [nestedList]
    i = 0
    try:
        while True:
            if type(nestedList[i]) is type([]):
                if not nestedList[i]:
                    nestedList.remove(nestedList[i])
                    continue
                for j in range(0, len(nestedList[i])):
                    nestedList.insert(i + j + 1, nestedList[i][j])
                nestedList.remove(nestedList[i])
                i = i - 1
            i += 1
    except IndexError:
        return nestedList


if __name__ == '__main__':
    print(flatten())
