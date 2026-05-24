# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = []
        q.append(root)
        if not root:
            return res
        while q:
            queLen = len(q)
            for i in range(0, queLen):
                node = q.pop(0)

                if i == (queLen-1):    #if it is the right sided node
                    res.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return res

        