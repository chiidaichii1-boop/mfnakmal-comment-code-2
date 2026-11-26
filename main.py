"""Write one funny, painfully honest comment above fragile production code."""

import os

LINE = "Do not refactor this. The last person who tried now runs a goat farm in Wales."

# The gate allows 1-200 characters; keep the line well inside it.
assert 1 <= len(LINE) <= 200

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
