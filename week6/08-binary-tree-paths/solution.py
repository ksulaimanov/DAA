from typing import List, Optional

from tree_utils import TreeNode, build_tree, random_tree, tree_to_list  # local helpers (LeetCode provides TreeNode itself)


# ===== paste from here into LeetCode =====
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        path = []  # values on the way from the root to the current node

        def dfs(node):
            path.append(str(node.val))
            if node.left is None and node.right is None:
                result.append("->".join(path))  # a leaf: save the whole path
            else:
                if node.left:
                    dfs(node.left)
                if node.right:
                    dfs(node.right)
            path.pop()  # backtrack: leave the node

        if root:
            dfs(root)
        return result
# ===== end of the LeetCode part =====


def reference(node):  # builds the strings bottom-up, used only for testing
    if node is None:
        return []
    if node.left is None and node.right is None:
        return [str(node.val)]
    return [str(node.val) + "->" + p for p in reference(node.left) + reference(node.right)]


if __name__ == "__main__":
    assert Solution().binaryTreePaths(build_tree([1, 2, 3, None, 5])) == ["1->2->5", "1->3"]
    assert Solution().binaryTreePaths(build_tree([1])) == ["1"]
    assert Solution().binaryTreePaths(build_tree([])) == []
    for _ in range(500):
        t = random_tree(15)
        assert Solution().binaryTreePaths(t) == reference(t), tree_to_list(t)
    print("tree paths: all tests passed")
