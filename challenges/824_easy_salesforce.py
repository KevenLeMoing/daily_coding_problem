"""
Write a program to merge two binary trees. Each node in the new tree should hold a value equal to the sum of the values
of the corresponding nodes of the input trees.
If only one input tree has a node in a given position, the corresponding node in the new tree
should match that input node.
"""


class BinaryTree:
    def __init__(self):
        self.right_node = 0
        self.left_node = 0

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