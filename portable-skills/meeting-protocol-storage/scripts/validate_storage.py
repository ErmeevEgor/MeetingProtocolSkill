#!/usr/bin/env python3
"""Validate a Confluence Storage Format XML/XHTML fragment using stdlib XML parser."""
from __future__ import annotations

import argparse
from pathlib import Path
import sys
import xml.etree.ElementTree as ET

ROOT_OPEN = (
    '<root '
    'xmlns:ac="http://atlassian.com/content" '
    'xmlns:ri="http://atlassian.com/resource/identifier" '
    'xmlns:at="http://atlassian.com/template">'
)
ROOT_CLOSE = '</root>'


def validate_fragment(text: str) -> None:
    stripped = text.strip()
    if stripped.startswith('```') or stripped.endswith('```'):
        raise ValueError('Storage Format must not be wrapped in Markdown code fences')
    if '<html' in stripped.lower() or '<body' in stripped.lower() or '<head' in stripped.lower():
        raise ValueError('Storage Format output must be a fragment, not a full HTML document')
    ET.fromstring(ROOT_OPEN + stripped + ROOT_CLOSE)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=Path)
    args = parser.parse_args()
    try:
        text = args.file.read_text(encoding='utf-8-sig')
        validate_fragment(text)
    except (OSError, UnicodeError, ValueError, ET.ParseError) as exc:
        print(f'INVALID: {exc}', file=sys.stderr)
        return 1
    print(f'OK: {args.file}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
