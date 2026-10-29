from typing import Optional

from tree_utils import TreeNode, build_tree, random_tree, tree_to_list  # local helpers (LeetCode provides TreeNode itself)


# ===== paste from here into LeetCode =====
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        best = 0
        stack = [(root, 1)]  # (node, depth of this node)
        while stack:
            node, depth = stack.pop()
            best = max(best, depth)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        return best
# ===== end of the LeetCode part =====


def reference(node):  # recursive version, used only for testing
    if node is None:
        return 0
    return 1 + max(reference(node.left), reference(node.right))


if __name__ == "__main__":
    assert Solution().maxDepth(build_tree([3, 9, 20, None, None, 15, 7])) == 3
    assert Solution().maxDepth(build_tree([1, None, 2])) == 2
    assert Solution().maxDepth(build_tree([])) == 0
    for _ in range(500):
        t = random_tree(20)
        assert Solution().maxDepth(t) == reference(t), tree_to_list(t)
    print("max depth: all tests passed")
