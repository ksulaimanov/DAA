from solution import Solution
from tree_utils import build_tree, tree_to_list


def wrong_invert(root):
    if root is None:
        return None
    root.left = wrong_invert(root.right)
    root.right = wrong_invert(root.left)  # BUG: root.left was already overwritten
    return root


tree = [4, 2, 7, 1, 3, 6, 9]
print("tree:", tree)
print("correct                       :", tree_to_list(Solution().invertTree(build_tree(tree))))
print("two separate assignments (bug):", tree_to_list(wrong_invert(build_tree(tree))))
