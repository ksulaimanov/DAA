from typing import Optional

from tree_utils import TreeNode, build_tree, random_tree, tree_to_list  # local helpers (LeetCode provides TreeNode itself)


# ===== paste from here into LeetCode =====
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        stack = [(root, targetSum)]  # (node, what is still needed before this node)
        while stack:
            node, remaining = stack.pop()
            remaining -= node.val
            if node.left is None and node.right is None and remaining == 0:
                return True  # a root-to-leaf path with the needed sum
            if node.right:
                stack.append((node.right, remaining))
            if node.left:
                stack.append((node.left, remaining))
        return False
# ===== end of the LeetCode part =====


def path_sums(node, acc=0):  # all root-to-leaf sums, used only for testing
    if node is None:
        return []
    acc += node.val
    if node.left is None and node.right is None:
        return [acc]
    return path_sums(node.left, acc) + path_sums(node.right, acc)


if __name__ == "__main__":
    big = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
    assert Solution().hasPathSum(build_tree(big), 22) is True
    assert Solution().hasPathSum(build_tree([1, 2, 3]), 5) is False
    assert Solution().hasPathSum(build_tree([]), 0) is False
    assert Solution().hasPathSum(build_tree([1, 2]), 1) is False
    for _ in range(500):
        t = random_tree(15)
        sums = path_sums(t)
        for target in range(-30, 31, 3):
            assert Solution().hasPathSum(t, target) == (target in sums), (tree_to_list(t), target)
        for s in sums:
            assert Solution().hasPathSum(t, s) is True
    print("path sum: all tests passed")
