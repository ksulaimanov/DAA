from tree_utils import build_tree


def trace(root):
    result, stack = [], [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        print(f"pop {node.val:>2} -> visit   result={result}")
        if node.right:
            stack.append(node.right)
            print(f"     push right {node.right.val}")
        if node.left:
            stack.append(node.left)
            print(f"     push left  {node.left.val}")
        print(f"     stack={[n.val for n in stack]}")
    return result


if __name__ == "__main__":
    print("tree: [1, None, 2, 3]")
    print("result:", trace(build_tree([1, None, 2, 3])))
