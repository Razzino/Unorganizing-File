# File Unorganizer (Python)

A simple Python utility that reverses folder organization by moving
all files from subfolders back into the main directory.

After moving the files, empty subfolders are automatically removed.

## Features

- Moves files from subfolders back to the main folder
- Removes empty directories after cleanup
- Ignores locked or non-empty folders safely
- Simple and lightweight automation script

## How to Run

1. Make sure Python 3 is installed
2. Clone or download this repository
3. Open the script and set the target folder:

```python
folder = r"path/to/your/folder"
```
4. Run the script:
```python
python unorganize.py
```
