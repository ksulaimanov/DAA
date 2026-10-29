from solution import Solution
from tree_utils import build_tree


def wrong_any_node(root, target):
    stack = [(root, 0)]
    while stack:
        node, total = stack.pop()
        total += node.val
        if total == target:  # BUG: the path must end at a leaf
            return True
        for child in (node.left, node.right):
            if child:
                stack.append((child, total))
    return False


def wrong_prune(root, target):
    stack = [(root, 0)]
    while stack:
        node, total = stack.pop()
        total += node.val
        if total > target:  # BUG: negative values can bring the sum back down
            continue
        if node.left is None and node.right is None and total == target:
            return True
        for child in (node.left, node.right):
            if child:
                stack.append((child, total))
    return False


tree, target = [1, 2], 1
print(f"tree {tree}, target {target} (root is not a leaf, so the answer is False)")
print("  correct          :", Solution().hasPathSum(build_tree(tree), target))
print("  check every node :", wrong_any_node(build_tree(tree), target))

tree, target = [10, -5], 5
print(f"tree {tree}, target {target} (10 + -5 = 5, so the answer is True)")
print("  correct          :", Solution().hasPathSum(build_tree(tree), target))
print("  prune if sum > target:", wrong_prune(build_tree(tree), target))
