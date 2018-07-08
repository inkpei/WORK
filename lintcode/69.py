# 69. 二叉树的层次遍历
# 给出一棵二叉树，返回其节点值的层次遍历（逐层从左往右访问）
#
# 样例
# 给一棵二叉树 {3,9,20,#,#,15,7} ：
#
#   3
#  / \
# 9  20
#   /  \
#  15   7
# 返回他的分层遍历结果：
#
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
# 挑战
# 挑战1：只使用一个队列去实现它
#
# 挑战2：用DFS算法来做

class queue:
    def __init__(self):
        self.elem = []
        self.length = 0

    def push(self,s):
        self.elem.append(s)
        self.length += 1

    def pop(self):
        if self.length > 0:
            self.length -= 1
            k = self.elem[0]
            self.elem.pop(0)
            return k
    def empty(self):
        return self.length == 0
    def top(self):
        if self.length > 0:
            return self.elem[0]


class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        if root == None:
            return []
        q = queue()
        q.push(root)
        res = []
        while q.length != 0:
            length = q.length
            tmp = []
            for i in range(length):
                r = q.pop()
                if r.left:
                    q.push(r.left)
                if r.right:
                    q.push(r.right)
                tmp.append(r.val)
            res.append(tmp)
        return res

        # write your code here



