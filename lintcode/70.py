# 70. 二叉树的层次遍历 II
# 给出一棵二叉树，返回其节点值从底向上的层次序遍历（按从叶节点所在层到根节点所在的层遍历，然后逐层从左往右遍历）
#
# 样例
# 给出一棵二叉树 {3,9,20,#,#,15,7},
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 按照从下往上的层次遍历为：
#
# [
#   [15,7],
#   [9,20],
#   [3]
# ]
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

    def levelOrderBottom(self, root):
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
            res.insert(0,tmp)
        return res