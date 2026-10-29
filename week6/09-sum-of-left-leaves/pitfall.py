from solution import Solution
from tree_utils import build_tree


def sum_all_left_children(root):
    total, stack = 0, [root]
    while stack:
        node = stack.pop()
        if node.left:
            total += node.left.val  # BUG: the left child may have children
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return total


def sum_all_leaves(root):
    total, stack = 0, [root]
    while stack:
        node = stack.pop()
        if node.left is None and node.right is None:
            total += node.val  # BUG: right leaves are counted too
        for child in (node.left, node.right):
            if child:
                stack.append(child)
    return total


tree = [1, 2, 3, 4, 5]
print("tree:", tree, "(the only left leaf is 4)")
print("correct                  :", Solution().sumOfLeftLeaves(build_tree(tree)))
print("sum of all left children :", sum_all_left_children(build_tree(tree)))
print("sum of all leaves        :", sum_all_leaves(build_tree(tree)))
