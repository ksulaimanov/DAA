from solution import Solution
from tree_utils import build_tree


def preorder_wrong_order(root):
    result, stack = [], [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.left:  # BUG: pushing left first means right is popped first
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return result


tree = [1, 2, 3]
print("tree:", tree)
print("push right, then left :", Solution().preorderTraversal(build_tree(tree)))
print("push left, then right :", preorder_wrong_order(build_tree(tree)))
