import json
from collections import deque


def get_leaf(root=2, height=6, left_branch=lambda l_r: l_r*3, right_branch=lambda r_r: r_r+4):
    """
    получает на вход корень дерева, высоту дерева и функции для левой и правой веток
    возвращает список всех листьев дерева в неупорядоченном виде

    > get_leaf(2, 2, lambda l_r: l_r*3, lambda r_r: r_r+4)

    [2, 6, 6, 18, 10, 18, 10]
    """
    leafs = [root]
    vspom = []
    for i in range(height):
        if i == 0:
            vspom.append(left_branch(leafs[-1]))
            vspom.append(right_branch(leafs[-1]))
        else:
            for j in range(1, 2**i+1):
                vspom.append(left_branch(leafs[-j]))
                vspom.append(right_branch(leafs[-j]))
        leafs.extend(vspom)
        vspom = []
    return leafs


def gen_bin_tree(root=2, height=6, left_branch=lambda l_r: l_r*3, right_branch=lambda r_r: r_r+4):
    """
    получает на вход корень дерева, высоту дерева и функции для левой и правой веток
    возвращает полное дерево с заданными параметрами вместе с изначальным корнем (root) в формате json

    > gen_bin_tree(2, 2, lambda l_r: l_r+2, lambda r_r: r_r+4)

    {
      "2": {
        "6": {
          "10": {},
          "8": {}
        },
        "4": {
          "8": {},
          "6": {}
        }
      }
    }
    """
    tree = get_leaf(root, height, left_branch, right_branch)
    tree = list(map(lambda x: {x: {}}, tree))
    for l in range(height-1, -1, -1):
        for m in range(2**l-1, 2**(l+1)-1):
            key = next(iter(tree[m]))
            right_child = tree.pop()
            left_child = tree.pop()
            tree[m][key].update(right_child)
            tree[m][key].update(left_child)
    return tree[0]



#print(json.dumps(gen_bin_tree(), indent=2))




