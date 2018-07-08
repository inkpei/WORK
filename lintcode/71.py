#
# 71. 二叉树的锯齿形层次遍历
# 给出一棵二叉树，返回其节点值的锯齿形层次遍历（先从左往右，下一层再从右往左，层与层之间交替进行）
#
# 样例
# 给出一棵二叉树 {3,9,20,#,#,15,7},
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其锯齿形的层次遍历为：
#
# [
#   [3],
#   [20,9],
#   [15,7]
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

    def zigzagLevelOrder(self, root):
        if root == None:
            return []
        q = queue()
        q.push(root)
        res = []
        flag = 1
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
            if flag == -1:
                tmp.reverse()
            flag = -flag
            res.append(tmp)
        return res