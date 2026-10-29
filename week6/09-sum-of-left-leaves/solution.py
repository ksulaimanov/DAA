from typing import Optional

from tree_utils import TreeNode, build_tree, random_tree, tree_to_list  # local helpers (LeetCode provides TreeNode itself)


# ===== paste from here into LeetCode =====
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        total = 0
        stack = [root] if root else []
        while stack:
            node = stack.pop()
            left = node.left
            # a leaf cannot know that it is a left child, so look from the parent
            if left and left.left is None and left.right is None:
                total += left.val
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return total
# ===== end of the LeetCode part =====


def reference(node, is_left=False):  # recursive version, used only for testing
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return node.val if is_left else 0
    return reference(node.left, True) + reference(node.right, False)


if __name__ == "__main__":
    assert Solution().sumOfLeftLeaves(build_tree([3, 9, 20, None, None, 15, 7])) == 24
    assert Solution().sumOfLeftLeaves(build_tree([1])) == 0
    assert Solution().sumOfLeftLeaves(build_tree([1, 2, 3, 4, 5])) == 4
    for _ in range(500):
        t = random_tree(20)
        if t is None:
            continue
        assert Solution().sumOfLeftLeaves(t) == reference(t), tree_to_list(t)
    print("left leaves: all tests passed")
