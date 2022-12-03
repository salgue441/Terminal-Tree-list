""" This module provides the RP Tree Cli """

import argparse
import pathlib
import sys

from . import __version__
from .rptree import DirectoryTree


def main() -> None:
    """ The main routine. 
        :param None
        :return None
    """

    args = parse_cmd_line_arguments()
    root_dir = pathlib.Path(args.root_dir)

    if not root_dir.is_dir():
        print(f"Error: {root_dir} is not a directory.")
        sys.exit(1)

    tree = DirectoryTree(root_dir)
    tree.generate()


def parse_cmd_line_arguments() -> argparse.Namespace:
    """ Parse the command line arguments.
        :param None
        :return: The parsed arguments.
    """

    parser = argparse.ArgumentParser(
        prog="tree",
        description="Print a directory tree.",
        epilog="Thanks for using RP Tree!",
    )

    parser.version = f"RP Tree v{__version__}"
    parser.add_argument("-v", "--version", action="version")

    parser.add_argument(
        "root_dir",
        metavar="ROOT_DIR",
        nargs="?",
        default=".",
        help="Generate a full directory tree starting at ROOT_DIR",
    )

    return parser.parse_args()
