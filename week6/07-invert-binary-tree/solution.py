from typing import Optional

from tree_utils import TreeNode, build_tree, random_tree, tree_to_list  # local helpers (LeetCode provides TreeNode itself)


# ===== paste from here into LeetCode =====
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        # both recursive calls finish before the assignment happens
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
# ===== end of the LeetCode part =====


def mirror(node):  # builds a new mirrored tree, used only for testing
    if node is None:
        return None
    return TreeNode(node.val, mirror(node.right), mirror(node.left))


if __name__ == "__main__":
    got = Solution().invertTree(build_tree([4, 2, 7, 1, 3, 6, 9]))
    assert tree_to_list(got) == [4, 7, 2, 9, 6, 3, 1]
    assert tree_to_list(Solution().invertTree(build_tree([2, 1, 3]))) == [2, 3, 1]
    assert Solution().invertTree(build_tree([])) is None
    for _ in range(500):
        t = random_tree(15)
        expected = tree_to_list(mirror(t))
        assert tree_to_list(Solution().invertTree(t)) == expected
    print("invert: all tests passed")
