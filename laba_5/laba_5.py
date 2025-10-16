import json

def get_leaf(root=2, height=6, left_branch=lambda l_r: l_r*3, right_branch=lambda r_r: r_r+4):
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
        for k in range(len(vspom)):
            leafs.append(vspom[k])
        vspom = []
    return leafs



def gen_bin_tree1(root=2, height=6, left_branch=lambda l_r: l_r*3, right_branch=lambda r_r: r_r+4):
    tree = get_leaf(root, height, left_branch, right_branch)
    tree = list(map(lambda x: {x: {}}, tree))
    for l in range(height-1, 0, -1):
        for m in range(2**l, 2**(l+1)):
            #tree[m-1] = {tree[m-1]: {tree[-1]: {}, tree[-2]: {}}}
            key = list(tree[m].keys())[0]
            tree[m-1][key] = {tree[-1], tree[-2]}
            tree = tree[:-2]
    return tree



print(json.dumps(gen_bin_tree1(2, 3, lambda l_r: l_r+1, lambda r_r: r_r+3), indent=2))




