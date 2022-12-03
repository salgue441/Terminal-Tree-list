# TREE TERMINAL VISUALIZER

Command line tool to list the contents of a directory or folder in a tree-like diagram
with a vertical layout.

## Output

The output is a tree-like diagram of the contents of the directory or folder. The diagram is printed to the terminal.

```bash
..\rptree_test\
├───.git
│   ├───hooks
│   ├───info
│   ├───logs
│   │   └───refs
│   │       ├───heads
│   │       └───remotes
│   │           └───origin
│   ├───objects
│   │   ├───info
│   │   └───pack
│   └───refs
│       ├───heads
│       ├───remotes
│       │   └───origin
│       └───tags
│
├───hello\
│   └───hello.py
│   └───__init__.py
│
├───tests\
│   └───test_hello.py
│
├───.gitignore
├───LICENSE
├───requirements.txt
├───setup.py
└───README.md
```

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

## Commands

### Current Version

```bash
python tree.py -v
```

Output

```bash
RP Tree v0.1.0
```

### Help Message

```bash
python tree.py --help
```

Output

```bash
usage: tree [-h] [-v] [ROOT_DIR]

Print a directory tree.

positional arguments:
  ROOR_DIR            Generates a full directory tree starting at ROOT_DIR

options:
  -h, --help          show this help message and exit
  -v, --version       show program's version number and exit

Thanks for using RP Tree!
```
