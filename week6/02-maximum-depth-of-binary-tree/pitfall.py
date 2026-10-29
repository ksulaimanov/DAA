from solution import Solution
from tree_utils import TreeNode


def recursive_depth(node):
    if node is None:
        return 0
    return 1 + max(recursive_depth(node.left), recursive_depth(node.right))


# a "linked list" tree: every node has only a right child
root = TreeNode(0)
cur = root
for i in range(1, 5000):
    cur.right = TreeNode(i)
    cur = cur.right

print("tree: a chain of 5000 nodes")
try:
    print("recursive:", recursive_depth(root))
except RecursionError as e:
    print("recursive: RecursionError:", e)
print("iterative:", Solution().maxDepth(root))
