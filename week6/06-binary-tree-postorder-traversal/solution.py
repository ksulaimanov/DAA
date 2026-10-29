from typing import List, Optional

from tree_utils import TreeNode, build_tree, random_tree, tree_to_list  # local helpers (LeetCode provides TreeNode itself)


# ===== paste from here into LeetCode =====
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root is None:
            return result
        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)  # order of visits: root, right, left
            if node.left:  # left goes in first ...
                stack.append(node.left)
            if node.right:  # ... so right comes out first
                stack.append(node.right)
        result.reverse()  # reversed: left, right, root = postorder
        return result
# ===== end of the LeetCode part =====


def reference(node):  # recursive version, used only for testing
    if node is None:
        return []
    return reference(node.left) + reference(node.right) + [node.val]


if __name__ == "__main__":
    assert Solution().postorderTraversal(build_tree([1, None, 2, 3])) == [3, 2, 1]
    assert Solution().postorderTraversal(build_tree([1, 2, 3])) == [2, 3, 1]
    assert Solution().postorderTraversal(build_tree([])) == []
    assert Solution().postorderTraversal(build_tree([1])) == [1]
    for _ in range(500):
        t = random_tree(15)
        assert Solution().postorderTraversal(t) == reference(t), tree_to_list(t)
    print("postorder: all tests passed")
