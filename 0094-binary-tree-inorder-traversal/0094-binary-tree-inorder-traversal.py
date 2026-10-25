class Solution:
    def inorderTraversal(self, root):
        result = []

        def dfs(node):
            if node is None:
                return

            dfs(node.left)       # 1. Visit left subtree
            result.append(node.val)  # 2. Visit root
            dfs(node.right)      # 3. Visit right subtree

        dfs(root)
        return result
