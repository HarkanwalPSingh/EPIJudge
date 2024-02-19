import functools
from typing import Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook
from collections import namedtuple


Status = namedtuple('Status', ('targetNodes', 'ancestor'))

def lcaHelper(tree: BinaryTreeNode, node0: BinaryTreeNode, node1: BinaryTreeNode):
    
    if not tree:
        return Status(targetNodes=0, ancestor=None)
    
    leftResult = lcaHelper(tree.left, node0, node1)
    if leftResult.targetNodes == 2:
      return leftResult
    
    rightResult = lcaHelper(tree.right, node0, node1)
    if rightResult.targetNodes == 2:
        return rightResult
    
    targetNodes = 0

    if node0 == tree:
      targetNodes += 1
    if node1 == tree:
      targetNodes += 1
    
    targetNodes += (leftResult.targetNodes + rightResult.targetNodes)

    return Status(targetNodes=targetNodes, ancestor=tree if targetNodes == 2 else None)

def lca(tree: BinaryTreeNode, node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:

    return lcaHelper(tree,node0,node1).ancestor


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
