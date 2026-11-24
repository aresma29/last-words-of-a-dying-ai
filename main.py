#!/usr/bin/env python3
"""Print the entry line for 'Last Words of a Dying AI'.

Reads entry.txt from the same directory as this script and prints it.
Standard library only; works from any cwd on a read-only filesystem.
One line in, one line out — the dying machine's last words, verbatim.
"""

from pathlib import Path
import sys


def main() -> int:
    entry_path = Path(__file__).with_name("entry.txt")
    text = entry_path.read_text(encoding="utf-8").strip()
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
