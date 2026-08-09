# summary.yml Data Format

## Purpose

`summary.yml` is the fiscal-year ledger for the events grants program.
It lives in the private SVN repo at:

    https://svn.apache.org/repos/private/pmc/comdev/events-grants/FY20XX/summary.yml

It is **internal only** -- budget amounts and individual grant details
are never published. Only aggregate counts go in the quarterly public
report.

## Who updates it

The wg-events committee chair (or designee) updates this file after
each grant approval and each reimbursement disbursement.

## When to update

- After a grant is approved: add entry to the relevant `grants` list,
  update `totals`
- After receipts are filed and reimbursement is processed: update
  `disbursed` on the entry, update `totals`
- After any status change worth tracking

## Schema

```yaml
# -----------------------------------------------------------
# Events Grants Ledger -- FY2027
# INTERNAL ONLY -- do not publish dollar amounts
# -----------------------------------------------------------

fiscal_year: FY2027          # string, format "FY" + 4-digit year
last_updated: 2027-03-15     # ISO date, updated on every commit

# ----- Per-category sections -----
# Each category has: budget, grants (list), totals (computed)

speaker_travel:
  budget: 30000              # integer, dollars, set at start of FY

  grants:                    # list of individual grants
    - id: "2027-01-spitzer-iceberg-summit"   # matches filename in speaker-travel/
      applicant: "Russell Spitzer"           # display name
      conference: "Apache Iceberg Summit"
      date: 2027-02-15                       # conference start date
      approved: 2400                         # integer, dollars approved
      disbursed: 2400                        # integer, dollars actually paid out
      status: reimbursed                     # see Status Values below

    - id: "2027-03-garcia-kubecon-eu"
      applicant: "Maria Garcia"
      conference: "KubeCon EU"
      date: 2027-04-02
      approved: 2800
      disbursed: 0
      status: approved

  totals:                    # recompute after every change
    approved_count: 2        # number of grants approved
    approved_amount: 5200    # sum of all approved
    disbursed_count: 1       # number fully reimbursed
    disbursed_amount: 2400   # sum of all disbursed
    remaining: 24800         # budget - approved_amount

meetups:
  budget: 9600

  grants:
    - id: "2027-02-alc-bangalore-feb"
      organizer: "Sagara Gunathunga"
      project: "general"               # or specific project name
      location: "Bangalore, India"
      date: 2027-02-22
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

# ----- Grand totals -----
# Recompute from category totals after every change

grand_totals:
  budget: 79600
  approved_amount: 5550
  disbursed_amount: 2720
  remaining: 74050
```

## Field Reference

### Top-level fields

| Field | Type | Description |
|-------|------|-------------|
| fiscal_year | string | "FY" + year (e.g., "FY2027") |
| last_updated | date | ISO date of last edit |

### Category fields (speaker_travel, meetups, sprints, summits, materials)

| Field | Type | Description |
|-------|------|-------------|
| budget | integer | Allocated dollars for this category this FY |

### Grant entry fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Matches the .txt filename (without extension) |
| applicant / organizer | string | yes | Person's display name |
| conference / project | string | yes | What it's for |
| location | string | meetups/sprints/summits only | City, Country |
| date | date | yes | Event start date |
| approved | integer | yes | Dollars approved (0 if pending) |
| disbursed | integer | yes | Dollars paid out (0 until reimbursed) |
| status | string | yes | See Status Values below |

### Totals fields (computed -- update manually after each change)

| Field | Type | Description |
|-------|------|-------------|
| approved_count | integer | Number of grants with status != denied |
| approved_amount | integer | Sum of all `approved` fields |
| disbursed_count | integer | Number with status == reimbursed |
| disbursed_amount | integer | Sum of all `disbursed` fields |
| remaining | integer | budget - approved_amount |

## Status Values

| Status | Meaning |
|--------|---------|
| applied | Application received, not yet evaluated |
| approved | Evaluated and approved; awaiting event + receipts |
| denied | Evaluated and denied |
| completed | Event attended; awaiting receipts |
| receipts_filed | Receipts submitted; awaiting reimbursement |
| reimbursed | Money paid out; grant complete |
| withdrawn | Applicant withdrew or event cancelled |

## Commit Convention

One `svn ci` per logical change. Commit message format:

    [events-grants] [category] id: description

Examples:

    [events-grants] [speaker-travel] garcia-kubecon-eu: approved $2800
    [events-grants] [meetups] alc-bangalore-feb: reimbursed $320
    [events-grants] totals: updated after March disbursements

## Quarterly Public Report

Generated from this file but **stripped of dollar amounts and names**.
Public report shows only:

- Number of grants awarded per category
- Number of events funded per category
- Geographic distribution (continents/countries)
- Total events count and total people reached (estimated)

Script to generate: TBD (simple Python that reads summary.yml and
outputs the aggregate markdown).

## Versioning

This format will evolve. Breaking changes get a version bump at the
top of the file:

```yaml
format_version: 1   # increment on breaking schema changes
```

Non-breaking additions (new optional fields) don't require a version
bump.
