from tree_utils import build_tree, tree_to_list


def trace(node, depth=0):
    if node is None:
        return None
    pad = "  " * depth
    print(f"{pad}invert({node.val})")
    new_left = trace(node.right, depth + 1)
    new_right = trace(node.left, depth + 1)
    node.left, node.right = new_left, new_right
    left = node.left.val if node.left else None
    right = node.right.val if node.right else None
    print(f"{pad}swap done at {node.val}: left={left}, right={right}")
    return node


if __name__ == "__main__":
    tree = [4, 2, 7, 1, 3, 6, 9]
    print("tree:", tree)
    print("result:", tree_to_list(trace(build_tree(tree))))
