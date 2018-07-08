#
# 68. 二叉树的后序遍历
# 给出一棵二叉树，返回其节点值的后序遍历。
#
# 样例
# 给出一棵二叉树 {1,#,2,3},
#
#    1
#     \
#      2
#     /
#    3
# 返回 [3,2,1]
#
# 挑战
# 你能使用非递归实现么？

class stack:
    def __init__(self):
        self.elem = []
        self.length = 0

    def push(self,number):
        self.elem.append(number)
        self.length += 1

    def pop(self):
        if self.length > 0:
            self.length -= 1
            k = self.elem[self.length]
            self.elem.pop(self.length)
            return k

    def top(self):
        if self.length > 0:
            return self.elem[self.length - 1]

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        s = stack()
        r = stack()
        p = root
        res = []
        while p != None or s.length != 0:
            while p != None:
                s.push(p)
                p = p.left
            p = s.pop()
            p = p.right

        return res