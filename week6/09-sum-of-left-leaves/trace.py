from tree_utils import build_tree


def trace(root):
    total, stack = 0, [root]
    while stack:
        node = stack.pop()
        left = node.left
        if left and left.left is None and left.right is None:
            total += left.val
            print(f"node {node.val:>2}: left child {left.val} is a leaf -> total={total}")
        else:
            shown = left.val if left else None
            print(f"node {node.val:>2}: left child is {shown} (not a left leaf) -> total={total}")
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return total


if __name__ == "__main__":
    print("tree: [3, 9, 20, None, None, 15, 7]")
    print("result:", trace(build_tree([3, 9, 20, None, None, 15, 7])))
