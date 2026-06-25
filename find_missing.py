#!/usr/bin/env python3
"""Find missing translation entries in QueueMetrics / WombatDialer label files.

Usage:
    find_missing.py            # list all locales that still have missing entries
    find_missing.py <locale>   # show the detail of every missing entry for a locale

A missing entry is the two-line block:

        # 🔴 key -> English text for reference   (or '👽' when an alien value exists)
        ➡️ key=

i.e. an arrowed line whose value (right of '=') is empty.
"""

import glob
import os
import re
import sys

ARROW = "➡"  # ➡️ marks an empty/untranslated value line

# (product label, filename glob) -> locale is the part matched by the '*'
PRODUCTS = [
    ("queuemetrics", "queuemetrics_*.md"),
    ("wombatdialer", os.path.join("WombatDialer", "wombatdialer_*.md")),
]

# directory of this script, so it works regardless of the current working dir
ROOT = os.path.dirname(os.path.abspath(__file__))


def locale_of(path, prefix):
    """Extract the locale from a file path, e.g. queuemetrics_th_TH.md -> th_TH."""
    name = os.path.basename(path)
    return name[len(prefix) + 1 : -len(".md")]  # strip 'prefix_' and '.md'


def files_for_locale(locale=None):
    """Yield (product, locale, path) for every label file (optionally one locale)."""
    for product, pattern in PRODUCTS:
        for path in sorted(glob.glob(os.path.join(ROOT, pattern))):
            loc = locale_of(path, product)
            if loc == "en_US":
                continue  # English is the source, never "missing"
            if locale is None or loc == locale:
                yield product, loc, path


def missing_entries(path):
    """Return a list of (lineno, reference_comment, arrow_line) for missing entries."""
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().splitlines()

    out = []
    for i, line in enumerate(lines):
        if ARROW not in line:
            continue
        # value is everything after the first '='; missing == empty value
        _, _, value = line.partition("=")
        if value.strip():
            continue
        prev = lines[i - 1].strip() if i > 0 and lines[i - 1].lstrip().startswith("#") else ""
        out.append((i + 1, prev, line.strip()))
    return out


def list_locales():
    """Print every locale that has missing entries, with per-product counts."""
    totals = {}  # locale -> {product: count}
    for product, loc, path in files_for_locale():
        n = len(missing_entries(path))
        if n:
            totals.setdefault(loc, {})[product] = n

    if not totals:
        print("No missing translations found. \U0001f389")
        return

    width = max(len(loc) for loc in totals)
    print("Locales with missing translations:\n")
    for loc in sorted(totals, key=lambda l: -sum(totals[l].values())):
        parts = ", ".join(f"{p}: {c}" for p, c in sorted(totals[loc].items()))
        total = sum(totals[loc].values())
        print(f"  {loc:<{width}}  {total:>4}  ({parts})")
    print(f"\n{len(totals)} locale(s) need work.")


def show_locale(locale):
    """Print the detail of every missing entry for one locale."""
    found_any = False
    for product, loc, path in files_for_locale(locale):
        entries = missing_entries(path)
        if not entries:
            continue
        found_any = True
        rel = os.path.relpath(path, ROOT)
        print(f"\n=== {rel}  ({len(entries)} missing) ===")
        for lineno, ref, arrow in entries:
            if ref:
                print(f"  {lineno}: {ref}")
            print(f"  {lineno}: {arrow}")

    if not found_any:
        # distinguish "complete" from "no such file"
        if any(True for _ in files_for_locale(locale)):
            print(f"No missing entries for locale '{locale}'. ✅")
        else:
            print(f"No label files found for locale '{locale}'.")


def main(argv):
    if len(argv) > 1:
        show_locale(argv[1])
    else:
        list_locales()


if __name__ == "__main__":
    main(sys.argv)
