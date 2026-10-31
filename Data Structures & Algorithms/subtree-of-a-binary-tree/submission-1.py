# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isEqual(self, root, subRoot):

        queue = deque([(root, subRoot)])

        while queue:
            
            left, right = queue.popleft()
            
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            
            queue.append((left.left, right.left))
            queue.append((left.right, right.right))

        return True
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if self.isEqual(node, subRoot):
                return True
            else:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return False
