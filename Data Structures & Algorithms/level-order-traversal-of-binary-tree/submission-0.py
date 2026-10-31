# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([[root]])
        return_list = []
        while queue:
            r = []
            nodes = []
            level = queue.popleft()
            for node in level:
                r.append(node.val)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            return_list.append(r)
            if nodes:
                queue.append(nodes)
        return return_list   