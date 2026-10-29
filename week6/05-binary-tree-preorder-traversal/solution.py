from typing import List, Optional

from tree_utils import TreeNode, build_tree, random_tree, tree_to_list  # local helpers (LeetCode provides TreeNode itself)


# ===== paste from here into LeetCode =====
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root is None:
            return result
        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)  # visit the node first
            if node.right:  # right goes in first ...
                stack.append(node.right)
            if node.left:  # ... so left comes out first
                stack.append(node.left)
        return result
# ===== end of the LeetCode part =====


def reference(node):  # recursive version, used only for testing
    if node is None:
        return []
    return [node.val] + reference(node.left) + reference(node.right)


if __name__ == "__main__":
    assert Solution().preorderTraversal(build_tree([1, None, 2, 3])) == [1, 2, 3]
    assert Solution().preorderTraversal(build_tree([])) == []
    assert Solution().preorderTraversal(build_tree([1])) == [1]
    for _ in range(500):
        t = random_tree(15)
        assert Solution().preorderTraversal(t) == reference(t), tree_to_list(t)
    print("preorder: all tests passed")
