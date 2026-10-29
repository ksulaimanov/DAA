from tree_utils import build_tree


def trace(root, target):
    stack = [(root, target)]
    while stack:
        node, remaining = stack.pop()
        remaining -= node.val
        is_leaf = node.left is None and node.right is None
        print(f"pop {node.val:>2}: remaining after it = {remaining:>3}   leaf={is_leaf}")
        if is_leaf and remaining == 0:
            print("     leaf and remaining == 0 -> True")
            return True
        if node.right:
            stack.append((node.right, remaining))
        if node.left:
            stack.append((node.left, remaining))
    return False


if __name__ == "__main__":
    tree = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
    print("tree:", tree, " target: 22")
    print("result:", trace(build_tree(tree), 22))
