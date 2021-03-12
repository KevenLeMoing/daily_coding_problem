"""
Write a program to merge two binary trees. Each node in the new tree should hold a value equal to the sum of the values
of the corresponding nodes of the input trees.
If only one input tree has a node in a given position, the corresponding node in the new tree
should match that input node.
"""


class BinaryTree:
    def __init__(self, right: int = 0, left: int = 0):
        self.right_node = right
        self.left_node = left

    def set_right_node(self, value: int):
        self.right_node = value

    def set_left_node(self, value: int):
        self.left_node = value

    def get_right_node(self) -> int:
        return self.right_node

    def get_left_node(self) -> int:
        return self.left_node


def merge_binary_trees(tree1: BinaryTree, tree2: BinaryTree) -> BinaryTree:
    """Merge two binaries tree into one. This tree should hold a value equal to the sum of the values
    of the corresponding nodes of the input trees.
    """
    merge_result = BinaryTree()
    merge_result.set_right_node(value=tree1.get_right_node() + tree2.get_right_node())
    merge_result.set_left_node(value=tree1.get_left_node() + tree2.get_left_node())
    return merge_result


first_tree = BinaryTree(3, 6)
second_tree = BinaryTree(4, 9)

fusion = merge_binary_trees(first_tree, second_tree)
print('right node is:{}'.format(fusion.get_right_node()))
print('left node is:{}'.format(fusion.get_left_node()))
