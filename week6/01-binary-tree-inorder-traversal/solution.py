from typing import List, Optional

from tree_utils import TreeNode, build_tree, random_tree, tree_to_list  # local helpers (LeetCode provides TreeNode itself)


# ===== paste from here into LeetCode =====
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        curr = root
        while curr or stack:
            while curr:  # go left as far as possible
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()  # the leftmost node that is not visited yet
            result.append(curr.val)  # visit it
            curr = curr.right  # then handle its right subtree
        return result
# ===== end of the LeetCode part =====


def reference(node):  # simple recursive version, used only for testing
    if node is None:
        return []
    return reference(node.left) + [node.val] + reference(node.right)


if __name__ == "__main__":
    assert Solution().inorderTraversal(build_tree([1, None, 2, 3])) == [1, 3, 2]
    assert Solution().inorderTraversal(build_tree([])) == []
    assert Solution().inorderTraversal(build_tree([1])) == [1]
    for _ in range(500):
        t = random_tree(15)
        assert Solution().inorderTraversal(t) == reference(t), tree_to_list(t)
    print("inorder: all tests passed")
