# 73. 前序遍历和中序遍历树构造二叉树
# 根据前序遍历和中序遍历树构造二叉树.
#
# 样例
# 给出中序遍历：[1,2,3]和前序遍历：[2,1,3]. 返回如下的树:
#
#   2
#  / \
# 1   3


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param inorder: A list of integers that inorder traversal of a tree
    @param preorder: A list of integers that preorder traversal of a tree
    @return: Root of a tree
    """
    def buildTree(self, preorder, inorder):
        # write your code here
        if len(inorder) is 0 and len(preorder) is 0:
            return None
        if len(inorder) is 1:  
            return TreeNode(inorder[0])
        root = TreeNode(preorder[0])
        index = inorder.index(root.val)
        inl = inorder[:index]
        inr = inorder[index+1:]
        prel = []
        prer = []
        for i in range(len(preorder)):
            if preorder[i] in inl:
                prel.append(preorder[i])
            elif preorder[i] in inr:
                prer.append(preorder[i])
        root.left = self.buildTree(prel, inl)
        root.right = self.buildTree(prer, inr)
        return root