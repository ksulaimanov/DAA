from tree_utils import build_tree


def trace(values):
    print("tree:", values)
    order, stack = [], [build_tree(values)]
    while stack:
        node = stack.pop()
        order.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
        print(f"  visit {node.val}   order={order}   stack={[n.val for n in stack]}")
    print("  root-right-left order :", order)
    order.reverse()
    print("  reversed = postorder  :", order)
    return order


if __name__ == "__main__":
    trace([1, None, 2, 3])
    print()
    trace([1, 2, 3])
