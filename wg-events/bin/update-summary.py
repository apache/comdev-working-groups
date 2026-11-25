#!/usr/bin/env python3
"""
Recalculate summary.yml totals from individual grant .txt files.

Usage:
    uv run update-summary.py [--fy FY2027]

Requires: pyyaml
"""
# /// script
# requires-python = ">=3.9"
# dependencies = ["pyyaml"]
# ///

import sys
import re
from pathlib import Path
import yaml

FY = sys.argv[2] if len(sys.argv) > 2 and sys.argv[1] == "--fy" else "FY2027"
BASE = Path.home() / "comdev-private" / "events-grants" / FY

CATEGORIES = {
    "speaker_travel": "speaker-travel",
    "meetups": "meetups",
    "sprints": "sprints",
    "summits": "summits",
    "materials": "materials",
}


def parse_grant_file(path):
    """Extract key fields from a .txt grant record."""
    content = path.read_text()
    fields = {}
    for line in content.splitlines():
        if ":" in line and not line.startswith(" ") and not line.startswith("#"):
            key, _, val = line.partition(":")
            fields[key.strip().lower()] = val.strip()
    return fields


def main():
    summary_path = BASE / "summary.yml"
    if not summary_path.exists():
        print(f"ERROR: {summary_path} not found")
        sys.exit(1)

    summary = yaml.safe_load(summary_path.read_text())
    summary["last_updated"] = str(__import__("datetime").date.today())

    for cat_key, dir_name in CATEGORIES.items():
        cat_dir = BASE / dir_name
        if not cat_dir.exists():
            continue

        grants = []
        approved_total = 0
        disbursed_total = 0
        approved_count = 0
        disbursed_count = 0

        for f in sorted(cat_dir.glob("*.txt")):
            fields = parse_grant_file(f)
            status = fields.get("status", "applied").lower()
            approved = int(re.sub(r"[^\d]", "", fields.get("approved amount", "0")) or 0)
            disbursed = int(re.sub(r"[^\d]", "", fields.get("actual spend", "0")) or 0)

            if status not in ("denied", "withdrawn"):
                approved_count += 1
                approved_total += approved
            if status == "reimbursed":
                disbursed_count += 1
                disbursed_total += disbursed

            grants.append({
                "id": f.stem,
                "approved": approved,
                "disbursed": disbursed,
                "status": status,
            })

        budget = summary[cat_key]["budget"]
        summary[cat_key]["grants"] = grants
        summary[cat_key]["totals"] = {
            "approved_count": approved_count,
            "approved_amount": approved_total,
            "disbursed_count": disbursed_count,
            "disbursed_amount": disbursed_total,
            "remaining": budget - approved_total,
        }

    # Grand totals
    grand_budget = sum(summary[k]["budget"] for k in CATEGORIES)
    grand_approved = sum(summary[k]["totals"]["approved_amount"] for k in CATEGORIES)
    grand_disbursed = sum(summary[k]["totals"]["disbursed_amount"] for k in CATEGORIES)
    summary["grand_totals"] = {
        "budget": grand_budget,
        "approved_amount": grand_approved,
        "disbursed_amount": grand_disbursed,
        "remaining": grand_budget - grand_approved,
    }

    summary_path.write_text(yaml.dump(summary, default_flow_style=False, sort_keys=False))
    print(f"Updated {summary_path}")
    print(f"  Approved: ${grand_approved:,} / ${grand_budget:,}")
    print(f"  Disbursed: ${grand_disbursed:,}")
    print(f"  Remaining: ${grand_budget - grand_approved:,}")


if __name__ == "__main__":
    main()
