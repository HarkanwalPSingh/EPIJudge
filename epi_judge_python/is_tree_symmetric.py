from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

def is_mirror(nodeA: BinaryTreeNode, nodeB: BinaryTreeNode) -> bool:
    if not nodeA and not nodeB:
        return True
    elif nodeA and nodeB:
        return (nodeA.data == nodeB.data) and \
        is_mirror(nodeA.left, nodeB.right) and \
        is_mirror(nodeA.right, nodeB.left)
    else:
        return False

def is_symmetric(tree: BinaryTreeNode) -> bool:
    """
    Space:
    Time :

    Helper - isMirror
    """
    return not tree or is_mirror(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
