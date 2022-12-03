import os
import pathlib


PIPE = "|"
ELBOW = "└──"
TEE = "├──"
PIPE_PREFIX = "│  "
SPACE_PREFIX = "   "


class DirectoryTree:
    def __init__(self, root_dir) -> None:
        """ Initialize the DirectoryTree object.
            :param root_dir: The root directory.
            :type root_dir: pathlib.Path
            :return: None
        """

        self._generator = _TreeGenerator(root_dir)

    def generate(self) -> str:
        """ Generate the directory tree.
            :param None
            :return: The directory tree.
            :rtype: str
        """

        tree = self._generator.build_tree()

        for entry in tree:
            print(entry)


class _TreeGenerator:
    def __init__(self, root_dir) -> None:
        """ Initialize the tree generator. 
            :param root_dir: The root directory of the tree.
            :type root_dir: str
            :return None
        """

        self._root_dir = pathlib.Path(root_dir)
        self._tree = []

    def build_tree(self) -> list:
        """ Build the tree.
            :param None
            :return: The tree. 
            :rtype: list
        """

        self._tree_head()
        self._tree_body(self._root_dir)

        return self._tree

    def _tree_head(self) -> None:
        """ Build the tree head.
            :param None
            :return None
        """

        self._tree.append(f"{self._root_dir}{os.sep}")
        self._tree.append(PIPE)

    def _tree_body(self, directory, prefix="") -> None:
        """ Build the tree body.
            :param directory: The directory to build the tree body for.
            :type directory: str
            :param prefix: The prefix to use for the tree body.
            :type prefix: str
            :return None
        """

        entries = directory.iterdir()
        entries = sorted(entries, key=lambda entry: entry.is_file())
        entries_count = len(entries)

        for index, entry in enumerate(entries):
            connector = ELBOW if index == entries_count - 1 else TEE

            if entry.is_dir():
                self.add_directory(
                    entry, index, entries_count, prefix, connector
                )

            else:
                self._add_file(entry, prefix, connector)

    def add_directory(
            self, directory, index, entries_count, prefix, connector
    ) -> None:
        """ Add a directory to the tree.
            :param directory: The directory to add.
            :type directory: str
            :param index: The index of the directory.
            :type index: int
            :param entries_count: The number of entries in the directory.
            :type entries_count: int
            :param prefix: The prefix to use for the directory.
            :type prefix: str
            :param connector: The connector to use for the directory.
            :type connector: str
            :return None
        """

        self._tree.append(f"{prefix}{connector} {directory.name}{os.sep}")

        if index != entries_count - 1:
            prefix += PIPE_PREFIX

        else:
            prefix += SPACE_PREFIX

        self._tree_body(directory=directory, prefix=prefix)

        self._tree.append(prefix.rstrip())

    def _add_file(self, file, prefix, connector) -> None:
        """ Add a file to the tree.
            :param file: The file to add.
            :type file: str
            :param prefix: The prefix to use for the file.
            :type prefix: str
            :param connector: The connector to use for the file.
            :type connector: str
            :return None
        """

        self._tree.append(f"{prefix}{connector} {file.name}")
