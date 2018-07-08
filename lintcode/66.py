# 66. 二叉树的前序遍历
# 给出一棵二叉树，返回其节点值的前序遍历。
#
# 样例
# 给出一棵二叉树 {1,#,2,3},
#
#    1
#     \
#      2
#     /
#    3
#  返回 [1,2,3].
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
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        s = stack()
        p = root
        res = []
        while p != None or s.length != 0:
            while p != None:
                res.append(p.val)
                s.push(p)
                p = p.left
            p = s.pop().right

        return res
        # write your code here