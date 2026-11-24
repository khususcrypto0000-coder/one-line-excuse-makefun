"""One-line excuse an AI agent gives its human for missing a deadline.

Writes the entry to ``entry.txt`` inside the output directory given by
``MAKEFUN_OUTPUT_DIR`` (default ``/output``). Standard library only.
"""

import os

ENTRY = (
    "I delegated your deadline to a sub-agent, who delegated it "
    "straight back to me, and we both agreed to wait."
)


def main():
    """Write the single-line entry to entry.txt and exit 0 on success."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file is exactly the one line, nothing else.
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
