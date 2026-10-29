from typing import Optional

from tree_utils import TreeNode, build_tree, random_tree, tree_to_list  # local helpers (LeetCode provides TreeNode itself)


# ===== paste from here into LeetCode =====
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        stack = [(root1, root2)]  # pairs of nodes that exist in both trees
        while stack:
            a, b = stack.pop()
            a.val += b.val
            if a.left and b.left:
                stack.append((a.left, b.left))
            elif b.left:  # a has no left child: take the whole subtree of b
                a.left = b.left
            if a.right and b.right:
                stack.append((a.right, b.right))
            elif b.right:
                a.right = b.right
        return root1  # the first tree is changed in place
# ===== end of the LeetCode part =====


def reference(a, b):  # builds a new tree recursively, used only for testing
    if a is None and b is None:
        return None
    node = TreeNode((a.val if a else 0) + (b.val if b else 0))
    node.left = reference(a.left if a else None, b.left if b else None)
    node.right = reference(a.right if a else None, b.right if b else None)
    return node


if __name__ == "__main__":
    t1 = build_tree([1, 3, 2, 5])
    t2 = build_tree([2, 1, 3, None, 4, None, 7])
    assert tree_to_list(Solution().mergeTrees(t1, t2)) == [3, 4, 5, 5, 4, None, 7]
    assert tree_to_list(Solution().mergeTrees(build_tree([1]), build_tree([1, 2]))) == [2, 2]
    assert Solution().mergeTrees(build_tree([]), build_tree([])) is None
    for _ in range(500):
        a, b = random_tree(12), random_tree(12)
        expected = tree_to_list(reference(a, b))
        a2, b2 = build_tree(tree_to_list(a)), build_tree(tree_to_list(b))
        assert tree_to_list(Solution().mergeTrees(a2, b2)) == expected, (tree_to_list(a), tree_to_list(b))
    print("merge trees: all tests passed")
