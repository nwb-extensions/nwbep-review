#!/usr/bin/env python3
"""Extract comments from a .docx file (Google Docs export preserves them).

Usage: python3 extract_comments.py NWBEP004.docx > NWBEP004_comments.json

Google Docs exports include comments as w:comment elements in the
word/comments.xml part of the .docx ZIP archive.
"""

import json
import sys
import xml.etree.ElementTree as ET
import zipfile

WORD_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"


def extract_comments(docx_path: str) -> list[dict]:
    """Extract comments from a .docx file."""
    comments = []

    with zipfile.ZipFile(docx_path, "r") as zf:
        # Check if comments.xml exists
        if "word/comments.xml" not in zf.namelist():
            return comments

        with zf.open("word/comments.xml") as f:
            tree = ET.parse(f)

        root = tree.getroot()

        for comment in root.findall(f"{{{WORD_NS}}}comment"):
            comment_id = comment.get(f"{{{WORD_NS}}}id", "")
            author = comment.get(f"{{{WORD_NS}}}author", "")
            date = comment.get(f"{{{WORD_NS}}}date", "")
            initials = comment.get(f"{{{WORD_NS}}}initials", "")

            # Extract text from all paragraphs in the comment
            text_parts = []
            for para in comment.findall(f".//{{{WORD_NS}}}p"):
                para_text = ""
                for run in para.findall(f".//{{{WORD_NS}}}r"):
                    for t in run.findall(f"{{{WORD_NS}}}t"):
                        if t.text:
                            para_text += t.text
                if para_text:
                    text_parts.append(para_text)

            comments.append(
                {
                    "id": comment_id,
                    "author": author,
                    "initials": initials,
                    "date": date,
                    "text": "\n".join(text_parts),
                }
            )

    return comments


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file.docx>", file=sys.stderr)
        sys.exit(1)

    docx_path = sys.argv[1]
    comments = extract_comments(docx_path)

    print(json.dumps(comments, indent=2, ensure_ascii=False))

    # Summary to stderr
    if comments:
        authors = {}
        for c in comments:
            author = c["author"]
            authors[author] = authors.get(author, 0) + 1
        print(f"\nExtracted {len(comments)} comments:", file=sys.stderr)
        for author, count in sorted(authors.items()):
            print(f"  {author}: {count}", file=sys.stderr)
    else:
        print("No comments found in document.", file=sys.stderr)


if __name__ == "__main__":
    main()
