from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

def isBalanced(tree: BinaryTreeNode) -> tuple[bool, int]:
    if not tree:
      return True, -1
    
    isLeftTreeBalanced, leftHeight = isBalanced(tree.left)
    isRightTreeBalanced, rightHeight = isBalanced(tree.right)

    isSkew = abs(leftHeight - rightHeight) > 1

    return (isLeftTreeBalanced and isRightTreeBalanced and not isSkew), 1 + max(leftHeight, rightHeight)


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    """
    Time: O(N)
    Space: O(N)
    """
    
    return isBalanced(tree)[0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
