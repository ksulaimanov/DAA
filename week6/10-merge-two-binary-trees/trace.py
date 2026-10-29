from tree_utils import build_tree, tree_to_list


def trace(values1, values2):
    root1, root2 = build_tree(values1), build_tree(values2)
    stack = [(root1, root2)]
    while stack:
        a, b = stack.pop()
        print(f"pair a={a.val}, b={b.val}: a.val becomes {a.val + b.val}")
        a.val += b.val
        for side in ("left", "right"):
            ca, cb = getattr(a, side), getattr(b, side)
            if ca and cb:
                stack.append((ca, cb))
                print(f"   {side:<5}: both have a child -> push pair ({ca.val}, {cb.val})")
            elif cb:
                setattr(a, side, cb)
                print(f"   {side:<5}: only b has {cb.val} -> attach b's subtree to a")
            elif ca:
                print(f"   {side:<5}: only a has {ca.val} -> keep it")
            else:
                print(f"   {side:<5}: no children")
    return tree_to_list(root1)


if __name__ == "__main__":
    t1 = [1, 3, 2, 5]
    t2 = [2, 1, 3, None, 4, None, 7]
    print("tree 1:", t1)
    print("tree 2:", t2)
    print("result:", trace(t1, t2))
