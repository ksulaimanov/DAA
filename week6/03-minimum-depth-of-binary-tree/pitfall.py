from solution import Solution
from tree_utils import build_tree


def wrong_min_depth(node):
    if node is None:
        return 0
    # BUG: a missing child counts as depth 0, but a node with one child is not a leaf
    return 1 + min(wrong_min_depth(node.left), wrong_min_depth(node.right))


tree = [2, None, 3, None, 4, None, 5, None, 6]
print("tree:", tree)
print("1 + min(left, right):", wrong_min_depth(build_tree(tree)))
print("BFS (my solution)   :", Solution().minDepth(build_tree(tree)))
