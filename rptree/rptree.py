import os
import pathlib


PIPE = "|"
ELBOW = "└──"
TEE = "├──"
PIPE_PREFIX = "│  "
SPACE_PREFIX = "   "


class DirectoryTree:
    def __init__(self, root_dir):
        self._generator = _TreeGenerator(root_dir)

    def generate(self):
        tree = self._generator.build_tree()

        for entry in tree:
            print(entry)


class _TreeGenerator:
    def __init__(self, root_dir):
        """ Initialize the tree generator. 
            :param root_dir: The root directory of the tree.
            :type root_dir: str
            :return None
        """

        self._root_dir = pathlib.Path(root_dir)
        self._tree = []

    def build_tree(self):
        """ Build the tree.
            :param None
            :return: The tree. """

        self._tree_head()
        self._tree_body(self._root_dir)

        return self._tree

    def _tree_head(self):
        """ Build the tree head.
            :param None
            :return None
        """

        self._tree.append(f"{self._root_dir}{os.sep}")
        self._tree.append(PIPE)
