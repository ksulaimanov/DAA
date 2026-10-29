from solution import Solution
from tree_utils import build_tree, tree_to_list


def wrong_merge(a, b):
    if a is None or b is None:  # BUG: should return the other tree, not None
        return None
    a.val += b.val
    a.left = wrong_merge(a.left, b.left)
    a.right = wrong_merge(a.right, b.right)
    return a


t1 = [1, 3, 2, 5]
t2 = [2, 1, 3, None, 4, None, 7]
print("tree 1:", t1)
print("tree 2:", t2)
print("mine                            :", tree_to_list(Solution().mergeTrees(build_tree(t1), build_tree(t2))))
print("return None if one side is empty:", tree_to_list(wrong_merge(build_tree(t1), build_tree(t2))))
