# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        queue = deque([(p, q)])

        while queue:
            left, right = queue.popleft()

            if not left and not right:
                continue
            
            if left and not right:
                return False
            
            if right and not left:
                return False

            if left.val != right.val:
                return False
            
            queue.append((left.left, right.left))
            queue.append((left.right, right.right))
        
        return True
