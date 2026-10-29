from solution import Solution
from tree_utils import build_tree


def inorder_forgot_right(root):
    result, stack, curr = [], [], root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        result.append(curr.val)
        curr = None  # BUG: should be curr = curr.right
    return result


tree = [1, None, 2, 3]
print("tree:", tree)
print("correct           :", Solution().inorderTraversal(build_tree(tree)))
print("forgot node.right :", inorder_forgot_right(build_tree(tree)))
