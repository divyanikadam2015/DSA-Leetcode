class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        l = r = root
        left = right = 0

        while l:
            left += 1
            l = l.left

        while r:
            right += 1
            r = r.right

        if left == right:
            return (1 << left) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)