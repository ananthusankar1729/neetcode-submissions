# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        l = []
        que = []
        que.append(root)

        while que:
            qlen = len(que)
            lev = []
            for i in range(qlen):
                node = que.pop(0)
                if node:
                    lev.append(node.val)
                    que.append(node.left)
                    que.append(node.right)
            if lev:
                l.append(lev)
        return l


        