"""Notes From a Passive-Aggressive Fridge -- one-line entry for make.fun.

Writes a single dry, petty note from a passive-aggressive fridge to
/output/entry.txt. Standard library only, fully deterministic: the same
note every run.
"""

import os

LINE = (
    "The door alarm went off 14 times today. I counted. I always count."
)


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
