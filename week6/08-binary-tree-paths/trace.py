from tree_utils import build_tree


def trace(root):
    result, path = [], []

    def dfs(node, depth):
        pad = "  " * depth
        path.append(str(node.val))
        print(f"{pad}enter {node.val}   path={path}")
        if node.left is None and node.right is None:
            result.append("->".join(path))
            print(f"{pad}  leaf -> save {result[-1]!r}")
        else:
            if node.left:
                dfs(node.left, depth + 1)
            if node.right:
                dfs(node.right, depth + 1)
        path.pop()
        print(f"{pad}leave {node.val}   path={path}")

    dfs(root, 0)
    return result


if __name__ == "__main__":
    print("tree: [1, 2, 3, None, 5]")
    print("result:", trace(build_tree([1, 2, 3, None, 5])))
