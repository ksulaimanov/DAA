from tree_utils import build_tree


def trace(root):
    best = 0
    stack = [(root, 1)]
    while stack:
        node, depth = stack.pop()
        best = max(best, depth)
        print(f"pop {node.val:>2} at depth {depth}   best={best}")
        for child in (node.left, node.right):
            if child:
                stack.append((child, depth + 1))
                print(f"     push {child.val:>2} with depth {depth + 1}")
    return best


if __name__ == "__main__":
    print("tree: [3, 9, 20, None, None, 15, 7]")
    print("result:", trace(build_tree([3, 9, 20, None, None, 15, 7])))
