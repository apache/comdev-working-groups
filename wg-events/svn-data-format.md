# SVN Data Format & Directory Structure

## Location

All grant tracking data lives in the private ComDev PMC SVN repo:

    https://svn.apache.org/repos/private/pmc/comdev/events-grants/

## Directory Structure

```
events-grants/
├── README.txt              ← This format spec
├── FY2027/
│   ├── speaker-travel/
│   │   ├── 2027-01-spitzer-iceberg-summit.txt
│   │   ├── 2027-03-garcia-kubecon-eu.txt
│   │   └── ...
│   ├── meetups/
│   │   ├── 2027-02-alc-bangalore-feb.txt
│   │   ├── 2027-03-flink-meetup-berlin.txt
│   │   └── ...
│   ├── sprints/
│   │   ├── 2027-04-tomcat-sprint-london.txt
│   │   └── ...
│   ├── summits/
│   │   ├── 2027-06-nuttx-community-day.txt
│   │   └── ...
│   ├── materials/
│   │   ├── 2027-02-alc-bangalore-feb.txt
│   │   └── ...
│   └── summary.yml         ← Running FY ledger (YAML)
├── FY2028/
│   └── ...
└── templates/
    ├── speaker-travel.txt
    ├── meetup.txt
    ├── sprint.txt
    ├── summit.txt
    └── materials.txt
```

## Naming Convention

Files are named: `YYYY-MM-shortname-event.txt`

- YYYY-MM: Month the grant was approved
- shortname: Applicant last name or ALC/project name
- event: Brief event identifier

## File Formats

All files are plain text, fixed-field format. One file per grant.

---

### Speaker Travel Grant Record

```
SPEAKER TRAVEL GRANT
====================
Status: [APPLIED | APPROVED | DENIED | COMPLETED | REIMBURSED]

Applicant:       [name]
Apache ID:       [id or "none"]
Email:           [email]

Conference:      [name]
Location:        [city, country]
Dates:           [YYYY-MM-DD to YYYY-MM-DD]
Talk title:      [title]
Apache project:  [project name]

Travel from:     [city, country]
Continent match: [same-continent | inter-continental (override)]

Applied:         YYYY-MM-DD
Evaluated by:    [evaluator1], [evaluator2]
Score:           [X/15]
Decision:        [APPROVED | DENIED]
Decision date:   YYYY-MM-DD
Approved amount: $[X]

Actual spend:    $[X] (filled after receipts)
Receipts filed:  YYYY-MM-DD
Reimbursed:      YYYY-MM-DD
Reimbursed via:  [method -- e.g., "ASF Treasurer wire"]

Deliverable:     [URL to blog post / slides / trip report]
Deliverable date: YYYY-MM-DD

Notes:
[free-form notes, one per line]
```

---

### Meetup Grant Record

```
MEETUP GRANT
============
Status: [APPLIED | APPROVED | COMPLETED | REIMBURSED]

Organizer:       [name]
Apache ID:       [id or "none"]
ALC Chapter:     [name or "none"]
Email:           [email]

Event:           [description]
Project:         [Apache project or "general"]
Location:        [city, country]
Date:            YYYY-MM-DD
Attendance:      [expected] / [actual] (actual filled post-event)

Applied:         YYYY-MM-DD
Approved by:     [committee member]
Approved amount: $[X]

Actual spend:    $[X]
Receipts filed:  YYYY-MM-DD
Reimbursed:      YYYY-MM-DD

Report posted:   [Yes/No] (to dev@community)
Report date:     YYYY-MM-DD

Notes:
[free-form]
```

---

### Sprint Grant Record

```
SPRINT GRANT
============
Status: [APPLIED | APPROVED | COMPLETED | REIMBURSED]

Organizer:       [name]
Apache ID:       [id]
Email:           [email]

Project:         [Apache project]
Location:        [city, country]
Date:            YYYY-MM-DD
Attendance:      [expected] / [actual]
Reviewers present: [count]

Applied:         YYYY-MM-DD
Evaluated by:    [evaluator1], [evaluator2]
Approved amount: $[X]

Actual spend:    $[X]
Receipts filed:  YYYY-MM-DD
Reimbursed:      YYYY-MM-DD

Outcomes:
  PRs submitted: [count]
  Issues closed: [count]
  New contributors: [count]

Report posted:   [Yes/No]
Report date:     YYYY-MM-DD

Notes:
[free-form]
```

---

### Summit Grant Record

```
SUMMIT GRANT
============
Status: [APPLIED | APPROVED | COMPLETED | REIMBURSED]

Organizer:       [name]
Apache ID:       [id]
Email:           [email]

Project:         [Apache project]
PMC approval:    [URL to lists.apache.org thread]
Location:        [city, country]
Date:            YYYY-MM-DD
Attendance:      [expected] / [actual]

Applied:         YYYY-MM-DD
Evaluated by:    [evaluator1], [evaluator2]
ComDev PMC vote: [thread URL or date]
Approved amount: $[X]

Actual spend:    $[X]
Receipts filed:  YYYY-MM-DD
Reimbursed:      YYYY-MM-DD

Report posted:   [Yes/No]
Report date:     YYYY-MM-DD

Notes:
[free-form]
```

---

### Materials Reimbursement Record

```
MATERIALS REIMBURSEMENT
=======================
Status: [PRE-APPROVED | RECEIPTS FILED | REIMBURSED]

Organizer:       [name]
Email:           [email]
Event:           [event name and date]
Associated grant: [link to meetup/sprint/summit file, if any]

Pre-approved:    YYYY-MM-DD
Approved by:     [committee member]
Approved amount: $[X]

Items:
  [item] -- $[X]
  [item] -- $[X]
  [item] -- $[X]

Actual spend:    $[X]
Receipts filed:  YYYY-MM-DD
Reimbursed:      YYYY-MM-DD

Notes:
[free-form]
```

---

### summary.yml (per fiscal year)

YAML format -- human-editable, machine-parseable, supports comments.

```yaml
# FY2027 Events Grants Ledger
# Updated by committee chair after each disbursement
# INTERNAL ONLY -- do not publish dollar amounts

fiscal_year: FY2027
last_updated: 2027-01-15

speaker_travel:
  budget: 30000
  grants:
    - id: 2027-01-spitzer-iceberg-summit
      approved: 2400
      disbursed: 2400
      status: reimbursed
    - id: 2027-03-garcia-kubecon-eu
      approved: 2800
      disbursed: 0
      status: approved
  totals:
    approved_count: 2
    approved_amount: 5200
    disbursed_count: 1
    disbursed_amount: 2400
    remaining: 24800

meetups:
  budget: 9600
  grants:
    - id: 2027-02-alc-bangalore-feb
      approved: 350
      disbursed: 320
      status: reimbursed
  totals:
    approved_count: 1
    approved_amount: 350
    disbursed_count: 1
    disbursed_amount: 320
    remaining: 9250

sprints:
  budget: 18000
  grants: []
  totals:
    approved_count: 0
    approved_amount: 0
    disbursed_count: 0
    disbursed_amount: 0
    remaining: 18000

summits:
  budget: 18000
  grants: []
  totals:
    approved_count: 0
    approved_amount: 0
    disbursed_count: 0
    disbursed_amount: 0
    remaining: 18000

materials:
  budget: 4000
  grants: []
  totals:
    approved_count: 0
    approved_amount: 0
    disbursed_count: 0
    disbursed_amount: 0
    remaining: 4000

# Computed from above -- update after each change
grand_totals:
  budget: 79600
  approved_amount: 5550
  disbursed_amount: 2720
  remaining: 74050
```

**Why YAML:**
- Comments allowed (annotations, dates, context)
- Human-editable with any text editor (no trailing-comma traps)
- `yaml.safe_load()` in Python for reporting scripts
- Diff-friendly in SVN (one field per line)
- Individual grant entries are minimal (just id + amounts + status)
  with full detail in the per-grant .txt files

## Workflow

1. Application arrives on events-grants@ list
2. Committee member creates the record file in SVN with Status: APPLIED
3. As evaluation/approval happens, update the file
4. After reimbursement, update to REIMBURSED and fill actual amounts
5. Update summary.txt with running totals after each disbursement
6. Quarterly: use summary.txt to generate the public report
   (aggregate numbers only -- no names or specific amounts published)

## Notes

- All files are plain text -- editable with any text editor
- One `svn ci` per status change (keeps clean history)
- Commit messages: "[events-grants] [type] shortname: status change"
  e.g., "[events-grants] [speaker-travel] garcia: APPROVED $2,400"
- Budget amounts in summary.txt are internal -- never published
