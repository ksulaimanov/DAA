import random
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    # LeetCode level-order format, for example [1, None, 2, 3]
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def tree_to_list(root):
    # the inverse of build_tree (trailing None values are removed)
    if root is None:
        return []
    out = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            out.append(None)
        else:
            out.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
    while out and out[-1] is None:
        out.pop()
    return out


def random_tree(max_nodes, low=-9, high=9):
    # random binary tree with 0..max_nodes nodes, used by the self-tests
    n = random.randint(0, max_nodes)
    if n == 0:
        return None
    root = TreeNode(random.randint(low, high))
    slots = [(root, "left"), (root, "right")]
    for _ in range(n - 1):
        parent, side = slots.pop(random.randrange(len(slots)))
        child = TreeNode(random.randint(low, high))
        setattr(parent, side, child)
        slots.append((child, "left"))
        slots.append((child, "right"))
    return root
