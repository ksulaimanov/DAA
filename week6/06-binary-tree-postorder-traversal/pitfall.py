from solution import Solution
from tree_utils import build_tree


def reversed_normal_preorder(root):
    result, stack = [], [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:  # ordinary preorder: root, left, right
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    result.reverse()  # BUG: this gives right, left, root and not left, right, root
    return result


tree = [1, 2, 3]
print("tree:", tree)
print("root-right-left, reversed (mine)      :", Solution().postorderTraversal(build_tree(tree)))
print("ordinary preorder, reversed (wrong)   :", reversed_normal_preorder(build_tree(tree)))
