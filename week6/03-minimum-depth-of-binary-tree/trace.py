from collections import deque

from tree_utils import build_tree


def trace(root):
    queue = deque([(root, 1)])
    while queue:
        node, depth = queue.popleft()
        if node.left is None and node.right is None:
            print(f"pop {node.val:>2} at depth {depth}: it is a leaf -> answer {depth}")
            return depth
        print(f"pop {node.val:>2} at depth {depth}: not a leaf, push its children")
        for child in (node.left, node.right):
            if child:
                queue.append((child, depth + 1))
        print(f"     queue={[(n.val, d) for n, d in queue]}")


if __name__ == "__main__":
    print("tree: [3, 9, 20, None, None, 15, 7]")
    print("result:", trace(build_tree([3, 9, 20, None, None, 15, 7])))
