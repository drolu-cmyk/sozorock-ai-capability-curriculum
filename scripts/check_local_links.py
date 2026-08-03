#!/usr/bin/env python3
"""Check relative Markdown links without making network requests."""

from pathlib import Path
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
SKIP_PREFIXES = ("http://", "https://", "mailto:", "#")

def main() -> None:
    errors = []
    for md in ROOT.rglob("*.md"):
        if any(part in {".git", "node_modules"} for part in md.parts):
            continue
        text = md.read_text(encoding="utf-8")
        for raw_target in LINK_RE.findall(text):
            target = raw_target.split("#", 1)[0].strip().strip("<>")
            if not target or target.startswith(SKIP_PREFIXES):
                continue
            path = (md.parent / unquote(target)).resolve()
            try:
                path.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"{md.relative_to(ROOT)} -> outside repository: {target}")
                continue
            if not path.exists():
                errors.append(f"{md.relative_to(ROOT)} -> missing: {target}")
    if errors:
        print("\n".join(f"ERROR: {e}" for e in errors))
        sys.exit(1)
    print("OK: local Markdown links resolve")

if __name__ == "__main__":
    main()
