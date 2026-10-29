from solution import Solution
from tree_utils import build_tree


def paths_without_backtracking(root):
    result, path = [], []

    def dfs(node):
        path.append(str(node.val))
        if node.left is None and node.right is None:
            result.append("->".join(path))
        else:
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        # BUG: no path.pop() here

    dfs(root)
    return result


tree = [1, 2, 3, None, 5]
print("tree:", tree)
print("with path.pop()    :", Solution().binaryTreePaths(build_tree(tree)))
print("without path.pop() :", paths_without_backtracking(build_tree(tree)))
