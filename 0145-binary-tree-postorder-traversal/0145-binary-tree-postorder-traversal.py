class Solution:
    def postorderTraversal(self, root):
        result = []

        def dfs(node):
            if node is None:
                return

            dfs(node.left)
            dfs(node.right)
            result.append(node.val)

        dfs(root)

        return result