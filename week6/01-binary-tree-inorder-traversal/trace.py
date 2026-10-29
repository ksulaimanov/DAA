from tree_utils import build_tree


def names(nodes):
    return [n.val for n in nodes]


def trace(root):
    result, stack, curr = [], [], root
    while curr or stack:
        while curr:
            stack.append(curr)
            print(f"push {curr.val:>2}  (go left)   stack={names(stack)}")
            curr = curr.left
        curr = stack.pop()
        result.append(curr.val)
        print(f"pop  {curr.val:>2}  (visit)     stack={names(stack)}  result={result}")
        curr = curr.right
        print(f"     go right -> {curr.val if curr else None}")
    return result


if __name__ == "__main__":
    print("tree: [1, None, 2, 3]")
    print("result:", trace(build_tree([1, None, 2, 3])))
