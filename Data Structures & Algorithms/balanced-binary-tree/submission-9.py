# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            return 1 + max(left, right)

        

        
        leftheight = dfs(root.left)
        rightheight = dfs(root.right)

        if abs(leftheight - rightheight) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        