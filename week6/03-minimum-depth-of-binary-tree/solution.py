from collections import deque
from typing import Optional

from tree_utils import TreeNode, build_tree, random_tree, tree_to_list  # local helpers (LeetCode provides TreeNode itself)


# ===== paste from here into LeetCode =====
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        queue = deque([(root, 1)])  # (node, depth of this node)
        while queue:
            node, depth = queue.popleft()
            if node.left is None and node.right is None:
                return depth  # BFS reaches the shallowest leaf first
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
# ===== end of the LeetCode part =====


def reference(node):  # recursive version with the one-child special case
    if node is None:
        return 0
    if node.left is None:
        return 1 + reference(node.right)
    if node.right is None:
        return 1 + reference(node.left)
    return 1 + min(reference(node.left), reference(node.right))


if __name__ == "__main__":
    assert Solution().minDepth(build_tree([3, 9, 20, None, None, 15, 7])) == 2
    assert Solution().minDepth(build_tree([2, None, 3, None, 4, None, 5, None, 6])) == 5
    assert Solution().minDepth(build_tree([])) == 0
    for _ in range(500):
        t = random_tree(20)
        assert Solution().minDepth(t) == reference(t), tree_to_list(t)
    print("min depth: all tests passed")
