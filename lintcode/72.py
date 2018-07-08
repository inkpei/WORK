# 72. 中序遍历和后序遍历树构造二叉树
# 根据中序遍历和后序遍历树构造二叉树
#
# 样例
# 给出树的中序遍历： [1,2,3] 和后序遍历： [1,3,2]
#
# 返回如下的树：
#
#   2
#
#  /  \
#
# 1    3

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param inorder: A list of integers that inorder traversal of a tree
    @param postorder: A list of integers that postorder traversal of a tree
    @return: Root of a tree
    """
    def buildTree(self, inorder, postorder):
        if len(inorder) == 0:
            return
        inbegin,inend = 0, len(inorder) -1
        postbegin,postend = 0,len(postorder) - 1

        return self.helper(inorder, postorder,inbegin,inend,postbegin,postend)

    def helper(self,inorder, postorder,inbegin,inend,postbegin,postend):
        root=TreeNode(postorder[postend])
        mid = inorder.index(postorder[postend])

        leftlen = mid-inbegin
        rightlen = inend - mid

        if leftlen > 0:
            leftchild = self.helper(inorder, postorder,inbegin,mid-1,postbegin,postbegin+leftlen-1)
            root.left = leftchild
        if rightlen > 0:
            rightlen = self.helper(inorder, postorder,mid+1,inend,postbegin + leftlen, postend - 1)
            root.right = rightlen
        return root

        # write your code here
