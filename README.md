# TREE TERMINAL VISUALIZER

Command line tool to list the contents of a directory or folder in a tree-like diagram.

## How it works

1. Gets the path to a directory on your file system.
2. Opens the directory
3. Get a list of all its entries (directories and files)
4. If the directory contains subdirectories, then repeat the process from step two.

## Tree Body Representation

Includes the following components:

- A prefix string that provides the required spacing to reflect the position of
  an entry in the directory structure.
- A character that connects the current subdirectory or file to its parent.
- The name of the current subdirectory or file.
