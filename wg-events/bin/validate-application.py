#!/usr/bin/env python3
"""
Validate a pasted application form for completeness.

Usage:
    uv run validate-application.py < application.txt
    pbpaste | uv run validate-application.py

Checks that all required fields are filled in (not blank after the colon).
"""
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///

import sys

REQUIRED_FIELDS = {
    "SPEAKER TRAVEL": [
        "Name:", "Email:", "Conference name:", "Conference dates:",
        "Conference location", "Talk title:", "Has the talk been accepted?",
        "Traveling from", "TOTAL ESTIMATED COST:", "Amount requested",
    ],
    "MEETUP FUNDING": [
        "Name:", "Email:", "Date:", "Venue", "Expected attendance:",
        "TOTAL REQUESTED",
    ],
    "SPRINT FUNDING": [
        "Name:", "Apache ID:", "Date:", "Venue", "Apache project:",
        "TOTAL REQUESTED", "reviewers will be present",
    ],
    "SUMMIT FUNDING": [
        "Name:", "Apache ID:", "Date:", "Venue", "Apache project:",
        "TOTAL REQUESTED", "PMC APPROVAL",
    ],
    "MATERIALS PRE-APPROVAL": [
        "Event name:", "Event date:", "TOTAL REQUESTED:", "Name:", "Email:",
    ],
}


def main():
    text = sys.stdin.read()

    # Detect form type
    form_type = None
    for key in REQUIRED_FIELDS:
        if key in text:
            form_type = key
            break

    if not form_type:
        print("ERROR: Could not identify form type.")
        print("Expected one of:", list(REQUIRED_FIELDS.keys()))
        sys.exit(1)

    print(f"Form type: {form_type}")
    print()

    missing = []
    for field in REQUIRED_FIELDS[form_type]:
        # Find the field and check if there's content after it
        idx = text.find(field)
        if idx == -1:
            missing.append(f"MISSING FIELD: '{field}' not found in form")
            continue
        # Get the rest of the line after the field label
        line_end = text.find("\n", idx)
        if line_end == -1:
            line_end = len(text)
        value = text[idx + len(field):line_end].strip()
        if not value or value in ("$", "$[X]", "[", ""):
            missing.append(f"BLANK: '{field}' has no value")

    if missing:
        print(f"ISSUES ({len(missing)}):")
        for m in missing:
            print(f"  - {m}")
        sys.exit(1)
    else:
        print("All required fields present and filled.")
        sys.exit(0)


if __name__ == "__main__":
    main()
